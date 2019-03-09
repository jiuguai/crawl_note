import requests
query = "one"
data = {
	"kw": query
}

headers = {
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
	"Cache-Control": "no-cache",
	"Connection": "keep-alive",
	"Content-Length": "6",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"Cookie": "BIDUPSID=1C527BE06A988E74355D16B99CC5ABCD; BAIDUID=C264D01F13E0630C3D2F2525229200BF:FG=1; PSTM=1540397688; PRY=1; BDUSS=VyRWVldGQtLUFuRnZ2RGxFeTBwMFRtZ1N0NVdsNURPeThLNjhiSlExb2FZZnBiQVFBQUFBJCQAAAAAAAAAAAEAAABGRMoad2luZDJ6ZXJvAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABrU0lsa1NJbbE; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6; H_PS_PSSID=1467_21095_20883_22158; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1540993094; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1540993094; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D",
	"Host": "fanyi.baidu.com",
	"Origin": "https://fanyi.baidu.com",
	"Pragma": "no-cache",
	"Referer": "https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest",
}

url = "https://fanyi.baidu.com/sug"
rep = requests.post(url,headers=headers,data=data)
print(rep.json())
