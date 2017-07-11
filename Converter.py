# Converter

# This is my first Python script ever :)

# I know the code might be bad, but it served it's purpose, to convert a CSV file into a new format i could import into a Wordpress guestbook :)

import csv
#import numpy 
import time
from itertools import imap
from operator import itemgetter


with open('gb.csv', 'rU') as csvFile:
  reader = csv.reader(csvFile, delimiter=';', quotechar='"')
  
  data = list(reader)

data = data[1:]

id=0
author_name=1
author_email=2
author_origin=3
author_website=4
author_ip=5
author_host=6
content=7
datetime=8
timefield=9
isspam=10
ischecked=11
istrash=12
admin_reply=13


for (rowIndex, rowItem) in enumerate(data):
  
  dt=rowItem[datetime]+" "+rowItem[timefield]
  t = int(time.mktime(time.strptime(dt, "%d/%m/%y %H.%M")))
  rowItem[datetime]=t
  rowItem[isspam]=0
  rowItem[ischecked]=1
  rowItem[istrash]=0
  rowItem[content]= rowItem[content].replace('"',"&quot;")

fieldnames = ['id','author_name','author_email','author_origin','author_website','author_ip','author_host','content','datetime','isspam','ischecked','istrash','admin_reply']
with open('output.csv', 'wb') as output_file:
            writer = csv.writer(output_file,quotechar='"')
            writer.writerow(fieldnames)
            writer.writerows(imap(itemgetter(0,1,2,3,4,5,6,7,8,10,11,12,13), data))
