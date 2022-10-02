import time
import pyautogui
from random import uniform as u
from temtem.directkeys import PressKey,ReleaseKey,W,A,S,D

def up():
    PressKey(W)
    time.sleep(round(u(0.20,0.40),2))
    ReleaseKey(W)

def right():
    PressKey(D)
    time.sleep(round(u(0.20,0.40),2))
    ReleaseKey(D)

def left():
    PressKey(A)
    time.sleep(round(u(0.20,0.40),2))
    ReleaseKey(A)

def down():
    PressKey(S)
    time.sleep(round(u(0.20,0.40),2))
    ReleaseKey(S)

def mouseleft(x,y):
    pyautogui.click(x,y)
