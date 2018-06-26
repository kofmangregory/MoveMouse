# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:23:45 2018

@author: gregoryvladimir.TRN
"""

import win32api

state_left = win32api.GetKeyState(0x01) # Left button

def move_mouse(x, y):
    win32api.SetCursorPos((x, y))
    
while(True):
    
    a = win32api.GetKeyState(0x01)
    
    move_mouse(10, 10)
    move_mouse(20, 20)
    
    if a != state_left:
        break
    
    
    
    
    