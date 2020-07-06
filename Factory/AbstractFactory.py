from abc import ABC, abstractmethod


class Computer(ABC):

	@abstractmethod
	def getRAM(self): pass

	@abstractmethod
	def getHDD(self): pass

	@abstractmethod
	def getCPU(self): pass

	def __repr__(self):
		return "RAM: {}\nHDD: {}\nCPU: {}\n".format(self.getRAM(), self.getHDD(), self.getCPU())


class PC(Computer):
	def __init__(self, ram, hdd, cpu):
		self.ram = ram
		self.hdd = hdd
		self.cpu = cpu

	def getRAM(self): return self.ram

	def getHDD(self): return self.hdd

	def getCPU(self): return self.cpu
	

class Server(Computer):
	def __init__(self, ram, hdd, cpu):
		self.ram = ram
		self.hdd = hdd
		self.cpu = cpu

	def getRAM(self): return self.ram

	def getHDD(self): return self.hdd

	def getCPU(self): return self.cpu


class ComputerAbstractFactory(ABC):

	@abstractmethod
	def create_computer(self): pass


class PCFactory(ComputerAbstractFactory):
	def __init__(self, ram, hdd, cpu):
		self.ram = ram
		self.hdd = hdd
		self.cpu = cpu

	def create_computer(self):
		return PC(self.ram, self.hdd, self.cpu)


class ServerFactory(ComputerAbstractFactory):
	def __init__(self, ram, hdd, cpu):
		self.ram = ram
		self.hdd = hdd
		self.cpu = cpu

	def create_computer(self):
		return Server(self.ram, self.hdd, self.cpu)


class ComputerFactory(object):

	@staticmethod
	def get_computer(factory):
		return factory.create_computer()



if __name__ == '__main__':
	pc = ComputerFactory.get_computer(PCFactory("2 GB","500 GB","2.4 GHz"))
	server = ComputerFactory.get_computer(ServerFactory("64 GB","2000 GB","3.8 GHz"))

	print(pc)
	print(server)