#!/usr/bin/python

import urllib3
import json


# for retrieving from the dotmic api
class Dotmic:
	
	def __init__(self, key):
		self.KEY = key


	def search(self, query, count=3):
		
		if count > 10:
			count = 3
			
		query = query.split(" ")
		try:
			qr = "+".join(query)
			url = "http://api-v1-dotmic.in/?search=%s&start-index=0&max-results=%s&ua=%s" %(qr,str(count),self.KEY)
			http = urllib3.PoolManager()
			response = http.request('GET',url)
			data = json.loads(response.data)
			return data
		except UnicodeEncodeError:
			print "Item cannot be encoded"
