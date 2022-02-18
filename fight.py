#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from sqlite3 import connect
import time
import random
import os
from tkinter.messagebox import NO
import pyautogui

time.sleep(3)

print("开始游戏")
start_time = time.time()

while True:
    shop_osPath = os.path.join("img","fight")
    files = os.listdir(shop_osPath)
    for file_name in files:
        if not os.path.isdir(file_name):
            imgs = os.path.join(shop_osPath, file_name)
            locate = pyautogui.locateOnScreen(imgs)
            if locate is not None:
                point = pyautogui.center(locate)
                pyautogui.click(point)
                print("file: {}".format(file_name))

    _time = "已经刷了 {} s".format(time.time()-start_time)
    print(_time, end='')
    print('\b' * len(_time) * 2, end='', flush=True)

    # time.sleep(random.randint(7, 15))
    time.sleep(random.randint(3, 6))
