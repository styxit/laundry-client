from dotenv import load_dotenv, find_dotenv
from os import environ
from Tools.LaundryService import LaundryService


# Load configuration from .env file.
load_dotenv(find_dotenv())

# Initiate Laundry Service.
laundryService = LaundryService(
    host=environ.get("LAUNDRY_ADMIN_DOMAIN"),
    token=environ.get("LAUNDRY_ADMIN_MACHINE_TOKEN"),
    machineId=environ.get("LAUNDRY_ADMIN_MACHINE_ID")
)

# TODO: Take a picture.
image = "IMAGE STREAM showing 2:34"

# TODO: Detect characters in image.
characters = "2134"

# TODO: Convert characters to time in seconds.
seconds = 9240

# Push time to Laundry service.
pushed = laundryService.push(seconds)

if pushed:
    print("Time successfully pushed to Laundry Service.")
else:
    print("Failed to push time to Laundry Service.")

