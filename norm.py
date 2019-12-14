# -*- encoding: utf-8 -*-

htagcount = {}


def increment(filename,data_size):
	f = open(filename,"r",encoding='utf-8')
	for line in f:
		line = line.strip('\n\ufeff').split('\t')
		if line[0]=='' or line[1]=='':
			continue
		if line[0] not in htagcount:
			htagcount[line[0]] = 0
		norm_p = float(line[1])/(data_size/1024)
		htagcount[line[0]]+=norm_p
	f.close()
	
increment("result_Dec10/part-00000",3034234880)
increment("result_Dec11/part-00000",2748567552)
increment("result_Dec12/part-00000",17844625408)
increment("result_Dec12_2/part-00000",2503872512)


htagcountlist = []
buf = ''

for item in htagcount:
	htagcountlist.append((item,htagcount[item]))
htagcountlist.sort(key=lambda item: item[1],reverse=True)
for item in htagcountlist:
	buf += (item[0] + '\t' + str(item[1]) + '\n')

f = open("ave.txt","w")
f.write(buf)
f.close()