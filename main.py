import os
import random
from turtledemo.penrose import start
from selenium import webdriver
from time import perf_counter
import time

def main():

    # Т. к. веб-страница загружает картинки динамически, то придётся использовать selenium для обработки
    browser = webdriver.Firefox() # С FireFox легче работает, потому что сильно гибок в настройках
    browser.get('https://thispersonnotexist.org')
    time.sleep(15)


if __name__ == '__main__':
    main()


