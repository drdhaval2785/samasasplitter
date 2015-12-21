# -*- coding: utf-8 -*-
import sys, re, codecs, string, datetime, itertools
from lxml import etree
from io import StringIO, BytesIO
from math import log
import collections
	
def unique(lst):
	output = []
	for member in lst:
		if member not in output:
			output.append(member)
	return output
def createwordlist(inputfile,outputfile):
	lines = open(inputfile).read().split()
	output = open(outputfile,'w')
	for line in lines:
		line = line.strip('0123456789.*')
		line = line.strip()
		if line is not '':
			output.write(line+"\n")
	output.close()
def sortbyfrequency(inputfile):
	lines = open(inputfile).read().split()
	counter = collections.Counter(lines)
	decreasing = counter.most_common()
	decreasing = sorted(decreasing, key=lambda x:(x[1],len(x[0])), reverse=True)
	output = open(inputfile, 'w')
	for (word,counter) in decreasing:
		if len(word) > 1:
			output.write(word+"\n")
	output.close()
def readwords(dictionary):
	return open(dictionary).read().split()
def sanhw2():
	fin = codecs.open('../CORRECTIONS/sanhw2/sanhw2.txt','r','utf-8')
	lines = fin.readlines()
	output = []
	for line in lines:
		line = line.strip()
		split = line.split(':') # ['aMSakalpanA', 'CAE;4,CCS;4,MD;4,MW;21,PD;50,PW;9']
		word = split[0] # 'aMSakalpanA'
		dictswithlnum = split[1].split(',') # ['CAE;4','CCS;4','MD;4','MW;21','PD;50','PW;9']
		dicts = []
		lnums = []
		for dictwlnum in dictswithlnum:
			[dict,lnum] = dictwlnum.split(';')
			dicts.append(dict) # ['CAE','CCS','MD','MW','PD','PW']
			lnums.append(lnum) # [4,4,4,21,50,9]
		output.append((word,dicts,lnums))
	return output
def createhwlist(dict):
	print "Creating headword data of", dict
	fout = codecs.open('dicts/'+dict+'.txt','w','utf-8')
	hw = []
	for (hword,dicts,lnums) in sanhw2:
		if len(hword) > 1 and (dict in dicts or dict=='ALL'):
			fout.write(hword+"\n")
			hw.append(hword)
	fout.close()
	print len(hw)
	print "Created headword data of", dict 

def colognedata():
	dictionaryname = ["ACC","CAE","AE","AP90","AP","BEN","BHS","BOP","BOR","BUR","CCS","GRA","GST","IEG","INM","KRM","MCI","MD","MW72","MW","MWE","PD","PE","PGN","PUI","PWG","PW","SCH","SHS","SKD","SNP","STC","VCP","VEI","WIL","YAT","ALL"]
	for dictionary in dictionaryname:
		createhwlist(dictionary)
def sortdescending(lst):
	return sorted(lst,key=len,reverse=True)
def upasarga():
	f = codecs.open('../inriaxmlwrapper/SL_preverbs.txt','r','utf-8')
	data = f.readlines()
	ups = []
	for line in data:
		word = line.split(' = ')[0]
		ups.append(word)
	return ups
		
def gerarddata():
	# Parsing the XMLs. We will use them as globals when need be.
	print "Preparing data of Gerard in gerard.txt"
	roots = etree.parse('../inriaxmlwrapper/SL_roots.xml') # parses the XML file.
	nouns = etree.parse('../inriaxmlwrapper/SL_nouns.xml')
	adverbs = etree.parse('../inriaxmlwrapper/SL_adverbs.xml')
	final = etree.parse('../inriaxmlwrapper/SL_final.xml')
	parts = etree.parse('../inriaxmlwrapper/SL_parts.xml')
	pronouns = etree.parse('../inriaxmlwrapper/SL_pronouns.xml')
	print 'Parsing over.'
	out = []
	for x in [nouns,roots,pronouns,final,parts,adverbs]:
		# Storing data
		out += [member.get('form') for member in x.xpath('/forms/f')]
	for up in sorted(upasarga(),key=len,reverse=True):
		out.append(up)
	out = list(set(out))
	out = sorted(out,key=len,reverse=True)	
	fout = codecs.open('dicts/gerard.txt','w','utf-8')
	for mem in out:
		fout.write(mem+"\n")
	print "Completed adding data to gerard.txt"
	fout.close()
def mwstrip(word):
	reps = ["/","'","^",">"]
	for rep in reps:
		word = word.replace(rep,'')
	word = word.replace(' ','-')
	word = re.sub('-{1,}','-',word)
	return word
def mwcomponentdata():
	# Parsing the XMLs. We will use them as globals when need be.
	print "Preparing data of MW from mw.xml"
	mw = etree.parse('../Cologne_localcopy/mw/mwxml/xml/mw.xml') # parses the XML file.
	print 'Parsing over.'
	out = [member.text for member in mw.xpath('/mw/*/h/key2')]
	fout = codecs.open('dicts/mwb.txt','w','utf-8')
	print len(out)
	samasamembers = []
	for i in xrange(len(out)):
		member = out[i]
		if member is not None:
			member = mwstrip(member)
			parts = member.split('-')
			for mem in parts:
				if len(mem) > 1:
					samasamembers.append(mem)
	count = collections.Counter(samasamembers)
	count = count.most_common()
	count = sorted(count, key=lambda x:(x[1],len(x[0])),reverse=True)
	for (a,b) in count:
		fout.write(a+"\n")
	print "Completed adding data to mwb.txt"
	fout.close()
def mwsplitlist():
	# Parsing the XMLs. We will use them as globals when need be.
	print "Preparing data of MW from mw.xml"
	mw = etree.parse('../Cologne_localcopy/mw/mwxml/xml/mw.xml') # parses the XML file.
	print 'Parsing over.'
	out = [member.text for member in mw.xpath('/mw/*/h/key2')]
	fout = codecs.open('dicts/mw2.txt','w','utf-8')
	print len(out)
	samasamembers = []
	for i in xrange(len(out)):
		member = out[i]
		if member is not None:
			member = mwstrip(member)
			if '-' in member:
				unsplit = member.replace('-','')
				member = member.replace('-','+')
				fout.write(unsplit+':'+member+'\n')
	print "Completed adding data to mw2.txt"
	fout.close()

if __name__=="__main__":
	"""
	sanhw2 = sanhw2()
	sanhw2 = sorted(sanhw2, key=lambda x: (len(x[1]),len(x[0])), reverse=True)
	colognedata()
	gerarddata()
	mwcomponentdata()
	"""
	mwsplitlist()