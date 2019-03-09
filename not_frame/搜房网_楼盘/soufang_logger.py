import logging


def getLogger():
	logger = logging.getLogger()
	

	# 创建一个handler，用于写入日志文件
	fh = logging.FileHandler('err.log',encoding='utf-8') 

	# 再创建一个handler，用于输出到控制台 
	ch = logging.StreamHandler() 

	f_formatter = logging.Formatter('%(asctime)s %(filename)s [%(lineno)s] - %(levelname)s :\n %(threadName)s: %(message)s')
	c_formatter = logging.Formatter('%(threadName)s - %(levelname)s: %(message)s')
	
	# logger.setLevel(logging.DEBUG)
	# ch.setLevel(logging.DEBUG)
	# fh.setLevel(logging.WARNING)

	fh.setFormatter(f_formatter) 
	ch.setFormatter(c_formatter) 
	logger.addHandler(fh) #logger对象可以添加多个fh和ch对象 
	logger.addHandler(ch) 
	return logger


# logger.debug('logger debug message') 
# logger.info('logger info message') 
# logger.warning('logger warning message') 
# logger.error('logger error message') 
# logger.critical('logger critical message')