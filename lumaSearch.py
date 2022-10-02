import pyautogui
from temtem.scrnCoords import getCoordsOfScreen

starImagePath = "C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/symbols/star.png"

def detectLuma():
	l, t, w, h = getCoordsOfScreen()
	h -= 500
	loc = pyautogui.locateOnScreen(starImagePath, confidence=0.8, region=(l, t, w, h))
	#print(loc)
	if loc is not None:
		#print("111")
		return True
	else:
		#print("222")
		return False


