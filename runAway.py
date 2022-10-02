import time
import pyautogui
from datetime import datetime
from temtem.logTemtem import logThis
from temtem.lumaSearch import detectLuma
from temtem.notifyU import notify, notifyError
from temtem.scrnCoords import getCoordsOfScreen
from temtem.mouseANDkeyboard import mouseleft



runImgPath = 'C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/symbols/runAwayButton.png'

def runnn():
	if detectLuma():
		notify()
		time.sleep(86400)
	else:
		l, t, w, h = getCoordsOfScreen()
		t += 500
		loc = pyautogui.locateCenterOnScreen(runImgPath, confidence=0.8, region=(l, t, w, h))
		#print(loc)
		if loc is not None:
			time.sleep(0.15)
			x, y = loc
			mouseleft(x, y)
			#print("Pressed 1 time")
			time.sleep(0.5)
			mouseleft(x, y)
			#print("Pressed 2 times ")
			logThis(f'Bot ran away at {datetime.now()}')
			print(f'Bot ran away at {datetime.now()}', end=" ")
			return
		else:
			print("Error in locating RUN AWAY button ")
			#notifyError()
			time.sleep(86400)