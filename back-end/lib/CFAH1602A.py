# Higher level interface for the CFAH1602A LCD display driver
from time import sleep

from drivers.CFAH1602ADriver import CFAH1602ADriver

class CFAH1602A:
	driver: CFAH1602ADriver

	def __init__(self, rs_pin: int, rw_pin: int, e_pin: int, db0_pin: int, db1_pin: int, db2_pin: int, db3_pin: int, db4_pin: int, db5_pin: int, db6_pin: int, db7_pin: int):
		self.driver = CFAH1602ADriver(rs_pin, rw_pin, e_pin, db0_pin, db1_pin, db2_pin, db3_pin, db4_pin, db5_pin, db6_pin, db7_pin)

	def initialize(self):
		self.driver.function_set(data_length_8bit=True, two_line=True, font_5x11=False)
		sleep(0.005) # Wait for more than 4.1ms
		self.driver.function_set(data_length_8bit=True, two_line=True, font_5x11=False)
		sleep(0.00015) # Wait for more than 100us
		self.driver.function_set(data_length_8bit=True, two_line=True, font_5x11=False)
		# Now we can start actually setting data
		self.driver.function_set(data_length_8bit=True, two_line=True, font_5x11=False)
		self.driver.display_on_off_control(display_on=True, cursor_on=True, blink_on=True)
		self.driver.clear_display()
	
	def display_string(self, string: str, line: int):
		if line == 1:
			self.driver.set_ddram_address(0x00)
		elif line == 2:
			self.driver.set_ddram_address(0x40)
		else:
			raise ValueError("Line must be 1 or 2")
		
		for char in string:
			self.driver.write_data_to_ram(ord(char))