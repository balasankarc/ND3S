# -*- coding: utf-8 -*-

import inflection
import ngrams


def sentencer():
    in1 = open("text.txt", "r")
    content = str(in1.read())
    txt = ' '.join(content.split())
    txt = content.split(".")
    root_dict = dict()
    linecounter = 1
    for i in txt:
        currentline = i.strip()
        root_list = inflection.stem(currentline)
        root_dict[linecounter] = root_list
        linecounter += 1
    in1.close()
    for linenumber, rootlist in root_dict.iteritems():
        print "Line Number : " + str(linenumber)
        print "Number of words = " + str(len(rootlist))
        ngram = ngrams.ngrams(rootlist, 2)
        for item in ngram:
            for i in item:
                print i
        print ""

sentencer()
