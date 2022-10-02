import pyautogui
from time import sleep
from temtem.scrnCoords import getCoordsOfScreen
from temtem.mouseANDkeyboard import mouseleft

temCardsSlotCoords = (345, 25)
balmSlotCoords = (390, 25)
bagButtonCoords = (405, 564)
firstTemtemCoords = (580, 200)
secondTemtemCoords = (670, 370)
temCardImgPath = 'C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/symbols/temCard.png'
bagButtonImgPath = 'C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/symbols/bagButton.png'
temtemStatBarImgPath = 'C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/symbols/temtemStatBars.png'
releaseButtonImgPath = 'C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/symbols/releaseButton.png'
yesButtonImgPath = 'C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/symbols/yesButton.png'
temHealthBarImgPath = 'C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/symbols/temHealthBar.png'
acceptButtonImgPath = 'C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/symbols/acceptButton.png'

def catchemall():
	l, t, w, h = getCoordsOfScreen()
	#sleep(3)
	noOfTemtemOnScreen = pyautogui.locateAllOnScreen(temHealthBarImgPath, confidence=0.99, region=(l, t, w, h-500))
	noOfTemtemOnScreen = len(list(noOfTemtemOnScreen))
	print(noOfTemtemOnScreen)

	if noOfTemtemOnScreen == 1:
		flag1 = True
		while flag1:
			flag2 = True

			mouseleft(x=bagButtonCoords[0] + l, y=bagButtonCoords[1] + t)
			sleep(0.3)
			mouseleft(x=temCardsSlotCoords[0] + l, y=temCardsSlotCoords[1] + t)
			sleep(0.3)
			loc = pyautogui.locateCenterOnScreen(temCardImgPath, confidence=0.8, region=(l, t, w, h))
			mouseleft(x=loc[0], y=loc[1])

			sleep(0.4)

			mouseleft(x=bagButtonCoords[0] + l, y=bagButtonCoords[1] + t)
			sleep(0.3)
			mouseleft(x=temCardsSlotCoords[0] + l, y=temCardsSlotCoords[1] + t)
			sleep(0.3)
			mouseleft(x=loc[0], y=loc[1])

			while flag2:
				loc = pyautogui.locateCenterOnScreen(releaseButtonImgPath, confidence=0.8, region=(l, t, w, h))
				loc2 = pyautogui.locateCenterOnScreen(bagButtonImgPath, confidence=0.8, region=(l, t, w, h))
				if loc is not None:
					mouseleft(x=loc[0], y=loc[1])
					flag3 = True
					while flag3:
						loc = pyautogui.locateCenterOnScreen(yesButtonImgPath, confidence=0.8, region=(l, t, w, h))
						if loc is not None:
							mouseleft(x=loc[0], y=loc[1])
							sleep(1)
							mouseleft(x=loc[0], y=loc[1])
							flag3 = False
							flag2 = False
							flag1 = False
							return
				elif loc2 is not None:
					flag2 = False

	elif noOfTemtemOnScreen == 2:
		flag1 = True
		counter = 0
		while flag1:
			flag2 = True

			mouseleft(x=bagButtonCoords[0] + l, y=bagButtonCoords[1] + t)
			sleep(0.3)
			mouseleft(x=temCardsSlotCoords[0] + l, y=temCardsSlotCoords[1] + t)
			sleep(0.3)
			loc = pyautogui.locateCenterOnScreen(temCardImgPath, confidence=0.8, region=(l, t, w, h))
			mouseleft(x=loc[0], y=loc[1])
			sleep(0.75)
			mouseleft(x=firstTemtemCoords[0], y=firstTemtemCoords[1])

			sleep(0.5)

			mouseleft(x=bagButtonCoords[0] + l, y=bagButtonCoords[1] + t)
			sleep(0.3)
			mouseleft(x=temCardsSlotCoords[0] + l, y=temCardsSlotCoords[1] + t)
			sleep(0.3)
			mouseleft(x=loc[0], y=loc[1])
			sleep(0.75)
			mouseleft(x=firstTemtemCoords[0]+l, y=firstTemtemCoords[1]+t)

			while flag2 and counter < 2:
				loc = pyautogui.locateCenterOnScreen(releaseButtonImgPath, confidence=0.8, region=(l, t, w, h))
				loc2 = pyautogui.locateCenterOnScreen(bagButtonImgPath, confidence=0.8, region=(l, t, w, h))
				if loc is not None:
					mouseleft(x=loc[0], y=loc[1])
					flag3 = True
					while flag3:
						loc = pyautogui.locateCenterOnScreen(yesButtonImgPath, confidence=0.8, region=(l, t, w, h))
						if loc is not None:
							mouseleft(x=loc[0], y=loc[1])
							#flag4 = True
							#codePointA
							counter += 1
							if counter == 2:
								flag3 = False
								flag1 = False
								sleep(0.75)
								mouseleft(loc[0], loc[1])
								return
							flag3 = False

				elif loc2 is not None:
					flag2 = False

				else:
					pass

#catchemall()
# 3 boxes for 1 temtem, 5 for 2, release, yes, click anywhere

def temp():
	l, t, w, h = getCoordsOfScreen()
	h -= 500
	t = pyautogui.locateAllOnScreen(temHealthBarImgPath, confidence=0.99, region=(l, t, w, h))
	#print(len(list(t)))
	for i in t:
		print(i)

#temp()
'''
if loc is not None:
	mouseleft(x=loc[0], y=loc[1])
	flag3 = True
	while flag3:
		loc3 = pyautogui.locateCenterOnScreen(acceptButtonImgPath, confidence=0.8, region=(l, t, w, h))
		if loc3 is not None:
			mouseleft(loc3[0], loc3[1])
			sleep(0.5)
			flag3 = False
	counter += 1
	if counter < 2:
		flag2 = False
		flag1 = False
		return
else:
	print('Error in locating the yes button !!!')
elif loc2 is not None:
flag2 = False


#code A
while flag4:
	loc3 = pyautogui.locateCenterOnScreen(acceptButtonImgPath, confidence=0.8, region=(l, t, w, h))
	if loc3 is not None:
		mouseleft(loc3[0], loc3[1])
		sleep(0.5)
		flag4 = False
		flag3 = False

'''