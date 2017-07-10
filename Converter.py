# Converter

# This is my first Python script ever :)

import csv
import numpy 
import time

with open('gb.csv', 'rU') as csvFile:
  reader = csv.reader(csvFile, delimiter=';', quotechar='"')
  
  data = list(reader)

id=0
author_name=1
author_email=2
author_origin=3
author_website=4
author_ip=5
author_host=6
content=7
date=8
timefield=9
isspam=10
ischecked=11
istrash=12
admin_reply=13


for (rowIndex, rowItem) in enumerate(data):
  if rowIndex==0:
    continue
  dt=rowItem[date]+" "+rowItem[timefield]
  t = int(time.mktime(time.strptime(dt, "%d/%m/%y %H.%M")))
#  t = (time.strptime("29.08.2011 11:05:02", "%d.%m.%Y %H:%M:%S"))
  print dt + " - " +str(t)
