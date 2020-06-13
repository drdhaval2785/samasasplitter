# This Python file uses the following encoding: utf-8
# Author - Dr. Dhaval patel - drdhaval2785@gmail.com - www.sanskritworld.in
# Date - 11 July 2017
import json
import re
import codecs
import datetime
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt

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
	print('started analysis', timestamp())

	input = 'astyuttarasyAMdiSihimAlayonAmanagADirAjaH'
	G = nx.DiGraph()
	print('Adding nodes', timestamp())
	G.add_nodes_from(xrange(len(input)))
	print('Added nodes', timestamp())
	for x in xrange(len(input)):
		for y in range(x+2,len(input)):
			strng = input[x:y]
			if strng in str_counter:
				cnt = str_counter[strng]
				G.add_edge(x,y, weight=cnt, string=strng)
	print('Added edges', timestamp())
	print('ended analysis', timestamp())

