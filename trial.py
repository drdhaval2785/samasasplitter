import itertools, timeit, datetime, sys
lstrep = [('A',('A','aa','aA','Aa','AA','As')),('I',('I','ii','iI','Ii','II')),('U',('U','uu','uU','Uu','UU')),('F',('F','ff','fx','xf','Fx','xF','FF')),('e',('e','ea','ai','aI','Ai','AI')),('o',('o','oa','au','aU','Au','AU','aH','aHa','as')),('E',('E','ae','Ae','aE','AE')),('O',('O','ao','Ao','aO','AO')),('ar',('af','ar')),('d',('t','d')),('H',('H','s')),('S',('S','s','H')),('M',('m','M')),('y',('y','i','I')),('N',('N','M')),('Y',('Y','M')),('R',('R','M')),('n',('n','M')),('m',('m','M')),('v',('v','u','U')),('r',('r','s','H')),]
lstrep1 = [('A',(('a','a'),('a','A'),('A','a'),('A','A'),('As',''))),('I',(('i','i'),('i','I'),('I','i'),('I','I'))),('U',(('u','u'),('u','U'),('U','u'),('U','U'))),('F',(('f','f'),('f','x'),('x','f'),('F','x'),('x','F'),('F','F'))),('e',(('e','a'),('a','i'),('a','I'),('A','i'),('A','I'))),('o',(('o','a'),('a','u'),('a','U'),('A','u'),('A','U'),('aH',''),('aH','a'),('as',''))),('E',(('a','e'),('A','e'),('a','E'),('A','E'))),('O',(('a','o'),('A','o'),('a','O'),('A','O'))),('ar',(('a','f'),)),('d',(('t',''),)),('H',(('s',''),)),('S',(('s',''),('H',''))),('M',(('m',''),)),('y',(('i',''),('I',''))),('N',(('M',''),)),('Y',(('M',''),)),('R',(('M',''),)),('n',(('M',''),)),('m',(('M',''),)),('v',(('u',''),('U',''))),('r',(('s',''),('H','')))]
dicti = 'dicts/mwb.txt'
dictionary = open(dicti).read().split()
def starts(word,list):
	output = {}
	upperrange = min(len(word),7)
	matched = [member for member in list if member.startswith(word[:3])]
	upperrange = len(word)
	for i in range(3,upperrange):
		output[i] = [member for member in matched if member.startswith(word[:i]) and len(member) < i+2]
	#return dict((k, v) for k, v in output.iteritems() if v)
	return output
def st1(word,list):
	output = []
	upperrange = min(len(word),7)
	matched = [member for member in list if member.startswith(word[:3])]
	upperrange = len(word)
	for i in range(3,upperrange):
		output += [member for member in matched if member.startswith(word[:i]) and len(member) < i+2]
	return output

def reps(letter,lstrep1):
	output = []
	for (a,lst) in lstrep:
		if len(lst) > 1:
			for (x,y) in lst:
				if letter == a:
					output.append(x+y)
		else:
			output.append(''.join(lst))
	return output

def permut(word):
	global lstrep1, dictionary
	# build output by applying each sub recorded
	out = []
	if word in dictionary:
		out.append(word)
	else:
		allowed = st1(inputword,dictionary)
		dictset = set(dictionary)
		input_str = word
		subs = []
		for i, c in enumerate(input_str):
			for (a,b) in lstrep1:
				if c == a:
					subs.append( (i, (a,b)))
		allowed = sorted(allowed, key=lambda x:len(x), reverse=True)
		for allow in allowed:
			entry = [entr for (a,(b,entr)) in subs if a==len(allow)-1]
			if len(entry) > 0:
				eligentries =  [(a,b) for (a,b) in entry[0] if allow[-1]==a]
				if len(eligentries) > 0:
					for eligen in eligentries:
						out.append((len(allow), allow[:-1]+eligen[0], eligen[1]+word[len(allow):]))
	return out
if __name__=="__main__":
	print datetime.datetime.now()
	inputword = sys.argv[1]
	print permut(inputword)
	print datetime.datetime.now()
	