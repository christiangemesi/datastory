#!/usr/bin/env python3 
# coding: utf-8

import pandas as pd
import os

#anpassen der datatypes

#change directory to raw
if os.path.exists("raw"):
    os.chdir('raw')
    print("changing directory to raw")
else:
    raise ValueError('couldnt change to directory raw')

df = pd.read_csv('raw_data.csv', na_values=['.'])
print("reading raw_data.csv")

print("renaming columns and doing some magic")
del df['Unnamed: 0']
df.columns = ['Kanton', 'Stadt', '1850','1860', '1870','1880','1890','1900','1910','1920','1930','1940','1950','1960','1970','1980','1990','2000']
df = df.astype('string')

print("setting datatypes")
years = ['1850','1860', '1870','1880','1890','1900','1910','1920','1930','1940','1950','1960','1970','1980','1990','2000']
for i in years:
    df[i] = df[i].replace(['...'],'0')
    df = df.astype({i:float})
    
os.chdir('..')

##change directory to processed
if os.path.exists("preprocessed"):
    os.chdir('preprocessed')
    print("changing directory to preprocessed")
else:
    raise ValueError('couldnt change to directory preprocessed')

print("saving processed_data.csv")
df.to_csv('processed_data.csv')

os.chdir('..')