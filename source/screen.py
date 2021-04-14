import time
import base64
import threading

from io import BytesIO
import pyscreenshot as ImageGrab


class Screen:
    '''[summary]
    '''

    def __init__(self):
        '''[summary]
        '''
        self.fps = 1
        self.screenbuf = ""
        self.screenfile = BytesIO()
        # threading.Thread(target=self.get_frames).start()

    def get_frames(self):
        '''[summary]
        '''
        while True:
            img = ImageGrab.grab(childprocess=False)
            self.screenfile = BytesIO()
            img.save(self.screenfile, quality=1, format="jpeg")
            img.close()
            self.screenbuf = base64.b64encode(self.screenfile.getvalue())
            time.sleep(1.0/self.fps)

    def gen(self):
        '''[summary]

        :return: [description]
        :rtype: [type]
        '''
        return self.screenbuf


screenlive = Screen()
