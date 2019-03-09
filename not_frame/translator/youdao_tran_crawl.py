import requests
import time
import hashlib
import random

md5 = hashlib.md5()
t = int(time.time()*1000)
words = "来无影去无踪"
hs = ("fanyideskweb%s%s6x(ZHw]mwzX#u0V7@yfwK" %(words,t)).encode()
md5.update(hs)
sign = md5.hexdigest()

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


# cookie = "OUTFOX_SEARCH_USER_ID_NCOO=148964555.05843297; _ga=GA1.2.1465151633.1532850898;OUTFOX_SEARCH_USER_ID=-1402717445@10.169.0.84; _ntes_nnid=4ae2cb3b2860ad2de61a3f9e1224ed36,1534222899940; SESSION_FROM_COOKIE=www.baidu.com; UM_distinctid=166a4cde89463d-00d4d909b80a9c-551e3f12-1fa400-166a4cde8954d5; P_INFO=wind13zero@163.com|1540363309|0|search|00&99|hun&1538722158&wydz_platform#hun&430100#10#0#0|187616&0||wind13zero@163.com; JSESSIONID=aaaZ4uzLaKxLYdJWo3KAw; JSESSIONID=abcI6m5Q5QXr-gfJx3KAw; DICT_LOGIN=8||{login_time}; DICT_FORCE=true; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; ___rl__test__cookies={update_time}" .format(login_time=t-random.randint(300,500),update_time=t-150)

cookie = "OUTFOX_SEARCH_USER_ID=-2085605978@10.169.0.84; JSESSIONID=aaafDxWkSEzqf-N642MAw; OUTFOX_SEARCH_USER_ID_NCOO=2059228259.4870148; ___rl__test__cookies={update_time}".format(update_time=t-150)


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "200",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": cookie,
    "Origin": "http://fanyi.youdao.com",
    "Pragma": "no-cache",
    "Referer": "http://fanyi.youdao.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

# from urllib import request
# from urllib.parse import urlencode
# import gzip
# import json
# import re
# data = urlencode(data).encode('utf-8')
# req = request.Request(url,data=data,headers=headers,method="POST")
# rep = request.urlopen(req)
# try:
#     content = rep.read()
#     t = gzip.decompress( content).decode()
#     t = json.loads(t)
#     print(t)
#     trans = t['smartResult']['entries']
#     # trans = '<br>'.join(map(lambda x:x.strip(),trans))
    
#     trans = '<br>'.join([tran.strip() for tran in trans if re.sub(r'\s','',tran) != ''])
#     print(trans)
# except:
#     print(content)



rep = requests.post(url,data=data,headers=headers,timeout=10)
# print(rep.request.headers)
# print(rep.json())
d = rep.json()
print(d)
try:
    d1 = d["smartResult"]["entries"]
    print("".join(d1))
except:
    d1 = d['translateResult'][0][0]['tgt']
    print(d1)
