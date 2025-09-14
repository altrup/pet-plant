import config
from lib.CFAH1602A import CFAH1602A

# Global hardware objects
global cfah1602a
cfah1602a = None

def initialize_hardware():
	global cfah1602a
	cfah1602a = CFAH1602A(
		config.RS_PIN,
		config.RW_PIN,
		config.E_PIN,
		config.DB0_PIN,
		config.DB1_PIN,
		config.DB2_PIN,
		config.DB3_PIN,
		config.DB4_PIN,
		config.DB5_PIN,
		config.DB6_PIN,
		config.DB7_PIN
	)

def get_moisture_percentage():
	pass

def set_led_state(state: bool):
	pass