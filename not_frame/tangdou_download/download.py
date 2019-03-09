from urllib import request


import requests


url = 'http://aqiniu.tangdou.com/1B9FB6332E193E6B9C33DC5901307461-20.mp4'
url = 'http://acc.tangdou.com/201811/529B2A452575E50608012EE1D95024FA-20.mp4?sign=e629e0c019f725383ad51d0869b1629e&stTime=1543059578'

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
req = request.Request(url,headers=headers)
rep = request.urlopen(req)
size = int(rep.headers['Content-Length'])
cur_size = 0
chunk_size = 1024 * 1000
with open('c://Users/zero/Desktop/t.mp4','wb') as f:
	while True:
		content = rep.read(chunk_size)
		read_size = len(content)

		if read_size == 0:
			break
		cur_size += read_size
		f.write(content)
		f.flush()
		print('\r%0.2f%%' %(cur_size / size * 100),end='')


