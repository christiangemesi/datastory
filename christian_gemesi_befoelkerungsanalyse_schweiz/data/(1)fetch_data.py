#!/usr/bin/env python3 
# coding: utf-8

from io import BytesIO
import zipfile
from urllib.request import urlopen
import os
import requests
import pandas as pd
import pathlib
import xlrd
import time
import glob

#Variables
url = 'https://www.bfs.admin.ch/bfsstatic/dam/assets/340621/appendix'
req = requests.get(url)
filename = 'appendix'

##change directory to raw
if os.path.exists("raw"):
    os.chdir('raw')
print("changing directory to raw")
    
##open file in case of being to big, downoad it in chunks
with open(filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
print("opening zip file")
time.sleep(1)

##unzip file and extract at current location
with zipfile.ZipFile(filename,"r") as zip_ref:
    zip_ref.extractall("")
print("unzipping file")
time.sleep(1)

##delete unused files
if os.path.exists("Suisse.xls"):
    os.remove("Suisse.xls")
    print("deleting Suisse.xls")
else:
    print("The file does not exist or got already deleted")

if os.path.exists("Grossregionen.xls"):
    os.remove("Grossregionen.xls")
    print("deleting Grossregionen.xls")
else:
    print("The file does not exist or got already deleted")

if os.path.exists("appendix"):
    os.remove("appendix")
    print("removing initial zip file")
else:
    print("The file does not exist or got already deleted")
time.sleep(1)

## make csv files of the old xls files with new format
excelFiles = ["AG","AI","AR","BE","BL","BS","FR","GE","GL","GR","JU","LU","NE","NW","OW","SG","SH","SO","SZ","TG","TI","UR","VD","VS","ZG","ZH"]
array_length = len(excelFiles)

for i in range(array_length) :
    newFile = excelFiles[i]+"-neu.csv"
    oldFile = excelFiles[i]+'.xls'
    
    print(newFile + " created") 
    
    data_dir = pathlib.Path('.')

    data = []
    for xlsfile in data_dir.glob(excelFiles[i]+'.xls'):
        df = pd.read_excel(xlsfile, skiprows=8,usecols=range(18))
        df = df[pd.to_numeric(df.iloc[:, 0], errors='coerce').notna()]
        df = pd.concat([df.iloc[:, 1:].set_index('Unnamed: 1')], 
                       keys=[xlsfile.stem], names=['Kanton', 'Stadt'])
        
        data.append(df)

    df = pd.concat(data)

    df.to_csv(newFile)

    ##delete unused files
    if os.path.exists(oldFile):
        os.remove(oldFile)
    else:
        print("The file does not exist or got already deleted")

        
#put each canton into one big csv
path = os.getcwd()
all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged = pd.concat(df_from_each_file)
print("------------------------------")
print("put all files into one big one")
print("------------------------------")
df_merged.to_csv( "raw_data.csv")
    
for i in range(array_length):
    toRemovedFile = excelFiles[i]+"-neu.csv"
    
    if os.path.exists(toRemovedFile):
        os.remove(toRemovedFile)
        print("remove", toRemovedFile)
    else:
        print("The file does not exist or got already deleted")
        
#change directory back directory
os.chdir('..')
print("changing directory to /data")