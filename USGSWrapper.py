import requests
import csv
import pandas as pd
import dateutil.parser as dateparser

'''
File ini mengandung wrapper dan controller yang menanggung proses dari
pengambilan data pada USGS. Data yang diterima dari USGS berbentuk CSV

Parameter yang dibutuhkan untuk memenuhi parameter dari pengguna:
- starttime
- endtime
- maxlatitude
- minlatitude
- maxlongitude
- minlongitude
- minmagnitude
- maxmagniude
- mindepth
- maxdepth
- orderby

Atribut yang akan diambil pada data ini adalah:
- time
- latitude
- longitude
- depth
- mag
'''

baseUrl = "https://earthquake.usgs.gov/fdsnws/event/1/query.csv"
columnList = ['time', 'latitude', 'longitude', 'depth', 'mag']

def getEarthquakeData():
    reader = pd.read_csv(baseUrl, usecols=columnList);
    data = reader.to_dict('r')
    for row in data:
        row['time'] = int(dateparser.parse(row['time']).timestamp()*1000)
    return data

if __name__ == "__main__":
    data = getEarthquakeData()
    print(data[0])