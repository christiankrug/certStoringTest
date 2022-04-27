import pymongo
import json
import random
import time
import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ctMonitor"]
mycol = mydb["certs"]


google = open('test_google.json')
rub = open('test_rub.json')
github = open('test_github.json')

dictionaries = []
dictionaries.append(json.load(google))
dictionaries.append(json.load(rub))
dictionaries.append(json.load(github))

while(True):
	start = datetime.datetime.now()
	for i in range(0,1000):
		x = mycol.insert_many(dictionaries)
		#pymongo adds the id field to the dictionary automatically, so we can reinsert the same stuff we need to delete that
		del dictionaries[0]["_id"]
		del dictionaries[1]["_id"]
		del dictionaries[2]["_id"]
	stop = datetime.datetime.now()
	time = stop - start
	print("Took us ", time.microseconds/1000, " ms for 3000 records")
		
