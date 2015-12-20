from bisect import bisect_left
import codecs, re, datetime
# Function to return timestamp
def timestamp():
	return datetime.datetime.now()
def sanhw1():
	fin = codecs.open('../CORRECTIONS/sanhw1/sanhw1.txt','r','utf-8');
	lines = fin.readlines()
	output = []
	for line in lines:
		line = line.strip()
		split = line.split(':')
		word = split[0]
		dicts = split[1].split(',')
		output.append((split[0],dicts)) # Added a tuple of (word,dicts)
	return output

headwithdicts = sanhw1()

def hw1():
	global headwithdicts
	output = []
	for (word,dicts) in headwithdicts:
		output.append(word)
	return output
def onlyhw():
	fin = codecs.open('dicts/mwb.txt','r','utf-8');
	lines = fin.readlines()
	output = []
	for line in lines:
		line = line.strip()
		output.append(line)
	return output

print timestamp()
#hw = hw1()
hw = onlyhw()
hw = sorted(hw)
print timestamp()
def  sw(wordlist, word):
	word_fragment = word[:-1]
	inter = wordlist[bisect_left(wordlist, word_fragment):bisect_left(wordlist, word_fragment[:-1] + chr(ord(word_fragment[-1])+1))]
	return [member for member in inter if len(member) == len(word)]
startswith = sw(hw,'viS')
print startswith
"""
if 'aDISA' in startswith:
	print 'aDISA'
"""
print timestamp()
