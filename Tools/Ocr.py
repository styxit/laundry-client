from subprocess import check_output

class Ocr:

    def parse(self, imageStream):
        print("Detect text in image")

        return check_output(["ssocr", "-d", "-1", "-t", "65", "make_mono", "invert", "-"], stdin=imageStream).decode("utf-8").strip()
