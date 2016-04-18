# -*- coding: utf-8 -*-
import sys, re
import codecs
import string
import datetime
import itertools
import collections
from lxml import etree
from io import StringIO, BytesIO
from math import log
import transcoder
"""
	Code to remove unnecessary tags from GRETIL pada indices and create a list of words in descending order.
	Usage python padaindexanalyser.py
	input - padadump.txt (a copy paste from GRETIL pada indices)
	output - 1. padawords.txt and 2. PI.txt. First is unsorted list, second is sorted according to occurrence.
"""
def removetag(text):
	output = re.sub(r'[ ][^ ]+$','',text)
	return output		
def finetune(text):
	output = transcoder.transcoder_processString(text,'roman','slp1')
	output = re.sub(r'^\'','a',output)
	return output
if __name__=="__main__":
	# part 1
	fin = codecs.open('dicts/padadump.txt','r','utf-8')
	fout = codecs.open('dicts/padawords.txt','w','utf-8')
	data = fin.readlines()
	fin.close()
	print "Reading lines"
	counter = 0
	for datum in data:
		dat = removetag(datum)
		counter = counter + 1
		lst = dat.split(' ')
		for member in lst:
			fout.write(finetune(member)+'\n')
		if counter % 1000 == 0:
			print counter
	fout.close()
	# part 2
	fin = codecs.open('dicts/padawords.txt','r','utf-8')
	words = fin.readlines()
	fin.close()
	fout = codecs.open('dicts/PI.txt','w','utf-8')
	output = collections.Counter(words).most_common()
	for (a,b) in output:
		fout.write(a)
