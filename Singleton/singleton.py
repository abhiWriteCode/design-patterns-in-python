class Singleton:
	__instance = None

	def __init__(self):
		if Singleton.__instance is not None:
			raise Exception("This class is a singleton! To get instance call Singleton.get_instance()")
		else:
			Singleton.__instance = self

	@staticmethod
	def get_instance():
		if Singleton.__instance is None:
			Singleton()
			
		return Singleton.__instance


s1 = Singleton.get_instance()
s2 = Singleton.get_instance()


print(s1 is s2)
print(id(s1))
print(id(s2))

#########################################################################

# class Singleton(object):
# 	__ONLY_INSTACE = False

# 	def __init__(self):
# 		if Singleton.__ONLY_INSTACE is True:
# 			raise Exception("This class is a singleton! To get instance call Singleton.get_instance()")
# 		Singleton.__ONLY_INSTACE = True

# 	@staticmethod
# 	def get_instance():
# 		return _InnerClass._instance


# class _InnerClass(object):
# 	_instance = Singleton()

# obj1 = Singleton.get_instance()
# obj2 = Singleton.get_instance()
# obj3 = Singleton.get_instance()


# print(id(obj1), id(obj2), id(obj3), sep='\n')
# print(type(obj1), type(obj2), type(obj3), sep='\n')