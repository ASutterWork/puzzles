#!/usr/bin/env python

human = [1,6,25,11,3,10,3,13,12]
goon = [3,22,3,1,19,18,7,13,12]
speaker = [11,7,12,7,25,18,19,16,3]
vals = {
	1:'a',
	2:'b',
	3:'c',
	4:'d',
	5:'e',
	6:'f',
	7:'g',
	8:'h',
	9:'i',
	10:'j',
	11:'k',
	12:'l',
	13:'m',
	14:'n',
	15:'o',
	16:'p',
	17:'q',
	18:'r',
	19:'s',
	20:'t',
	21:'u',
	22:'v',
	23:'w',
	24:'x',
	25:'y',
	26:'z'}

def printrot(text, key):
	for i in range(0,25):
		res = ""
		for j in text:
			res += vals.get((i+j)%26+1,str(i+j))
		print res

print 'human'
printrot(human, vals)
print ''
print 'goon'
printrot(goon, vals)
print ''
print 'speaker'
printrot(speaker, vals)
