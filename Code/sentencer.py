# -*- coding: utf-8 -*-

import inflection
import ngrams


def sentencer(inpfile):
    in1 = open(inpfile,"r")
    content = str(in1.read())
    #txt = ' '.join(content.split())
    txt = content.split(".")
    del(txt[-1])
    root_dict = dict()
    ngram_dict = dict()
    linecounter = 1
    for i in txt:
        currentline = i.strip()
        #print "Current Line : " + currentline
        root_list = inflection.stem(currentline)
        root_dict[linecounter] = root_list
        linecounter += 1
    in1.close()
    for linenumber, rootlist in root_dict.iteritems():
        #print "Line Number : " + str(linenumber)
        #print "Number of root words = " + str(len(rootlist))
        ngram = ngrams.ngrams(rootlist, 1)
        ngram_dict[linenumber] = ngram
    return ngram_dict

