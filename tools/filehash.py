import hashlib
import os

class FileHash:
	def __init__(self,path,hash_type='sha256',chunk_size=1024*1024):
		self.path = path
		self.size = os.path.getsize(path)
		self.hash = getattr(hashlib,hash_type)()
		self.chunk_size = chunk_size

	def run(self):
		cur_size = 0
		with open(self.path,'rb') as f:
			while True:
				content = f.read(self.chunk_size)
				if content:
					self.hash.update(content)
					cur_size += len(content)
					print('\r 已完成: %.2f%%' %(cur_size*100/self.size),end='')
				else:
					print()
					break
		self.hexdigest = self.hash.hexdigest()

	def __repr__(self):
		if 'hexdigest' not in self.__dict__:
			self.run()
		return self.hexdigest

if __name__ == '__main__':
	file_path = r'C:\Users\zero\Desktop\python_传智播客_目录.md'
	fh = FileHash(file_path)
	print(fh)
