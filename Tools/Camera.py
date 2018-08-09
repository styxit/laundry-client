from subprocess import Popen, PIPE

from Tools.ArgumentConfigLoader import ArgumentConfigLoader

class Camera:
    command = ["raspistill", "--output", "-"]

    def capture(self):
        # Load the camera config.
        config = ArgumentConfigLoader('camera').list()

        print("Taking a picture.")
        proc = Popen(
            self.command + config,
            stdout=PIPE
        )
        print("Finished taking a picture")

        # Return the image stream.
        return proc.stdout
