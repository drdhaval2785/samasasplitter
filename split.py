# -*- coding: utf-8 -*-
"""
python split.py aDigrahaRa MW
or
python split.py batchprocess/input.txt MW batchprocess/output.txt
"""
import sys, re
import codecs
import string
import datetime
import itertools
from lxml import etree
from io import StringIO, BytesIO
from math import log
import transcoder

# Function to return timestamp
def timestamp():
	return datetime.datetime.now()

def triming(lst):
	output = []
	for member in lst:
		member = member.strip()
		output.append(member)
	return output

def preparation(inputfile,translit='deva'):
	infile = codecs.open(inputfile,'r','utf-8')
	inputwords = infile.read().split()
	inputwords = triming(inputwords)
	output = []
	for word in inputwords:
		word = transcoder.transcoder_processString(word,'deva','slp1')
		if re.search('[^A-Za-z]',word):
			word = re.sub('[^A-Za-z]','',word)
			if not word == '':
				output.append(word)
		else:
			output.append(word)
	return output
	
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
def createhwlist(dictname):
	print "Creating headword data of sanhw2.txt"
	global sanhw2
	sanhw2 = sanhw2()
	sanhw2 = sorted(sanhw2, key=lambda x: (len(x[1]),len(x[0])), reverse=True)
	fout = codecs.open('dicts/hwsorted.txt','w','utf-8')
	hw = []
	for (hword,dicts,lnums) in sanhw2:
		if len(hword) > 1 and dictname in dicts:
			fout.write(hword+"\n")
			hw.append(hword)
	fout.close()
	print len(hw)
	print "Created headword data of sanhw2.txt"
def readwords(dictionary):
	return open(dictionary).read().split()
def startingpatterns(words):
	output = []
	for word in words:
		output += [word[2:x] for x in range(len(word))]
	return output
def readmwkey2():
	fin = codecs.open('dicts/mw2.txt','r','utf-8')
	lines = fin.readlines()
	lines = triming(lines)
	pairs = []
	for line in lines:
		[word,split] = line.split(':')
		pairs.append((word,split))
	return pairs
def unique(lst):
	output = []
	for member in lst:
		if member not in output:
			output.append(member)
	return output
# Asked the procedure at http://stackoverflow.com/questions/34108900/optionally-replacing-a-substring-python
def permut(word,lstrep,dictionary):
	global startpatterns # words from dictionary base
	dictset = set(dictionary)
	input_str = word
	# make substitution list a dict for easy lookup
	lstrep_map = dict(lstrep)
	# a substitution is an index plus a string to substitute. build
	# list of subs [[(index1, sub1), (index1, sub2)], ...] for all
	# characters in lstrep_map.
	subs = []
	for i, c in enumerate(input_str):
		if c in lstrep_map:
			subs.append([(i, sub) for sub in lstrep_map[c]])
	# build output by applying each sub recorded
	out = []
	for sub in itertools.product(*subs):
		# make input a list for easy substitution
		input_list = list(input_str)
		for j, cc in sub:
			if ''.join(input_list[0:2]) == word[0:2] and input_list[-1] == word[-1]:
				if input_str[0:j]+cc[0] in dictset:
					input_list[j] = cc
					out.append(''.join(input_list))
	out = list(set(out))
	out = sorted(out, key=len)
	return out
def permut1(word,lstrep,dictionary):
	global startpatterns # words from dictionary base
	dictset = set(dictionary)
	input_str = word
	# make substitution list a dict for easy lookup
	lstrep_map = dict(lstrep)
	# a substitution is an index plus a string to substitute. build
	# list of subs [[(index1, sub1), (index1, sub2)], ...] for all
	# characters in lstrep_map.
	subs = []
	for i, c in enumerate(input_str):
		if c in lstrep_map:
			subs.append([(i, sub) for sub in lstrep_map[c]])
	# build output by applying each sub recorded
	out = []
	for sub in itertools.product(*subs):
		# make input a list for easy substitution
		input_list = list(input_str)
		for j, cc in sub:
			if ''.join(input_list[0:2]) == word[0:2] and input_list[-1] == word[-1]:
				if input_str[0:j]+cc[0] in dictset:
					input_list[j] = cc
					out.append(''.join(input_list))
	out = list(set(out))
	out = sorted(out, key=len)
	return out
replas = [('kk','k'),('kK','K'),('gg','g'),('gG','G'),('NN','N'),('cc','c'),('cC','C'),('jj','j'),('jJ','J'),('YY','Y'),('ww','w'),('wW','W'),('qq','q'),('qQ','Q'),('RR','R'),('tt','t'),('tT','T'),('dd','d'),('dD','D'),('nn','n'),('pp','p'),('pP','P'),('bb','b'),('bB','B'),('mm','m'),('yy','y'),('rr','r'),('ll','l'),('vv','v'),('SS','S'),('zz','z'),('ss','s'),('hh','h'),('y','i'),('y','I'),('v','u'),('v','U'),]
def deduplicate(word):
	global replas
	for (a,b) in replas:
		word = word.replace(a,b)
	return word

term = [('A','a'),('I','i'),('AH','a'),('AH','as'),('aH','as'),('H',''),('m',''),('M',''),('O',''),('I','a'),('e','a')]
def determ(word):
	global term
	output = []
	if re.search('[AHImMO]$',word):
		for (a,b) in term:
			if re.search(a+'$',word):
				output.append(re.sub(a+'$',b,word))
	return output

#http://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words/11642687#11642687
def infer_spaces(s,dictionary):
    global words
    global wordcost
    global maxword
    #print len(words), len(wordcost), maxword
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""
    # Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k
    return "+".join(reversed(out))

if __name__=="__main__":
	debug = 1
	lstrep = [('A',('A','aa','aA','Aa','AA','As')),('I',('I','ii','iI','Ii','II')),('U',('U','uu','uU','Uu','UU')),('F',('F','ff','fx','xf','Fx','xF','FF')),('e',('e','ea','ai','aI','Ai','AI')),('o',('o','oa','au','aU','Au','AU','aH','aHa','as')),('E',('E','ae','Ae','aE','AE')),('O',('O','ao','Ao','aO','AO')),('ar',('af','ar')),('d',('t','d')),('H',('H','s')),('S',('S','s','H')),('M',('m','M')),('y',('y','i','I')),('N',('N','M')),('Y',('Y','M')),('R',('R','M')),('n',('n','M')),('m',('m','M')),('v',('v','u','U')),('r',('r','s','H')),]
	dictionary = 'dicts/md.txt'
	if len(sys.argv) > 2:
		dictionary = 'dicts/'+sys.argv[2]+'.txt'
	if len(sys.argv) > 1:
		inputwords = [sys.argv[1]]
	if len(sys.argv) == 4:
		outfile = codecs.open(sys.argv[3],'w','utf-8')
		inputwords = preparation(sys.argv[1])
	global solutions
	solutions = {}
	if debug == 1:
		print 'Reading knownpairs', timestamp()
	knownpairs = readmwkey2()
	if debug == 1:
		print 'Calculating costs of dictionary headwords', timestamp()
	words = readwords(dictionary)
	wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words)) 
	#print sys.argv[2]+"cost =",
	#print wordcost
	if debug == 1:
		print 'Calculated costs of dictionary headwords', timestamp()
	maxword = max(len(x) for x in words)
	#print sys.argv[2]+"maxword =",
	#print maxword
	if debug == 1:
		print 'Calculated maxword', timestamp()
	counter = 0
	for inputword in inputwords:
		test = infer_spaces(inputword,dictionary)
		if any(a == inputword for (a,b) in knownpairs):
			if len(sys.argv) == 4:
				outfile.write(inputword+':'+inputword+':1\n')
			print inputword, '1'
		elif not re.search('[+]',test):
			if len(sys.argv) == 4:
				outfile.write(inputword+':'+inputword+':2\n')
			print inputword, '2'
		else:
			perm = [inputword]
			perm += permut(inputword,lstrep,words)
			print len(perm)
			print timestamp()
			output = []
			for mem in perm:
				split = infer_spaces(mem,dictionary)
				if split is not False:
					output.append(split)
			output = sorted(output,key=lambda x:x.count('+'))
			output = [member for member in output if not re.search('[+][^AsmMH][+]',member) and not re.search('[+][^mMsH]{1}$',member)] # Remove the splits which have single letter members.
			if len(output) == 1 and output == [inputword]:
				if len(sys.argv) == 4:
					outfile.write(inputword+':'+inputword+':3\n')
				print inputword, '3'
			elif len(output) == 0:
				if len(sys.argv)==4:
					outfile.write(inputword+':'+inputword+':4\n')
				print inputword, '4'
			else:
				if len(sys.argv) == 4:
					outfile.write(inputword+':'+output[0]+':5\n')
				print output[0:5], '5'
				#print output[0], '5'
	if debug == 1:
		print timestamp()
