# -*- coding: utf-8 -*-
"""
Usage
python compoundstudy.py <dictname>
e.g.
python compoundstudy.py mwb

Read data from sanhw2.txt and compare it against
dictionary MD.
When a word is possibly a compound, it is stored in 
compoundhw.txt file.
This would require a cursory checking.

"""
import sys, re
import codecs
import string
import datetime
import itertools
from lxml import etree
from io import StringIO, BytesIO
import re
from math import log
import split as sp

def timestamp():
	return datetime.datetime.now()
def dictlnumback(dicts,lnums):
	output = ''
	for i in xrange(len(dicts)):
		output += ","+dicts[i]+";"+lnums[i]
	output = output.strip(',')
	return output

knownpairs = sp.readmwkey2()
def definitecompound(inputword,dictionary):
	global knownpairs, knownsplitcounter
	knownbreak = list(set([b for (a,b) in knownpairs if inputword==a]))
	if len(knownbreak) > 0:
		knownsplitcounter += 1
		if len(knownbreak) > 1:
			print inputword, 'has more than two possible breaks.', knownbreak
		return (inputword,knownbreak[0])
	comp = sp.infer_spaces(inputword,dictionary)
	splits = comp.split('+')
	if len(splits) > 1:
		splitlen = [len(member) for member in splits]
		if min(splitlen) > 3:
			return (inputword,comp)
		else:
			return ('','')
	else:
		return ('','')
		
	
if __name__=="__main__":
	print "Creating sanhw2 data"
	sanhw2 = sp.sanhw2()
	print "Created sanhw2 data"
	fout = codecs.open('compoundstudy/compoundhw.txt','w','utf-8')
	dictionary = 'dicts/mwb.txt'
	if len(sys.argv) == 2:
		dictionary = 'dicts/'+sys.argv[1]+'.txt'
	counter = 0
	samasacounter = 0
	knownsplitcounter = 0
	print "Data would be put in compoundstudy.txt"
	print "Will notify after every 100 samAsas split in the following format"
	print "Splits - <samasa_separated> / <words_examined>, Known splits - <words_split_from_mw_key_2_splits>"
	data = []
	for (word,dicts,lnums) in sanhw2:
		(hw,split) = definitecompound(word,dictionary)
		counter += 1
		if hw is not '':
			samasacounter += 1
			if samasacounter % 100 == 0:
				print 'Splits -',samasacounter, '/', counter, ', Known splits -', knownsplitcounter
			fout.write(hw+":"+split+":"+dictlnumback(dicts,lnums)+"\n")
	fout.close()	
	
	
	
		
	
