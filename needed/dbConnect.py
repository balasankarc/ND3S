# -*- coding: utf-8 -*-
#!/usr/bin/python

import os,sys,codecs,string,MySQLdb


db = MySQLdb.connect(host="localhost", #host name
		             user="root", # username
		              passwd="root", # password
		              db="malayalam",
			      charset="utf8") # name of the data base
cur = db.cursor()
def valid(word):
	count=cur.execute(u'SELECT w.id FROM word w WHERE w.word =%s',word)	
	return count

def splitPrefix(word):
	count=cur.execute(u'SELECT w.id FROM word w WHERE w.word like %s', word+'%' )	
	return count

def splitSuffix(word):
	count=cur.execute(u'SELECT w.id FROM word w WHERE w.word like %s', '%'+word )	
	return count

def getWord(word):
	count=cur.execute(u'SELECT w.word FROM word w WHERE w.word like %s','%' + word )	
	return count



