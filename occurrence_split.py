# This Python file uses the following encoding: utf-8
# Author - Dr. Dhaval patel - drdhaval2785@gmail.com - www.sanskritworld.in
# Date - 11 July 2017
import json
import re
import codecs
import datetime
from collections import Counter

# Function to return timestamp
def timestamp():
	return datetime.datetime.now()

def strcnt(str,str_counter):
	if str in str_counter:
		return str_counter[str]
	else:
		return 0

def substrset(strng,sett):
	for member in sett:
		if strng in member:
			return True
	else:
		return False
		
if __name__=="__main__":
	fin = codecs.open('dicts/str_counter/str_counter.json','r','utf-8')
	str_counter = json.load(fin)
	fin.close()
	print 'started analysis', timestamp()
	input = 'astiuttarasyAmdiSihimaAlayasnAmanagaaDirAjas'
	ytotal = Counter()
	probtuple = []
	for i in xrange(len(input)):
		ytotal[i] = 0
	for x in xrange(len(input)):
		zero = False
		for y in range(x+2,len(input)+2):
			str_under_consideration = input[x:y]
			strcount = strcnt(str_under_consideration,str_counter)
			if strcount == 0 and zero == False:
				ytotal[y-1] += 1
				zero = True
				break
	"""
	for (a,b) in ytotal.most_common():
		result = input[:a]+'+'+input[a:]
		print result
	"""
	result = []
	b = 0
	for a in ytotal:
		if ytotal[a] != 0:
			result.append(input[b:a])
			b = a
	result.append(input[b:])
	print result

	validforms = set()
	for x in xrange(len(result)-3):
		if result[x]+result[x+1]+result[x+2]+result[x+3] in str_counter and not substrset(result[x]+result[x+1]+result[x+2]+result[x+3],validforms):
			print result[x]+result[x+1]+result[x+2]+result[x+3]
			validforms.add(result[x]+result[x+1]+result[x+2]+result[x+3])
	for x in xrange(len(result)-2):
		if result[x]+result[x+1]+result[x+2] in str_counter and not substrset(result[x]+result[x+1]+result[x+2],validforms):
			print result[x]+result[x+1]+result[x+2]
			validforms.add(result[x]+result[x+1]+result[x+2])
	for x in xrange(len(result)-1):
		if result[x]+result[x+1] in str_counter and not substrset(result[x]+result[x+1],validforms):
			print result[x]+result[x+1]
			validforms.add(result[x]+result[x+1])
	print 'analysis completed', timestamp()
