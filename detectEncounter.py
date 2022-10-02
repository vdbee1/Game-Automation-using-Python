import timeit
import pyautogui
from temtem.scrnCoords import getCoordsOfScreen

temtemStatBarImagePath = 'C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/symbols/temtemStatBars.png'

def detectEncounter():
	l, t, w, h = getCoordsOfScreen()
	h -= 500
	loc = pyautogui.locateOnScreen(temtemStatBarImagePath, confidence=0.8, region=(l, t, w, h)) # region = (l,t,w,h)
	if loc is not None:
		return True
	else:
		return False
'''
start = timeit.timeit()
detectEncounter()
print(f"Time taken = {timeit.timeit() - start}")
'''