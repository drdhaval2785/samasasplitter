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

def dictlnumback(dicts,lnums):
	output = ''
	for i in xrange(len(dicts)):
		output += ","+dicts[i]+";"+lnums[i]
	output = output.strip(',')
	return output
def definitecompound(inputword,dictionary):
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
	for (word,dicts,lnums) in sanhw2:
		(hw,split) = definitecompound(word,dictionary)
		if hw is not '':
			print hw, '-', split
			fout.write(hw+":"+split+":"+dictlnumback(dicts,lnums)+"\n")
	fout.close()	
	
	
	
		
	
