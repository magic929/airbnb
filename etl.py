import pandas
import sys
import os
import sqlite3
import re

conn = sqlite3.connect('./db/airbnb.db')

path = "./data/"
regx = "amsterdam_.*_data_listings.csv.gz"
for f in os.listdir(path):
    try:
        if re.fullmatch(regx, f):
            print(f)
            df = pandas.read_csv(path + f, compression='gzip')
            df.to_sql('listing', conn, if_exists='append', index=False)
    except Exception as e:
        print("load the file error", e)
    
