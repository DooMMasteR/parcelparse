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

# check if parcelID is a valid number 
if not parcelID.isdigit():
  print('ParcelID is not a Number, check your input.')
  sys.exit(-1)

# check if parcelID has 12 digits
if len(parcelID) != 12:
  print('ParcelID must have 12 digits, check yout input.')
  sys.exit(-1)


# construct URL
pageURL = ('http://nolp.dhl.de/nextt-online-public/set_identcodes.do?lang=de&idc=' + parcelID)

# grab the page in soup it
try:
  statusPage = urllib.urlopen(pageURL)
  statusSoup = BeautifulSoup(statusPage.read())
except:
  print('Could not grab the URL, something is wrong here: ' + pageURL)
  sys.exit(-1)
  pass

# find the status message 
try:
  statusMSG = statusSoup.find('td', attrs={ 'class': 'mm_delivered'}).get_text()
  statusMSG = statusMSG.strip().split()[4:]
except:
  print('Something is wrong!!! Could not grab the status from the Page: ' + pageURL)
  sys.exit(-1)
  pass

# print the status message
print(' '.join(statusMSG) + '.')
