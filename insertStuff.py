import pymongo
import json
import random
import time
import datetime
import copy

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
		tempdics = []
		for j in range(len(dictionaries)):
			# pymongo adds the id field to the dictionary automatically, so we can reinsert the same stuff we need to delete that
			if "_id" in dictionaries[j]:
				del dictionaries[j]["_id"]
			# make data a little more random
			tempdics.append(copy.deepcopy(dictionaries[j]))
			tempdics[j]["subject"]["common_name"] = tempdics[j]["subject"]["common_name"]+str(datetime.datetime.utcnow())
			tempdics[j]["serial_number"] =  tempdics[j]["serial_number"]+str(datetime.datetime.utcnow())
		x = mycol.insert_many(tempdics)
		del tempdics
	stop = datetime.datetime.now()
	time = stop - start
	print("Took us ", time.microseconds/1000, " ms for 3000 records")
		
