# --- CONFIGURATION ---
# Edit these values to match your hardware setup

RS_PIN = 26
RW_PIN = 27
E_PIN = 19
DB0_PIN = 21
DB1_PIN = 20
DB2_PIN = 16
DB3_PIN = 12
DB4_PIN = 13
DB5_PIN = 6
DB6_PIN = 5
DB7_PIN = 11

# Set to True to use the real sensor, False to use mock data
USE_REAL_SENSOR = False

# --- Sensor Calibration ---
# To calibrate:
# 1. Test the sensor in completely dry soil and note the raw_value (this is your DRY_VALUE).
# 2. Test the sensor in water and note the raw_value (this is your WET_VALUE).
DRY_VALUE = 33000
WET_VALUE = 13000
