#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Orange Login - 1€ - 100 MB dat
# - po precerpani klesne rychlost na 128/128 kB - co pre radio uplne staci :)
# - 
# - Kazdy mesiac treba potvrdit precerpanie dat
# - kedy zo znizenou rychlostou ale zadarmo moze dalej vyuzivat data 
# - kedze to nemaju automaticky a treba to potvrdit, tak sa o to postara tento skript

import requests
import json
import time
import base64

timer = 5
_debug = True


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
        s = r.text#.encode('ISO-8859-1')     #.encode('utf-8')
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


t = postDataOrange()
vypis ('OK = ', t)