import os
import datetime.datetime
import time

filename = '/var/nslog/metrics_prom_demo_prometheus_profile.log'

while (True):
  ts = os.path.getmtime(filename)
  datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')
  time.sleep (2) #print timestamp every 2 seconds
