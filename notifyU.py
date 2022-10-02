import requests
import logging as lg

lg.basicConfig(filename='C:/Users/roger/AppData/Local/Programs/Python/Python36/temtem/logs/sentSMS.txt', level=lg.INFO)

def notify():
	url = "https://www.fast2sms.com/dev/bulk"
	payload = "sender_id=FSTSMS&message=Luma found at Roger's PC !!!&language=english&route=p&numbers=9891237237,9599950837"
	headers = {
	'authorization': "4oAewhBD7IQXRgf0tTzE35akKxsv8H1MFinUdONuJb6Wqm92jSAu5i4YaMfrWFqHN6Z0wp278lEez3oJ",
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	lg.info(msg=response.text)
	print(f'Response is {response.text}')

def notifyError():
	url = "https://www.fast2sms.com/dev/bulk"
	payload = "sender_id=FSTSMS&message=Error in running away !!!&language=english&route=p&numbers=9891237237,9599950837"
	headers = {
		'authorization': "4oAewhBD7IQXRgf0tTzE35akKxsv8H1MFinUdONuJb6Wqm92jSAu5i4YaMfrWFqHN6Z0wp278lEez3oJ",
		'Content-Type': "application/x-www-form-urlencoded",
		'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)

def notifyError2():
	url = "https://www.fast2sms.com/dev/bulk"
	payload = "sender_id=FSTSMS&message=Error in main prog file !!!&language=english&route=p&numbers=9891237237,9599950837"
	headers = {
		'authorization': "4oAewhBD7IQXRgf0tTzE35akKxsv8H1MFinUdONuJb6Wqm92jSAu5i4YaMfrWFqHN6Z0wp278lEez3oJ",
		'Content-Type': "application/x-www-form-urlencoded",
		'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)