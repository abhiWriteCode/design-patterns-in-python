from abc import ABC, abstractmethod


class Computer(object):
	def __init__(self, cb):
		self.ram = cb.ram
		self.hdd = cb.hdd
		self.is_graphics_card_enabled = cb.is_graphics_card_enabled
		self.is_bluetooth_enabled = cb.is_bluetooth_enabled

	def getRAM(self): return self.ram
	
	def getHDD(self): return self.hdd

	def check_graphics_card_enabled(self): return self.is_graphics_card_enabled

	def check_bluetooth_enabled(self): return self.is_bluetooth_enabled

	def __repr__(self):
		return "RAM: {}\nHDD: {}\nGraphics Cards Enable: {}\nBluetooth Enable: {}\n".format(self.getRAM(), 
		                                                                                    self.getHDD(),
		                                                                                    self.check_graphics_card_enabled(),
		                                                                                    self.check_bluetooth_enabled())

	class ComputerBuilder:
		def __init__(self, ram=None, 
		             hdd=None, 
		             is_graphics_card_enabled=None, 
		             is_bluetooth_enabled=None):
			self.ram = ram
			self.hdd = hdd
			self.is_graphics_card_enabled = is_graphics_card_enabled
			self.is_bluetooth_enabled = is_bluetooth_enabled

		def set_ram(self, ram):
			self.ram = ram
			return self

		def set_hdd(self, hdd):
			self.hdd = hdd
			return self

		def set_graphics_card_enabled(self, is_graphics_card_enabled):
			self.is_graphics_card_enabled = is_graphics_card_enabled
			return self

		def set_bluetooth_enabled(self, is_bluetooth_enabled):
			self.is_bluetooth_enabled = is_bluetooth_enabled
			return self

		def build(self):
			return Computer(self)



if __name__ == '__main__':
	computer = (Computer.ComputerBuilder(hdd="1 TB")
	            .set_ram("8 GB")
	            .set_graphics_card_enabled(True)
	            .set_bluetooth_enabled(False)
	            .build())

	print(computer)