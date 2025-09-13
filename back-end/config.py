# --- CONFIGURATION ---
# Edit these values to match your hardware setup

import board
import adafruit_mcp3xxx.mcp3008 as MCP

# Set to True to use the real sensor, False to use mock data
USE_REAL_SENSOR = True

# GPIO Pins for MCP3008 ADC
SPI_CLOCK_PIN = board.SCK
SPI_MISO_PIN = board.MISO
SPI_MOSI_PIN = board.MOSI
SPI_CS_PIN = board.D5

# ADC Channel for the soil moisture sensor
ADC_CHANNEL = MCP.P0

# GPIO Pin for the LED indicator
LED_PIN = board.D18

# --- Sensor Calibration ---
# To calibrate:
# 1. Test the sensor in completely dry soil and note the raw_value (this is your DRY_VALUE).
# 2. Test the sensor in water and note the raw_value (this is your WET_VALUE).
DRY_VALUE = 33000
WET_VALUE = 13000
