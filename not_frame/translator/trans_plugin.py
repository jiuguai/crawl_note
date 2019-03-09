#!/usr/bin/python
#-*- encoding: utf-8 -*-


import sublime
import sublime_plugin
import threading

from copy import deepcopy

import time
import hashlib
import random

from urllib import request
from urllib.parse import urlencode
import gzip
import json
import re


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "200",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",

    "Origin": "http://fanyi.youdao.com",
    "Pragma": "no-cache",
    "Referer": "http://fanyi.youdao.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}


class TrsInfo(object):
    word = ""
    trans = ""

class Youdao(object):

    def __init__(self):
        self._trs_info = TrsInfo()

    def _init_trs(self):
        self._trs_info.word = ""
        self._trs_info.trans = "没有找到相关的汉英互译结果。"


    def auto_translate(self, words):
        self._init_trs()
        self._trs_info.word = words
        t = int(time.time()*1000)
        cookie = "OUTFOX_SEARCH_USER_ID=-2085605978@10.169.0.84; JSESSIONID=aaafDxWkSEzqf-N642MAw; OUTFOX_SEARCH_USER_ID_NCOO=2059228259.4870148; ___rl__test__cookies={update_time}".format(update_time=t-150)



        headers['Cookie'] = cookie
        words = words.replace("_", " ")
        sublime.status_message("selector :" + words)
        md5 = hashlib.md5()
        
        hs = ("fanyideskweb%s%s6x(ZHw]mwzX#u0V7@yfwK" %(words,t)).encode()
        md5.update(hs)
        sign = md5.hexdigest()
 
        url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


        data = {
            "i": words,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": t,
            "sign": sign,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTIME",
            "typoResult": "false",
        }

        data = urlencode(data).encode('utf-8')
        req = request.Request(url,data=data,headers=headers,method="POST")
        try:
            rep = request.urlopen(req,timeout=10)
            t = gzip.decompress( rep.read()).decode()
            t = json.loads(t)
            try: 
                trans = t['smartResult']['entries']
                trans = '<br>'.join([re.sub(r'\s','',tran) for tran in trans if re.sub(r'\s','',tran) != ''])
            except:
                trans = t['translateResult'][0][0]['tgt']
            
            self._trs_info.trans = trans
        except Exception as e:
            sublime.status_message(e)
            pass
            
        return self._trs_info



youdao = Youdao()
global_thread_flag = 1

class ThreadRun(threading.Thread):
    '''class docs'''
    def __init__(self,fetch_func, render_func, args=[], render_args=[], thread_flag=0):
        '''init docs'''
        super(ThreadRun, self).__init__()
        self.setDaemon(True)
        self.fetch_func = fetch_func
        self.render_func = render_func
        self.args = args
        self.render_args = render_args
        self.thread_flag = thread_flag

    def run(self):
        if self.args:
            result = self.fetch_func(*self.args)
        else:    
            result = self.fetch_func()
         
        if self.thread_flag != global_thread_flag:
            return

        if self.render_args:    
            self.render_func(result, *self.render_args)
        else:    
            self.render_func(result)



class AutoTranslateCommand(sublime_plugin.WindowCommand):

    @property
    def current_word(self):
        view = self.window.active_view()
        current_region = view.sel()[0]
        if current_region.a != current_region.b:
            return view.substr(current_region)
        word = view.word(current_region)
        return view.substr(word)

    # encode
    def run(self):
        global global_thread_flag
        global_thread_flag += 1
        flag = deepcopy(global_thread_flag)
        ThreadRun(youdao.auto_translate, self.render_popup, [self.current_word], thread_flag=flag).start()


    def render_popup(self, trs_info):
        html = """<span class="keyword">{t.word}</span><br><span class="string quoted">{t.trans}</span>""".format(t=trs_info)

        sublime.View.show_popup(self.window.active_view(), html,on_hide=False)       
