import os,sys,codecs,string

def hyphenRem(inpt):
	words=inpt.encode('utf-8').split()
	for index in range(len(words)):
	   if (len(words[index])!=0 and "-" in words[index][-1] ) :
	   	words[index]=words[index]+words[index+1]
		words[index] =words[index].replace('-',"")
		words[index+1]=""
	return words
