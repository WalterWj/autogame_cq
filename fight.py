#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from sqlite3 import connect
import time
import sys
import os
import pyautogui

time.sleep(10)

print("开始游戏")
start_time = time.time()

while True:
    find_img_path = os.path.join("img", "find.png")
    connect_img_path = os.path.join("img", "connect.png")

    find_locate = pyautogui.locateOnScreen(find_img_path)
    connect_locate = pyautogui.locateOnScreen(connect_img_path)

    if find_locate is not None:
        find_point = pyautogui.center(find_locate)
        pyautogui.click(find_point)
    elif connect_locate is not None:
        connect_point = pyautogui.center(connect_locate)
        pyautogui.click(connect_point)
    else:
        _time = "已经刷了 {} s".format(time.time()-start_time)
        print(_time, end='')
        print('\b' * len(_time) * 2, end='', flush=True)

    time.sleep(15)
