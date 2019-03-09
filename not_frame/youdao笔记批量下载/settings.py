HEADERS = {
	# 'Referer': 'https://note.youdao.com/share/?token=A4EB9037044F4694B41708140F5A9FED&gid=10042410',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

TEMPLATE_URL = 'https://note.youdao.com/yws/api/group/{gid}/file/{file_id}?method=download&inline=true&version=1&shareToken={share_token}'