#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

import urllib.error, urllib.request, urllib.parse
import json
from dateutil.parser import parse
from dateutil.tz import gettz
from datetime import datetime 

sta = "KBFI"
url = "https://api.weather.gov/stations/{}/observations/latest".format(sta)
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

# First, we make the python equivalent of curl call to
# https://api.weather.gov/stations/KBFI/observations/latest
# and then strip out 'properties.timestamp'
# and .properties.temperature.value
# Then we convert timestamp from ISO-time to something readable,
# and convert temperature from C to F
# Display the time in a small font, 
# and the temperature in something big and fat

# top of loop
# get the data
data = urllib.request.urlopen(url).read()
# deserialize it
wxjson = json.loads(data)

# grab variables and convert
tempc = wxjson['properties']['temperature']['value']
tempf = (tempc * (9 / 5)) + 32
tempfs = "{:.1f}".format(tempf)
obstime = wxjson['properties']['timestamp']
obstimedt = parse(obstime).astimezone()
obstimes = obstimedt.strftime("%I:%M %p")
toplabel = "{} at {}".format(sta, obstimes)

# display it
ttk.Label(frm, text=toplabel).grid(column=0,row=0)
ttk.Label(frm, text=tempfs).grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)
# sleep some convenient time - 15 min?
# bottom of loop
# figure out how to do this refresh thing... 
# and how to change sizes, etc. 
root.mainloop()
