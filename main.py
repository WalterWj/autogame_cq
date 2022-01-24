#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import time
import sys
import os
import pyautogui

time.sleep(3)

_while = True
while _while:
    # 大成功区域 
    bait_img_path = os.path.join("..", "img", "bait.png")
    # 光标区域 列表: Box(left=1255, top=412, width=14, height=46)
    cursor_img_path = os.path.join("..", "img", "cursor.png")

    # 大成功区域位置
    list_box_bait = list(pyautogui.locateAllOnScreen(bait_img_path, grayscale=True))
    
    if len(list_box_bait) >= 1:
        bait_list0 = list_box_bait[0]
        # print("\n")
        print("bait 列表: {}".format(bait_list0))
        _num = 0
        while _while:   
            list_box_cursor = list(pyautogui.locateAllOnScreen(cursor_img_path, grayscale=True))
            if len(list_box_cursor) >= 1:
                curosor_list0 = list_box_cursor[0]
                print("游标：{}".format(curosor_list0))
                if bait_list0.left <= curosor_list0.left <= (bait_list0.left + bait_list0.width):
                    pyautogui.click(1604, 877)
                    # _while = False
                    print("1604, 877 点击转盘")
                    time.sleep(3)
                    break
                else:
                    pass
            else:
                break
            time.sleep(0.1)
            if _num <= 100:
                _num += 1
            else:
                break
    else:
        c = "轮空"
        print(c, end='')
        print('\b' * len(c) * 2, end='', flush=True)

        

    # _list = pyautogui.locateOnScreen(img_path)
    # print("列表: {}".format(_list))

    time.sleep(3)


# 1604, 877 点击转盘

