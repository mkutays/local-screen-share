import threading
from io import BytesIO
import time
import base64
import pyscreenshot as ImageGrab


class Screen():
    def __init__(self):
        self.FPS = 1
        self.screenbuf = ""
        self.screenfile = BytesIO()
        threading.Thread(target=self.getframes).start()

    def __del__(self):
        self.screenfile.close()

    def getframes(self):
        while True:
            im = ImageGrab.grab(childprocess=False)
            self.screenfile = BytesIO()
            im.save(self.screenfile, quality=1, format="jpeg")
            im.close()
            self.screenbuf = base64.b64encode(self.screenfile.getvalue())
            time.sleep(1.0/self.FPS)

    def gen(self):
        return self.screenbuf


screenlive = Screen()
