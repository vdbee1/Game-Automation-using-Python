import time
from temtem.runAway import runnn
from temtem.notifyU import notify, notifyError2
from temtem.lumaSearch import detectLuma
from temtem.detectEncounter import detectEncounter
from temtem.mouseANDkeyboard import up,down,left,right
from temtem.catch_and_release import catchemall
from temtem.logTemtem import logThis


#TODO implement pause functionality
if __name__ == '__main__':
	for i in range(4,0,-1):
		print(f'Program starts running in {i}')
		time.sleep(1)
	counter = 0
	while True:
		if not detectEncounter():
			up()
			down()
			#left()
			#right()
		elif detectEncounter():
			runnn()
			#if detectLuma():
				#notify()
				#time.sleep(86400)wsw
			#catchemall()
			logThis(f'Encounter no. {counter+1}')
			print(f'Encounter no. {counter+1}')
			counter += 1
			time.sleep(5)
		else:
			print("Error")
			notifyError2()
