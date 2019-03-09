import telnetlib
import time
import re

items = [0, 0]

# 每次读取等待时间
WAIT_REC_TIME = 2
# 轮询时间
CYCLE_TIME = 5

# 爬虫是 暂停状态
is_pause = False

# 设置暂停和接触暂停界限
PAUSE_COUNT = 10000
UNPAUSE_COUNT = 1000

host = '192.168.0.51'
port = 6023
timeout = 10
info_commend = 'prefs() \r\n'.encode('utf-8')

def get_item_count(item_search, key):
	if item_search:
		return int(item_search.groupdict().get(key, 0))
	else:
		return 0


with telnetlib.Telnet(host=host, port=port, timeout=timeout) as tn:
	# execute commend
	tn.set_debuglevel(0)

	while True:
		
		tn.write(info_commend)

		time.sleep(WAIT_REC_TIME)
		temp = tn.read_very_eager()
		info = temp.decode('utf-8').strip()

		s = re.search(r'Jianshuv2Item\s+(?P<jsitem>\d+)',info,re.S)
		items[0] = get_item_count(s, 'jsitem')

		s = re.search(r'SpecialItem\s+(?P<scitem>\d+)',info,re.S)
		items[1] = get_item_count(s, 'scitem')

		count = sum(items)
		print('\ritem_count:{:>8}'.format(count), end='')
		if count > PAUSE_COUNT and not is_pause:
			is_pause = True
			tn.write(b'engine.pause()\r\n')
			print('\nstatus: pause')
		elif count < UNPAUSE_COUNT:
			if is_pause:
				print('\nstatus: unpause')
			is_pause = False
			tn.write(b'engine.unpause()\r\n')
			

		time.sleep(CYCLE_TIME)


