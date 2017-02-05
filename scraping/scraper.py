import os, sys; sys.path.insert(0, os.path.join("..", ".."))
import json
import csv
import time as t
import requests
from datetime import datetime, date, timedelta


def scraper(date, nb_year):
	""" 
		Scrap all flicker's photo from the flicker api in json format, for a period of time. The json fill will be then merged in one
		csv file.

		date -- a structur date from which the scraping start
		nb_year -- corresponds to number of years that should be scraped starting from the date above.
	"""
	
	# prepare for the ice age
	d1 = date
	oneDay = timedelta(days=1)
	d2 = d1 + oneDay


	print("--Grabing flicker from ficker api since "+ date.year)
	
	#scraping per days for each year
	for i in range(1, 365*nb_year):
	        d2 = d1 + oneDay
	        params = {'method': 'flickr.photos.search', 'format' : 'json', 'woe_id' : 23424957, 'api_key':"5784927bc745bbf1649a65c0b9174018", 'min_taken_date':str(d1), 'max_taken_date':str(d2), 'extras':"tags, original_format, license, geo, date_taken, date_upload, o_dims, views"}
	        data = requests.get('https://api.flickr.com/services/rest/', params=params)
	        dataFile = open(path + str(d1) + "-photos.json","w+")
	        dataFile.write(data.text)
	        dataFile.close()
	        dataJSONified = json.loads(data.text.lstrip("jsonFlickrApi(").rstrip(')'))
	        pages = dataJSONified["photos"]["pages"]

	        for page in range(2,pages+1,1):
	            params = {'method': 'flickr.photos.search', 'format' : 'json', 'woe_id' : 23424957, 'api_key':"5784927bc745bbf1649a65c0b9174018", 'min_taken_date':str(d1), 'max_taken_date':str(d2), 'extras':"tags, original_format, license, geo, date_taken, date_upload, o_dims, views", 'page':page}
	            data = requests.get('https://api.flickr.com/services/rest/', params=params)  
	            dataFile = open(path + str(d1) + "-" + str(page) + "-photos.json","w+")
	            dataFile.write(data.text)
	            dataFile.close()

	        d1 = d1 + oneDay
	        #to avoid to be banned 
	        t.sleep()
	
	print("--Convesting json files to csv file")

	dirlist = os.listdir(path)
	csvFile = csv.writer(open('Flickrs-Switzerland-1990-2017.csv', 'w+'), delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	csvFile.writerow(['userid', 'title', 'dateupload', 'datetaken', 'views', 'tags', 'lat', 'lon', 'place_id', 'woeid'])

	#Convert the colllected json files to one csv file
	for name in dirlist:
	    if name.endswith("photos.json"): 
	        data = open(path + name,'r').read().lstrip('jsonFlickrApi(').rstrip(')')

	        dataJsonify = json.loads(data)

	        for photo in dataJsonify['photos']['photo']:
	            userid = photo['owner']
	            title = photo['title']#.encode('utf-8')
	            dateupload = photo['dateupload']
	            datetaken = photo['datetaken']
	            views = photo['views']
	            tags = photo['tags']#.encode('utf-8') 
	            lat = photo['latitude']
	            lon = photo['longitude']
	            #print(photo['place_id'])
	            try:
	                place_id = photo['place_id']
	            except:
	                place_id = ""    
	            try:
	                woeid = photo['woeid']
	            except:
	                woeid = ""
	            
	            csvFile.writerow([userid, title, dateupload, datetaken, views, tags, lat, lon, place_id, woeid])

	print("--Scraping done")

