from subprocess import Popen, PIPE

class Camera:
    def capture(self):
        print("Taking a picture.")
        proc = Popen(["raspistill", "-o", "-", "--width", "600", "--height", "500", "--rotation", "270"], stdout=PIPE)
        print("Finished taking a picture")

        # Return the image stream.
        return proc.stdout
