"""
mv_longlat_11374

This program prints a csv file of all motor vehicle accidents in 11374 zip code
from 07/17/2012 to 05/13/2019

The Google Map link is:
https://drive.google.com/open?id=1dx8_fza2K0wba2TxX1Cal_J4vmf4awRE&usp=sharing

There are a few obvious errors in the data that place accidents in other
boroughs.


"""

import sys
import csv   #Comma-separated values.  Do not name this Python script csv.py.
import datetime
import urllib.request
import io
import pandas as pd
from functools import reduce


url = "https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv" \
    "?accessType=DOWNLOAD"  

try:
    fileFromUrl = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = fileFromUrl.read() #Read whole file into one big sequenceOfBytes.
fileFromUrl.close()

try:
    s = sequenceOfBytes.decode("utf-8")    #s is a string
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

fileFromString = io.StringIO(s)
df = pd.read_csv(fileFromString, dtype = {'ZIP CODE': str}) #reads in fileFromString as DataFrame
fileFromString.close()

df.fillna(0, inplace=True) #replaces NaN values with 0

to_drop = [
            'CONTRIBUTING FACTOR VEHICLE 2',
            'CONTRIBUTING FACTOR VEHICLE 3',
            'CONTRIBUTING FACTOR VEHICLE 4',
            'CONTRIBUTING FACTOR VEHICLE 5',
            'VEHICLE TYPE CODE 1',
            'VEHICLE TYPE CODE 2',
            'VEHICLE TYPE CODE 3',
            'VEHICLE TYPE CODE 4',
            'VEHICLE TYPE CODE 5',
            'TIME',
            'BOROUGH',
            'ON STREET NAME',
            'CROSS STREET NAME',
            'OFF STREET NAME',
            'NUMBER OF PERSONS INJURED',
            'NUMBER OF PERSONS KILLED',
            'NUMBER OF PEDESTRIANS INJURED',
            'NUMBER OF PEDESTRIANS KILLED',
            'NUMBER OF CYCLIST INJURED',
            'NUMBER OF MOTORIST INJURED',
            'NUMBER OF MOTORIST KILLED',
            'CONTRIBUTING FACTOR VEHICLE 1',
            'UNIQUE KEY',
            'DATE',
            'NUMBER OF CYCLIST KILLED',
            'LOCATION'
          ]

df.drop(columns=to_drop,inplace=True)

is_11374 =  df['ZIP CODE'] == '11374'  #returns list of booleans
df_11374 = df[is_11374]  #produces dataframe containing info for 11374 zip only
df_11374 = df_11374[df_11374['LONGITUDE']!=0]
df_11374 = df_11374[df_11374['LATITUDE']!=0]

print(df_11374.to_csv(index=False))
