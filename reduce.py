# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

inputsrc = sys.stdin
#inputsrc = open("mapped.txt","r",encoding='utf-16-le')
htagcount = {}
for line in inputsrc:
	line = line.strip('\n\ufeff').split('\t')
	if len(line)==1:
		continue
	if line[0] not in htagcount:
		htagcount[line[0]] = 0
	try:
		htagcount[line[0]] += int(line[1])
	except ValueError:
		pass
	else:
		continue

htagcountlist = []

for item in htagcount:
	htagcountlist.append((item,htagcount[item]))
htagcountlist.sort(key=lambda item: item[1],reverse=True)
for item in htagcountlist:
	print('%s\t%s\n' % (item[0],item[1]))
	
