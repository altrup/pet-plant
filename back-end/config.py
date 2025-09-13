# --- CONFIGURATION ---
# Edit these values to match your hardware setup
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# Set to True to use the real sensor, False to use mock data
USE_REAL_SENSOR = False

# --- Sensor Calibration ---
# To calibrate:
# 1. Test the sensor in completely dry soil and note the raw_value (this is your DRY_VALUE).
# 2. Test the sensor in water and note the raw_value (this is your WET_VALUE).
DRY_VALUE = 33000
WET_VALUE = 13000
