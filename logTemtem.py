import logging as lg

lg.basicConfig(filename='C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/logs/log.txt', level=lg.INFO)

def logThis(msg):
	lg.info(msg=msg)



