# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:23:45 2018

@author: gregoryvladimir.TRN
"""

import win32api
from win32api import GetSystemMetrics
import time
import numpy as np

state_left = win32api.GetKeyState(0x01) # Left button

SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)

def move_mouse(x, y):
    win32api.SetCursorPos((x, y))
    

    
while(win32api.GetKeyState(0x01) == state_left):
    
    time.sleep(2)
    #move_mouse(10, 10)
    #move_mouse(20, 20)
    
    
    
    x = np.random.randint(0, high=SCREEN_WIDTH)
    y = np.random.randint(0, high=SCREEN_HEIGHT)
    
    move_mouse(x, y)
    
   
    
    
    
    
    