# -*- coding: utf-8 -*-
"""
python dcsdictbuilder.py inputfile outputfile
"""
import sys, re
import codecs

def striptags(string):
	string = string.replace('\t','')
	return re.sub('<[^>]*>','',string)
if __name__=="__main__":
	inputfile = sys.argv[1]
	outputfile = sys.argv[2]
	fin = codecs.open(inputfile,'r','utf-8')
	fout = codecs.open(outputfile,'w','utf-8')
	attributetypes = set()
	for line in fin:
		if 'http://kjc-sv013.kjc.uni-heidelberg.de/dcs/index.php?contents=lemma' in line:
			[word1,occurrence,scrap] = line.split('</td>')
			[word,attribute] = word1.split('</a>')
			word = striptags(word)
			occurrence = striptags(occurrence)
			occurrence = occurrence.split(' ')[0]
			attribute = attribute.strip(' ()')
			attributetypes.add(attribute)
			if attribute in set(['mfn','nr','mf','fn','mn','adj','m','n','f']) and int(occurrence) > 1:
				fout.write(word+'\n')
	for member in attributetypes:
		print member.encode('utf-8')
	fin.close()
	fout.close()