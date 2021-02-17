# import pyautogui
import pytesseract
from PIL import Image
from selenium import webdriver


# needed for macos to grab both screens
import pyscreenshot
import os
import re
import time

def take_screenshot():
    f = os.path.join('img', 'scr.png')
    # my_screenshot = pyautogui.screenshot()
    my_screenshot = pyscreenshot.grab()
    (left, upper, right, lower) = (0, 0, int(my_screenshot.width / 2), my_screenshot.height)
    # print('Dimensions = ', left, upper, right, lower)
    my_screenshot_crop = my_screenshot.crop((left, upper, right, lower))
    # my_screenshot_crop.save(f)
    print('Finished')
    # return f
    return my_screenshot_crop


def ocr(f):
    config = ("-l eng --oem 1 --psm 11")
    # config = ("-l eng --oem 1 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    if isinstance(f, str):
        im = Image.open(f)
    else:
        im = f

    t = pytesseract.image_to_string(im, config=config)
    return t


def replace_common_mistakes(s):
    MISTAKES = [('|','I')]
    for m in MISTAKES:
        s = s.replace(m[0], m[1])
    return s


class mainloop:
    interval = 5

    def __init__(self):
        self.interval = 5
        self.driver = webdriver.Chrome()
        self.driver.get('https://play.aidungeon.io/main/play?publicId=56a97c53-a172-4bab-8c62-c9335d4f333c')

    def set_interval(self, interval):
        self.interval = interval

    def start(self):
        print(f'time =', time.strftime('%H:%M:%S'))
        self.execute()
        self.call_again(self.interval)

    def call_again(self, time_in_seconds):
        time.sleep(time_in_seconds)
        self.start()

    def execute(self):
        t = ocr(take_screenshot())
        matches = re.findall(r'(?<=\% )(.*)(?= \%)', t)
        matches = [replace_common_mistakes(x.strip()) for x in matches]
        print('matches =', matches)








if __name__ == '__main__':
    m = mainloop()
    m.start()
    # t = ocr(take_screenshot())
    # matches = re.findall(r'(?<=\% )(.*)(?= \%)', t)
    # matches = [x.strip() for x in matches]
    # print('matches =', matches)