# -*- coding: utf-8 -*-
import sys, re
import codecs
import string
import datetime
import itertools
import collections
import sys
	
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
if __name__=="__main__":
	sanhw2 = sanhw2()
	sanhw2 = sorted(sanhw2, key=lambda x: (len(x[1]),len(x[0])), reverse=True)
	colognedata()

	