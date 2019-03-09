class IntField:
	_value = 0
	def __get__(self, instance, owner):
		print(instance)
		print(owner)
		return self._value

	def __set__(self, instance, value):
		print(instance)
		print(value)
		self._value = value

class Test:
	age = IntField()

item = Test()
item.age = 12
print(item.age)