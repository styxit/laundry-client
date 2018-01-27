from dotenv import load_dotenv, find_dotenv
from os import environ

from Tools.Camera import Camera
from Tools.LaundryService import LaundryService
from Tools.Ocr import Ocr
from Tools.TimeConverter import TimeConverter

# Load configuration from .env file.
load_dotenv(find_dotenv())

# Initiate Laundry Service.
laundryService = LaundryService(
    host=environ.get("LAUNDRY_ADMIN_DOMAIN"),
    token=environ.get("LAUNDRY_ADMIN_MACHINE_TOKEN"),
    machineId=environ.get("LAUNDRY_ADMIN_MACHINE_ID")
)
# Initialize camera.
camera = Camera()
# Initialize OCR.
ocr = Ocr()
# Initialize time converter.
timeConverter = TimeConverter();

# Take a picture.
imageStream = camera.capture()

# Detect characters in image.
characters = ocr.parse(imageStream)
print("OCR detected: " + characters)

# Convert characters to time in seconds.
seconds = timeConverter.toSeconds(characters)
if (isinstance(seconds, int)):
    print("Seconds: " + str(seconds))

    # Push time to Laundry service.
    pushed = laundryService.push(seconds)
    if pushed:
        print("Time successfully pushed to Laundry Service.")
    else:
        print("Failed to push time to Laundry Service.")
