import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import config

# Global hardware objects
sensor_channel = None
led = None

def initialize_hardware():
    global sensor_channel, led
    if config.USE_REAL_SENSOR:
        try:
            # --- Initialize ADC for moisture sensor ---
            spi = busio.SPI(clock=config.SPI_CLOCK_PIN, MISO=config.SPI_MISO_PIN, MOSI=config.SPI_MOSI_PIN)
            cs = digitalio.DigitalInOut(config.SPI_CS_PIN)
            mcp = MCP.MCP3008(spi, cs)
            sensor_channel = AnalogIn(mcp, config.ADC_CHANNEL)
            print("Successfully initialized soil moisture sensor.")

            # --- Initialize LED ---
            led = digitalio.DigitalInOut(config.LED_PIN)
            led.direction = digitalio.Direction.OUTPUT
            print(f"Successfully initialized LED on pin {config.LED_PIN}.")
            return True

        except Exception as e:
            print(f"Could not initialize hardware: {e}")
            print("Falling back to mock data and disabling hardware output.")
            return False
    return False

def get_moisture_percentage():
    if sensor_channel:
        raw_value = sensor_channel.value
        
        # Ensure WET_VALUE is not equal to DRY_VALUE to avoid division by zero
        if config.WET_VALUE == config.DRY_VALUE:
            return 0

        # Calculate the percentage
        percentage = ((raw_value - config.DRY_VALUE) / (config.WET_VALUE - config.DRY_VALUE)) * 100
        
        # Constrain the percentage to 0-100
        percentage = max(0, min(100, percentage))
        
        print(f"Raw ADC: {raw_value}, Moisture: {percentage:.2f}%")
        return percentage
    return 0

def control_led(is_on):
    if led:
        led.value = is_on
