#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import time
import sys
import pyautogui

time.sleep(10)
_time = int(sys.argv[1])
_num = int(sys.argv[2])

print("开始游戏")
start_time = time.time()
a = 0
while a < int(_num):
    b = 0
    a += 1
    pyautogui.click(770, 723)
    while b <= _time/3:
        time.sleep(3)
        b += 1
        c = "已经刷了 {} s".format(time.time()-start_time)
        print(c, end='')
        print('\b' * len(c) * 2, end='', flush=True)

    pyautogui.click(770, 723)
    
    print("\n已经刷完第 {} 次".format(a))
    
