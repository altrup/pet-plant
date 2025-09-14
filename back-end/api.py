from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import hardware
import config

router = APIRouter()

# Global variable to store the target moisture level
target_moisture_level = 50  # Default value

# Mock data for moisture levels
mock_moisture_data = [
    {"name": "6 hours ago", "level": 45},
    {"name": "5 hours ago", "level": 50},
    {"name": "4 hours ago", "level": 55},
    {"name": "3 hours ago", "level": 60},
    {"name": "2 hours ago", "level": 58},
    {"name": "1 hour ago", "level": 55},
    {"name": "Now", "level": 52},
]

class Config(BaseModel):
    targetMoisture: int

@router.get("/moisture")
def get_moisture_levels():
    """
    Returns moisture levels and controls the LED based on the target level.
    """
    global target_moisture_level

    if config.USE_REAL_SENSOR:
        try:
            percentage = hardware.get_moisture_percentage()
            
            print(f"Moisture: {percentage:.2f}%, Target: {target_moisture_level}%")

            # Control the LED
            if percentage < target_moisture_level:
                hardware.set_led_state(True)  # Turn LED ON (soil is too dry)
                print("LED ON - Soil is dry")
            else:
                hardware.set_led_state(False)  # Turn LED OFF (soil is moist enough)

            return [{"name": "Now", "level": round(percentage)}]
        except Exception as e:
            print(f"Error reading from sensor: {e}")
            return mock_moisture_data
    else:
        return mock_moisture_data

@router.post("/config")
def set_target_moisture(config_data: Config):
    """
    Sets the target moisture level.
    """
    global target_moisture_level
    if not (0 <= config_data.targetMoisture <= 100):
        raise HTTPException(status_code=400, detail="Target moisture must be between 0 and 100.")
    
    target_moisture_level = config_data.targetMoisture
    print(f"Target moisture set to {target_moisture_level}%")
    return {"success": True, "message": f"Target moisture set to {target_moisture_level}"}

@router.get("/")
def read_root():
    return {"Hello": "World"}
