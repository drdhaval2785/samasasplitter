# This Python file uses the following encoding: utf-8
# Author - Dr. Dhaval patel - drdhaval2785@gmail.com - www.sanskritworld.in
# Date - 11 July 2017
import json
import re
import codecs
import datetime

# Function to return timestamp
def timestamp():
	return datetime.datetime.now()

def strcnt(str,str_counter):
	if str in str_counter:
		return str_counter[str]
	else:
		return 0
if __name__=="__main__":
	fin = codecs.open('dicts/str_counter/str_counter.json','r','utf-8')
	str_counter = json.load(fin)
	fin.close()
	print 'started analysis', timestamp()
	input = 'astiuttarasyAmdiSihimAlayasnAmanagaaDirAjas'
	ytotal = {}
	for i in xrange(len(input)):
		ytotal[i] = 0
	for x in xrange(len(input)):
		zero = False
		for y in range(x+2,len(input)+1):
			str_under_consideration = input[x:y]
			strcount = strcnt(str_under_consideration,str_counter)
			if strcount == 0 and zero == False:
				ytotal[y-1] += 1
				zero = True
	for i in xrange(len(input)):
		print input[i], ytotal[i]
	print 'completed analysis', timestamp()
