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

to_drop = ['LATITUDE',          
          'LONGITUDE',
          'LOCATION',
           'CONTRIBUTING FACTOR VEHICLE 2',
           'CONTRIBUTING FACTOR VEHICLE 3',
           'CONTRIBUTING FACTOR VEHICLE 4',
           'CONTRIBUTING FACTOR VEHICLE 5',
           'VEHICLE TYPE CODE 1',
           'VEHICLE TYPE CODE 2',
           'VEHICLE TYPE CODE 3',
           'VEHICLE TYPE CODE 4',
           'VEHICLE TYPE CODE 5'
          ]


df.drop(columns=to_drop, inplace=True) #drops listed columns
is_11374 =  df['ZIP CODE'] == '11374'  #returns list of booleans
df_11374 = df[is_11374]  #produces dataframe containing info for 11374 zip only

print('Head of edited dataframe')
print(df_11374.head())
print()
print('Top 5 on street accident sites in Rego Park') 
print(df_11374['ON STREET NAME'].value_counts().head())
print()
print('Top 5 cross street accident sites in Rego Park')
print(df_11374['CROSS STREET NAME'].value_counts().head())
print()
print('Top 5 off street accident sites in Rego Park')
print(df_11374['OFF STREET NAME'].value_counts().head())

sys.exit(0)
