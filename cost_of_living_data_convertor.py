# -*- coding: utf-8 -*-
"""cost-of-living-data-convertor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10_cemCbQOwqG-jh0IZpDqd8Bt7HMWLG2

# IMPORT LIBRARIES
"""

import pandas as pd;

"""# IMPORT EXCELL FILE AND STORE IT INTO DATAFRAME THEN LOAD FOR CHECK DATA"""

file_name = "./cost-of-living.csv"

df = pd.read_csv(file_name)

df.head()

"""# GETING COLUMN NAMES HAVING NUMBER DATA"""

df_numbers_keys = df.drop(df.select_dtypes(include=['object']).keys().tolist(),axis=1).keys().tolist()
df_numbers_keys

"""# DATA CONVERSION FOR COLUMN DATA TO ROW"""

dataConverted = {"sno":[],"country":[],"city":[],"expense":[],"amount":[],"data_quality":[]}

def rowConverter(val,col_name):
  # data value get
  sno = i + 1
  ctr = current_row['country']
  city = current_row['city']
  expname = col_name
  amt = current_row[col_name]
  d_quality = current_row['data_quality']

  print(f"{sno} => {ctr} => {city} => {expname} => {amt} => {d_quality}")
  
  # add value in dataConverted dictonary
  dataConverted['sno'].append(sno)
  dataConverted['country'].append(ctr)
  dataConverted['city'].append(city)
  dataConverted['expense'].append(expname)
  dataConverted['amount'].append(amt)
  dataConverted['data_quality'].append(d_quality)

for i in range(0,len(df)):
    current_row = df.loc[i]
    for j in df_numbers_keys:
      if j!="data_quality":
        rowConverter(current_row,j)

dataConverted

MyData = pd.DataFrame(dataConverted)

MyData.head()

MyData.to_csv('cost-of-living-row.csv');