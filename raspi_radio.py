#!/usr/bin/python3 
# -*- coding: utf-8 -*-

# 2021 - Pocuvanie Radia Muzika cez Raspberry Pi formou Transmitter
# 
#

import requests
import time
import os

_debug = False

LIMIT_SLEEP = 5

DEBUG = True


session = requests.Session()

URL = "http://www.orange.sk/lp/limit?offerName=BO_DATA_Data%201%20Eur"
URL2 = "http://www.orange.sk/lp/limit/confirm/choosed/BO_DATA_Data+1+Eur-LP_TEMP_DISABLE_CONTINUE"

def vypis(*data):
	print (*data, flush=True)

def postDataOrangePotvrd():

	pyload = {
		'submit': 'AKTIVOVAT',
		'activate': 'AKTIVOVAT',
		#'activateOption': 'activateOption-BO_DATA_Data 1 Eur-LP_TEMP_DISABLE_CONTINUE',
		'choosedOption': 'BO_DATA_Data 1 Eur-LP_TEMP_DISABLE_CONTINUE'
	}
	_no_error = True
	vypis ('== post Data Orange AKTIVOVAT ===')
	try:
		r = session.post(URL2, data = pyload, timeout=15)
		vypis (r.status_code)
		vypis (r.headers)
		vypis (r.encoding)
		vypis (r.request.headers)
		vypis (r.cookies)
		vypis (r.url)
		vypis (r.request)
		vypis (r.reason)
	except:
		_no_error = False
		vypis ('CHYBA SPOJENIA... ', key)

	if _no_error:
		s = r.text
		if _debug:
			vypis (s)

		return True

	return False

def postDataOrange():
	pyload = {
		'submit': 'Aktivovať',
		'activate': 'activate',
		#'activateOption': 'activateOption-BO_DATA_Data 1 Eur-LP_TEMP_DISABLE_CONTINUE',
		'activateOption': 'BO_DATA_Data 1 Eur-LP_TEMP_DISABLE_CONTINUE'
	}

	_no_error = True
	vypis ('== post Data Orange ===')
	try:
		r = session.post(URL, data = pyload, timeout=15)
		vypis (r.status_code)
		vypis (r.headers)
		vypis (r.encoding)
		vypis (r.request.headers)
		vypis (r.cookies)
		vypis (r.url)
		vypis (r.request)
		vypis (r.reason)
	except:
		_no_error = False
		vypis ('CHYBA SPOJENIA... ', key)

	if _no_error:
		s = r.text#.encode('ISO-8859-1')     #.encode('utf-8')
		if _debug:
			vypis (s)
		t = False
		if 'AKTIVOVAT' in s:
			print ('Chystam sa aktivovat sluzbu...')
			time.sleep(3)
			t = postDataOrangePotvrd()
		return t

	return False


def isee(text):
	if DEBUG:
		print (text)


def checkInternet():
	#url = "https://1.1.1.1"
	url = 'https://listen.radioking.com'
	timeout = 50
	try:
		request = requests.get(url, timeout=timeout)
		isee("Internet OK :)")
		#if 'Dosiahnutie dátového limitu' in request.text:
		if 'precerpanie-options' in request.text:
			isee('Orange precerpanie limitu...')
			c = postDataOrange()
			if c:
				time.sleep(10)
			return c
		return True
	except (requests.ConnectionError, requests.Timeout) as exception:
		isee("NO Internet !.")
		return False


def runRadio():
	isee('Spustam Radio Muzika')
	try:
		os.system('/home/pi/radio.sh')
	except:
		isee('Radio chyba')
		return False
	return True

def killRadio():
	os.system('/home/pi/radio_kill.sh')

def checkInternetNonstop():	
	interval = 10
	restart = True
	while True:
		c = checkInternet()
		if c == False:
			killRadio()
			restart = True
			interval = 3
		else:
			if restart:
				d = runRadio()
				if d:
					restart = False
				else:
					killRadio()

			interval = 10
	
		time.sleep(interval)
		

if __name__ == "__main__":
	postDataOrange()
	checkInternetNonstop()

