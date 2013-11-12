#!/usr/bin/python
# -*- coding: utf-8 -*-

# pip install urllib
import urllib
import sys
# pip install html.py
#import HTML
#import datetime
# pip install BeautifulSoup4
from bs4 import BeautifulSoup
#from collections import OrderedDict

parcelID = sys.argv[1]

#print('Getting details for package ID: ' + str(parcelID))
pageURL = ('http://nolp.dhl.de/nextt-online-public/set_identcodes.do?lang=de&idc=' + parcelID)
#print('Grabbing page: ' + pageURL)
statusPage = urllib.urlopen(pageURL)
statusSoup = BeautifulSoup(statusPage.read())
statusMSG = statusSoup.find('td', attrs={ 'class': 'mm_delivered'}).get_text()
statusMSG = statusMSG.strip().split()[4:]
print(' '.join(statusMSG) + '.')
