import subprocess

from Tools.ArgumentConfigLoader import ArgumentConfigLoader

class Ocr:

    def parse(self, imageStream):
        print("Detecting text in image")

        # Load the ssocr config.
        config = ArgumentConfigLoader('ocr').list()

        # Construct command.
        # End with "-" to read image from stdin.
        command = ["ssocr"] + config + ["-"]

        try:
            characters = subprocess.check_output(
                command,
                stdin=imageStream
            ).decode("utf-8").strip()
        except subprocess.CalledProcessError as exception:
            print("OCR failed, exit code: " + str(exception.returncode))
            return None

        print("OCR detected: " + characters)
        return characters
