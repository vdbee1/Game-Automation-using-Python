import win32gui

def getCoordsOfScreen():
    win = win32gui.FindWindow(None, 'Temtem')
    #print(win)
    rect = win32gui.GetWindowRect(win)
    #print(rect)
    left, top, right, bottom = rect
    width = right - left
    height = bottom - top
    offsetL, offsetT = 10, 32
    offsetW, offsetH = 16, 39
    top += offsetT
    left += offsetL
    width -= offsetW
    height -= offsetH
    return (left, top, width, height)
