
import os,sys,codecs,string
def punctnRem(text): 
		for punct in string.punctuation:
			text = text.replace(punct," ")
			words = text.encode('utf-8').split()
		return words
