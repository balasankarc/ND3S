# -*- coding: utf-8 -*-
#!/usr/bin/python

import os,sys,codecs,string
import hyphen,punctn,plural,dbConnect,inflection

def getInput(inputFile):
	inpt=codecs.open(inputFile,encoding='utf-8', errors='ignore').read()
	return inpt

def writeOutput(outputFile,words):
	op=open(outputFile, "w")
	for index in range(len(words)):
		words[index]=unicode(words[index],encoding='utf-8', errors='ignore')
		op.write(words[index].encode("UTF-8"))
		op.write(" ")


def standardize(inpt):
	#remove hyphenation
	inputFile=getInput(inpt)
	partOp1=hyphen.hyphenRem(inputFile)
	writeOutput('afterHyph.txt',partOp1)

	#remove punctuation
	inputFile=getInput('afterHyph.txt')
	partOp2=punctn.punctnRem(inputFile)
	writeOutput('aftrPunctn.txt',partOp2)

	# mark Valid Words
	inputFile=getInput('aftrPunctn.txt')
	words = inputFile.split()
	f=open('valid.txt', "w")
	for index in range(len(words)):
		count = dbConnect.valid(words[index])
		if(count>0):	
			f.write("+")
		f.write(words[index].encode("UTF-8"))
		f.write(" ")
		
	#handle inflections
	inputFile=getInput('valid.txt')
	partOp3=inflection.stem(inputFile);
	f=open('infl.txt', "w")
	words=inputFile.split(" ")
	word_count=len(words)       
	word_iter=0
	word=""
	while word_iter < word_count:
		    
		    word = words[word_iter]
		    word= word.strip('!,.?:')
		    word_length = len(word)
		    word_iter = word_iter+1
		    f.write(partOp3[word].encode("UTF-8"))
		    f.write(" ")
	f.close()
	
	# mark Valid Words
	inputFile=getInput('infl.txt')
	words = inputFile.split()
	f=open('valid.txt', "w")
	for index in range(len(words)):
		if('+' not in words[index]):
			count = dbConnect.valid(words[index])
			if(count>0):	
				f.write("+")
			f.write(words[index].encode("UTF-8"))
			f.write(" ")
		else:
			f.write(words[index].encode("UTF-8"))
			f.write(" ")
			
	#handle compound words

			
	return 'valid.txt'
