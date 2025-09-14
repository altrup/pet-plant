# Logic for communicating with LCD (CFAH1602A)
from dataclasses import dataclass
from time import sleep
from gpiozero import DigitalInputDevice, DigitalOutputDevice

class CFAH1602ADriver:
	RS_PIN: int
	RW_PIN: int
	E_PIN: int
	DB0_PIN: int
	DB1_PIN: int
	DB2_PIN: int
	DB3_PIN: int
	DB4_PIN: int
	DB5_PIN: int
	DB6_PIN: int
	DB7_PIN: int

	def __init__(self, rs_pin: int, rw_pin: int, e_pin: int, db0_pin: int, db1_pin: int, db2_pin: int, db3_pin: int, db4_pin: int, db5_pin: int, db6_pin: int, db7_pin: int):
		self.RS_PIN = rs_pin
		self.RW_PIN = rw_pin
		self.E_PIN = e_pin
		self.DB0_PIN = db0_pin
		self.DB1_PIN = db1_pin
		self.DB2_PIN = db2_pin
		self.DB3_PIN = db3_pin
		self.DB4_PIN = db4_pin
		self.DB5_PIN = db5_pin
		self.DB6_PIN = db6_pin
		self.DB7_PIN = db7_pin

	@dataclass
	class WriteCommand:
		RS_PIN_VALUE: int
		RW_PIN_VALUE: int
		DB7_PIN_VALUE: int
		DB6_PIN_VALUE: int
		DB5_PIN_VALUE: int
		DB4_PIN_VALUE: int
		DB3_PIN_VALUE: int
		DB2_PIN_VALUE: int
		DB1_PIN_VALUE: int
		DB0_PIN_VALUE: int
	
	@dataclass
	class ReadCommand:
		RS_PIN_VALUE: int
		RW_PIN_VALUE: int
	
	@dataclass
	class ReadCommandResponse:
		DB7_PIN_VALUE: int
		DB6_PIN_VALUE: int
		DB5_PIN_VALUE: int
		DB4_PIN_VALUE: int
		DB3_PIN_VALUE: int
		DB2_PIN_VALUE: int
		DB1_PIN_VALUE: int
		DB0_PIN_VALUE: int

	# NOTE: all pins default to output pins
	def send_command(self, command: WriteCommand):
		RS_PIN_DEVICE = DigitalOutputDevice(self.RS_PIN)
		RW_PIN_DEVICE = DigitalOutputDevice(self.RW_PIN)
		E_PIN_DEVICE = DigitalOutputDevice(self.E_PIN)
		DB0_PIN_DEVICE = DigitalOutputDevice(self.DB0_PIN)
		DB1_PIN_DEVICE = DigitalOutputDevice(self.DB1_PIN)
		DB2_PIN_DEVICE = DigitalOutputDevice(self.DB2_PIN)
		DB3_PIN_DEVICE = DigitalOutputDevice(self.DB3_PIN)
		DB4_PIN_DEVICE = DigitalOutputDevice(self.DB4_PIN)
		DB5_PIN_DEVICE = DigitalOutputDevice(self.DB5_PIN)
		DB6_PIN_DEVICE = DigitalOutputDevice(self.DB6_PIN)
		DB7_PIN_DEVICE = DigitalOutputDevice(self.DB7_PIN)

		E_PIN_DEVICE.off()

		RS_PIN_DEVICE.value = command.RS_PIN_VALUE
		RW_PIN_DEVICE.value = command.RW_PIN_VALUE
		DB0_PIN_DEVICE.value = command.DB0_PIN_VALUE
		DB1_PIN_DEVICE.value = command.DB1_PIN_VALUE
		DB2_PIN_DEVICE.value = command.DB2_PIN_VALUE
		DB3_PIN_DEVICE.value = command.DB3_PIN_VALUE
		DB4_PIN_DEVICE.value = command.DB4_PIN_VALUE
		DB5_PIN_DEVICE.value = command.DB5_PIN_VALUE
		DB6_PIN_DEVICE.value = command.DB6_PIN_VALUE
		DB7_PIN_DEVICE.value = command.DB7_PIN_VALUE

		E_PIN_DEVICE.on()

		sleep(0.002) # Longest execution time is 1.53ms

		E_PIN_DEVICE.off()

		RS_PIN_DEVICE.close()
		RW_PIN_DEVICE.close()
		E_PIN_DEVICE.close()
		DB0_PIN_DEVICE.close()
		DB1_PIN_DEVICE.close()
		DB2_PIN_DEVICE.close()
		DB3_PIN_DEVICE.close()
		DB4_PIN_DEVICE.close()
		DB5_PIN_DEVICE.close()
		DB6_PIN_DEVICE.close()
		DB7_PIN_DEVICE.close()
	
	def clear_display(self):
		self.send_command(self.WriteCommand(
			RS_PIN_VALUE=0,
			RW_PIN_VALUE=0,
			DB7_PIN_VALUE=0,
			DB6_PIN_VALUE=0,
			DB5_PIN_VALUE=0,
			DB4_PIN_VALUE=0,
			DB3_PIN_VALUE=0,
			DB2_PIN_VALUE=0,
			DB1_PIN_VALUE=0,
			DB0_PIN_VALUE=1
		))
	
	def return_home(self):
		self.send_command(self.WriteCommand(
			RS_PIN_VALUE=0,
			RW_PIN_VALUE=0,
			DB7_PIN_VALUE=0,
			DB6_PIN_VALUE=0,
			DB5_PIN_VALUE=0,
			DB4_PIN_VALUE=0,
			DB3_PIN_VALUE=0,
			DB2_PIN_VALUE=0,
			DB1_PIN_VALUE=1,
			DB0_PIN_VALUE=0
		))
	
	def entry_mode_set(self, increment: bool, shift: bool):
		self.send_command(self.WriteCommand(
			RS_PIN_VALUE=0,
			RW_PIN_VALUE=0,
			DB7_PIN_VALUE=0,
			DB6_PIN_VALUE=0,
			DB5_PIN_VALUE=0,
			DB4_PIN_VALUE=0,
			DB3_PIN_VALUE=0,
			DB2_PIN_VALUE=1,
			DB1_PIN_VALUE=int(increment),
			DB0_PIN_VALUE=int(shift)
		))
	
	def display_on_off_control(self, display_on: bool, cursor_on: bool, blink_on: bool):
		self.send_command(self.WriteCommand(
			RS_PIN_VALUE=0,
			RW_PIN_VALUE=0,
			DB7_PIN_VALUE=0,
			DB6_PIN_VALUE=0,
			DB5_PIN_VALUE=0,
			DB4_PIN_VALUE=1,
			DB3_PIN_VALUE=1,
			DB2_PIN_VALUE=int(display_on),
			DB1_PIN_VALUE=int(cursor_on),
			DB0_PIN_VALUE=int(blink_on)
		))
	
	def cursor_or_display_shift(self, shift_display: bool, shift_right: bool):
		self.send_command(self.WriteCommand(
			RS_PIN_VALUE=0,
			RW_PIN_VALUE=0,
			DB7_PIN_VALUE=0,
			DB6_PIN_VALUE=0,
			DB5_PIN_VALUE=0,
			DB4_PIN_VALUE=1,
			DB3_PIN_VALUE=int(shift_display),
			DB2_PIN_VALUE=int(shift_right),
			DB1_PIN_VALUE=0,
			DB0_PIN_VALUE=0
		))
	
	def function_set(self, data_length_8bit: bool, two_line: bool, font_5x11: bool):
		self.send_command(self.WriteCommand(
			RS_PIN_VALUE=0,
			RW_PIN_VALUE=0,
			DB7_PIN_VALUE=0,
			DB6_PIN_VALUE=0,
			DB5_PIN_VALUE=1,
			DB4_PIN_VALUE=int(data_length_8bit),
			DB3_PIN_VALUE=int(two_line),
			DB2_PIN_VALUE=int(font_5x11),
			DB1_PIN_VALUE=0,
			DB0_PIN_VALUE=0
		))
	
	def set_cgram_address(self, address: int):
		if address < 0 or address > 63:
			raise ValueError("CGRAM address must be between 0 and 63")
		
		bit_values = [(address >> i) & 1 for i in range(6)][::-1]
		
		self.send_command(self.WriteCommand(
			RS_PIN_VALUE=0,
			RW_PIN_VALUE=0,
			DB7_PIN_VALUE=0,
			DB6_PIN_VALUE=1,
			DB5_PIN_VALUE=bit_values[0],
			DB4_PIN_VALUE=bit_values[1],
			DB3_PIN_VALUE=bit_values[2],
			DB2_PIN_VALUE=bit_values[3],
			DB1_PIN_VALUE=bit_values[4],
			DB0_PIN_VALUE=bit_values[5]
		))
	
	def set_ddram_address(self, address: int):
		if address < 0 or address > 127:
			raise ValueError("DDRAM address must be between 0 and 127")
		
		bit_values = [(address >> i) & 1 for i in range(7)][::-1]
		
		self.send_command(self.WriteCommand(
			RS_PIN_VALUE=0,
			RW_PIN_VALUE=0,
			DB7_PIN_VALUE=1,
			DB6_PIN_VALUE=bit_values[0],
			DB5_PIN_VALUE=bit_values[1],
			DB4_PIN_VALUE=bit_values[2],
			DB3_PIN_VALUE=bit_values[3],
			DB2_PIN_VALUE=bit_values[4],
			DB1_PIN_VALUE=bit_values[5],
			DB0_PIN_VALUE=bit_values[6]
		))
	
	def write_data_to_ram(self, data: int):
		if data < 0 or data > 255:
			raise ValueError("Data must be between 0 and 255")
		
		bit_values = [(data >> i) & 1 for i in range(8)][::-1]
		
		self.send_command(self.WriteCommand(
			RS_PIN_VALUE=1,
			RW_PIN_VALUE=0,
			DB7_PIN_VALUE=bit_values[0],
			DB6_PIN_VALUE=bit_values[1],
			DB5_PIN_VALUE=bit_values[2],
			DB4_PIN_VALUE=bit_values[3],
			DB3_PIN_VALUE=bit_values[4],
			DB2_PIN_VALUE=bit_values[5],
			DB1_PIN_VALUE=bit_values[6],
			DB0_PIN_VALUE=bit_values[7]
		))
	
	def read_data_from_ram(self):
		RS_PIN_DEVICE = DigitalOutputDevice(self.RS_PIN)
		RW_PIN_DEVICE = DigitalOutputDevice(self.RW_PIN)
		E_PIN_DEVICE = DigitalOutputDevice(self.E_PIN)
		DB0_PIN_DEVICE = DigitalInputDevice(self.DB0_PIN)
		DB1_PIN_DEVICE = DigitalInputDevice(self.DB1_PIN)
		DB2_PIN_DEVICE = DigitalInputDevice(self.DB2_PIN)
		DB3_PIN_DEVICE = DigitalInputDevice(self.DB3_PIN)
		DB4_PIN_DEVICE = DigitalInputDevice(self.DB4_PIN)
		DB5_PIN_DEVICE = DigitalInputDevice(self.DB5_PIN)
		DB6_PIN_DEVICE = DigitalInputDevice(self.DB6_PIN)
		DB7_PIN_DEVICE = DigitalInputDevice(self.DB7_PIN)

		E_PIN_DEVICE.off()

		RS_PIN_DEVICE.value = 1
		RW_PIN_DEVICE.value = 0

		E_PIN_DEVICE.on()

		sleep(0.002) # Longest execution time is 1.53ms

		response = self.ReadCommandResponse(
			DB7_PIN_VALUE=DB7_PIN_DEVICE.value,
			DB6_PIN_VALUE=DB6_PIN_DEVICE.value,
			DB5_PIN_VALUE=DB5_PIN_DEVICE.value,
			DB4_PIN_VALUE=DB4_PIN_DEVICE.value,
			DB3_PIN_VALUE=DB3_PIN_DEVICE.value,
			DB2_PIN_VALUE=DB2_PIN_DEVICE.value,
			DB1_PIN_VALUE=DB1_PIN_DEVICE.value,
			DB0_PIN_VALUE=DB0_PIN_DEVICE.value
		)

		RS_PIN_DEVICE.close()
		RW_PIN_DEVICE.close()
		E_PIN_DEVICE.close()
		DB0_PIN_DEVICE.close()
		DB1_PIN_DEVICE.close()
		DB2_PIN_DEVICE.close()
		DB3_PIN_DEVICE.close()
		DB4_PIN_DEVICE.close()
		DB5_PIN_DEVICE.close()
		DB6_PIN_DEVICE.close()
		DB7_PIN_DEVICE.close()

		return response

	def read_busy_flag_and_address(self):
		RS_PIN_DEVICE = DigitalOutputDevice(self.RS_PIN)
		RW_PIN_DEVICE = DigitalOutputDevice(self.RW_PIN)
		E_PIN_DEVICE = DigitalOutputDevice(self.E_PIN)
		DB0_PIN_DEVICE = DigitalInputDevice(self.DB0_PIN)
		DB1_PIN_DEVICE = DigitalInputDevice(self.DB1_PIN)
		DB2_PIN_DEVICE = DigitalInputDevice(self.DB2_PIN)
		DB3_PIN_DEVICE = DigitalInputDevice(self.DB3_PIN)
		DB4_PIN_DEVICE = DigitalInputDevice(self.DB4_PIN)
		DB5_PIN_DEVICE = DigitalInputDevice(self.DB5_PIN)
		DB6_PIN_DEVICE = DigitalInputDevice(self.DB6_PIN)
		DB7_PIN_DEVICE = DigitalInputDevice(self.DB7_PIN)

		E_PIN_DEVICE.off()

		RS_PIN_DEVICE.value = 1
		RW_PIN_DEVICE.value = 1
		
		sleep(0.002) # Longest execution time is 1.53ms

		busy_flag = DB7_PIN_DEVICE.value
		address = (
			(DB6_PIN_DEVICE.value << 6) |
			(DB5_PIN_DEVICE.value << 5) |
			(DB4_PIN_DEVICE.value << 4) |
			(DB3_PIN_DEVICE.value << 3) |
			(DB2_PIN_DEVICE.value << 2) |
			(DB1_PIN_DEVICE.value << 1) |
			DB0_PIN_DEVICE.value
		)

		E_PIN_DEVICE.on()

		RS_PIN_DEVICE.close()
		RW_PIN_DEVICE.close()
		E_PIN_DEVICE.close()
		DB0_PIN_DEVICE.close()
		DB1_PIN_DEVICE.close()
		DB2_PIN_DEVICE.close()
		DB3_PIN_DEVICE.close()
		DB4_PIN_DEVICE.close()
		DB5_PIN_DEVICE.close()
		DB6_PIN_DEVICE.close()
		DB7_PIN_DEVICE.close()

		return busy_flag, address