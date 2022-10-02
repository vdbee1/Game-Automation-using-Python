import numpy as np
import cv2
from mss import mss
import time
import win32gui

def getCordsOfScreen():
    win = win32gui.FindWindow(None, 'Temtem')
    #print(win)
    rect = win32gui.GetWindowRect(win)
    #print(rect)
    return rect

# This defines the area on the screen.
def scrCapture():
    left, top, right, bottom = getCordsOfScreen()
    width = right - left
    height = bottom - top
    offsetL, offsetT = 10, 32
    offsetW, offsetH = 17, 39
    print(left,top,width,height)
    mon = {'top' : top + offsetT, 'left' : left + offsetL, 'width' : width - offsetW, 'height' : height - offsetH}
    sct = mss()
    previous_time = 0
    while True:
        sct.grab(mon)
        img = np.array(sct.grab(mon))
        cv2.imshow ('frame', img)
        if cv2.waitKey ( 1 ) & 0xff == ord( 'q' ) :
            cv2.destroyAllWindows()
        txt1 = 'fps: %.1f' % ( 1./( time.time() - previous_time ))
        previous_time = time.time()
        print(txt1)
        #return img

scrCapture()
