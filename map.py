# -*- encoding: utf-8 -*- 
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

#inputsrc = open("twitterDoc.txt","r")
inputsrc = sys.stdin


d_keys1 = ['quote_count', 'reply_count', 'retweet_count', 'favorite_count']

def emit_string(d_key,llevel):
	if d_key in llevel:
		for htag in currentHashtag:
			print("%s\t%s\n" % (htag,str(llevel['quote_count'])))


count = 0
for line in inputsrc:
	line = line.strip('\n\r')
	if line=='' or len(line)<16:
		continue
	try:
		j_line = json.loads(line)
	except ValueError:
		continue
	currentHashtag = []
	if 'entities' in j_line.keys():
		if 'hashtags' in j_line['entities']:
			for htag in j_line['entities']['hashtags']:
				if htag['text'] != None:
					currentHashtag.append(htag['text'])
	if len(currentHashtag)==0:
		continue
	for desired_keys in d_keys1:
		emit_string(desired_keys,j_line)
	if 'retweeted_status' in j_line.keys():
		for desired_keys in d_keys1:
			emit_string(desired_keys,j_line['retweeted_status'])
	if 'quoted_status' in j_line.keys():
		for desired_keys in d_keys1:
			emit_string(desired_keys,j_line['quoted_status'])

inputsrc.close()
