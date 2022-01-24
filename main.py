#!/usr/bin/env python
# -*- coding: UTF-8 -*-



import time, sys 
import pyautogui

a=0
while a <= sys.argv[2]:
    time.sleep(sys.argv[1])
    pyautogui.click()

