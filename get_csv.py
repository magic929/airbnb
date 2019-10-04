import pandas
import sys
import os
import sqlite3
import re
import d6tpipe
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# api = d6tpipe.APIClient()
# api.setToken(config['databolt']['token'])
# pipe = d6tpipe.Pipe(api, config['databolt']['pipe'])

path = config['local']['path']
regx = config['local']['file_regex']

column = ["id", "name", "host_id", "summary", "space", 
            "description", "neighborhood_overview", "notes", 
            "transit", "host_id", "host_name", "host_since", 
            "host_verifications", "street", "neighbourhood_cleansed", 
            "latitude", "longitude", "property_type", "room_type", 
            "accommodates", "bathrooms", "bedrooms", "beds", "bed_type", 
            "amenities", "price", "weekly_price", "monthly_price", 
            "security_deposit", "cleaning_fee", "guests_included", 
            "extra_people", "minimum_nights", "maximum_nights", 
            "number_of_reviews", "review_scores_rating", "review_scores_accuracy", 
            "review_scores_cleanliness", "review_scores_checkin", "review_scores_communication", 
            "review_scores_location", "review_scores_value", "reviews_per_month"]

li = []
for f in os.listdir(path):
    try:
        if re.fullmatch(regx, f):
            df = pandas.read_csv(path + f, compression='gzip', usecols=column)
            li.append(df)
            # df.to_sql('listing', conn, if_exists='append', index=False)
    except Exception as e:
        print("load the file error", e)

frame = pandas.concat(li, axis=0, ignore_index=True)    
frame.to_csv('data/airbnb_list.csv')
# pipe.push_preview()
# pipe.push()
