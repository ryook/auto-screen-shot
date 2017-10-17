import os
import time

from selenium import webdriver
from selenium.webdriver import Firefox


class ScreenShot:
    def __init__(self, url, name='screenshot', dir='./screenshots'):
        try:
            self.driver = webdriver.Chrome('./chromedriver')
        except:
            self.driver = Firefox()
        self.name = name
        self.dir = dir
        self.url = url
        if not os.path.isdir(dir):
            os.mkdir(dir)


    def get_page(self):
        self.driver.get(self.url)

    def get_screenshot(self):
        self.driver.refresh()
        time.sleep(5)
        timestamp = time.strftime('%H%M%S', time.localtime())
        img_path = '{dir}/{name}_{time}.jpg'.format(dir=self.dir, name=self.name, time=timestamp)
        self.driver.save_screenshot(img_path)

    def close_driver(self):
        self.driver.close()


if __name__ == '__main__':
    nikkei = ScreenShot('https://www.nikkei.com')
    nikkei.get_page()
    nikkei.get_screenshot()
    nikkei.close_driver()