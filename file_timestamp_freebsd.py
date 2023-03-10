import os
import datetime.datetime
import time

filename = '__my_filename_goes_here__'

while (True):
  ts = os.path.getmtime(filename)
  datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')
  time.sleep (2) #print timestamp every 2 seconds
