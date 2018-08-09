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

# Take a picture.
imageStream = Camera().capture()

# Detect characters in image.
characters = Ocr().parse(imageStream)

if characters is not None:
    # Convert characters to time in seconds.
    seconds =  TimeConverter().toSeconds(characters)

    if seconds is not None:
        print("Seconds: " + str(seconds))

        # Push time to Laundry service.
        pushed = laundryService.push(seconds)
        if pushed:
            print("Time successfully pushed to Laundry Service.")
        else:
            print("Failed to push time to Laundry Service.")
