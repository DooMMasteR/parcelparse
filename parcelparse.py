#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'doommaster'

import sys
from providers import *


possible_modes = ['parse', 'add', 'delete', 'list', 'update', 'help']

try:
  if sys.argv[1] in possible_modes:
    mode = sys.argv[1]
  else:
    print('unknown mode, try help')
    sys.exit(-1)

except:
  print('no argument given, try help')
  sys.exit(-1)
  pass

if mode == possible_modes[0]:
  try:
    provider = sys.argv[2]
    if ('providers.'+ provider) not in sys.modules.keys():
      print('unknown provider')
      sys.exit(-1)
  except:
    print('no or wrong provider')
    sys.exit(-1)
    pass

  try:
    id = sys.argv[3]
  except:
    print('no or wrong id')
    sys.exit(-1)
    pass
  statusMSG = dhl.dhlparse(id)
  if statusMSG == -1:
    sys.exit(-1)
  else:
    print(statusMSG)



