# -*- coding: utf-8 -*-
import sys, re
import codecs
import string
import datetime
import itertools

# Function to return timestamp
def timestamp():
	return datetime.datetime.now()

def triming(lst):
	output = []
	for member in lst:
		member = member.strip()
		output.append(member)
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
#createhwlist('MD')
def readwords(dictionary):
	return open(dictionary).read().split()
	
def unique(lst):
	output = []
	for member in lst:
		if member not in output:
			output.append(member)
	return output

# Asked the procedure at http://stackoverflow.com/questions/34108900/optionally-replacing-a-substring-python
def permut(word,lstrep,dictionary):
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
		for i, cc in sub:
			input_list[i] = cc
		out.append(''.join(input_list))
	out = unique(out)
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
from math import log

def infer_spaces(s,dictionary):
    words = open(dictionary).read().split()
    wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words)) 
    maxword = max(len(x) for x in words)
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
    out = reversed(out)
	# Alteration in the code to give only exact match.
    reply = ''
    for member in out:
        if member in words:
            reply += member+"+"
        else:
            reply = False
    if reply is not False:
        reply = reply.rstrip('+')
    return reply
    #return "+".join(reversed(out))
	
if __name__=="__main__":
	lstrep = [('A',('A','aa','aA','Aa','AA')),('I',('I','ii','iI','Ii','II')),('U',('U','uu','uU','Uu','UU')),('F',('F','ff','fx','xf','Fx','xF','FF')),('e',('e','ea','ai','aI','Ai','AI')),('o',('o','oa','au','aU','Au','AU','aH','aHa')),('E',('E','ae','Ae','aE','AE')),('O',('O','ao','Ao','aO','AO'))]
	dictionary = 'dicts/MD.txt'
	if len(sys.argv) == 3:
		dictionary = 'dicts/'+sys.argv[2]+'.txt'
	inputword = sys.argv[1]
	words = readwords(dictionary)
	global solutions
	solutions = {}
	perm = permut(sys.argv[1],lstrep,words)
	output = []
	for mem in perm:
		split = infer_spaces(mem,dictionary)
		if split is not False:
			output.append(split)
	output = sorted(output,key=len)
	print output[:5]
