#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# pip install urllib
import urllib
import sys

# pip install BeautifulSoup4
from bs4 import BeautifulSoup

def dhlparse(parcelID):

  if not len(parcelID) == 12 or not parcelID.isdigit():
    print('DHL parcel-ID must be 12 digit number')
    return(-1)

  #print('Getting details for package ID: ' + str(parcelID))
  pageURL = ('http://nolp.dhl.de/nextt-online-public/set_identcodes.do?lang=de&idc=' + parcelID)
  #print('Grabbing page: ' + pageURL)

  try:
    statusPage = urllib.urlopen(pageURL)
    statusSoup = BeautifulSoup(statusPage.read())
  except:
    print('Could not grab the URL, something is wrong here: ' + pageURL)
    return(-1)
    pass

  try:
    statusMSG = statusSoup.find('td', attrs={ 'class': 'mm_delivered'}).get_text()
    statusMSG = statusMSG.strip().split()[4:]
  except:
    print('Something is wrong!!! Could not grab the status from the Page: ' + pageURL)
    return(-1)
    pass

  return(' '.join(statusMSG) + '.')
