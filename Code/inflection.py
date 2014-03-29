# -*- coding: utf-8 -*-


import codecs

out = codecs.open("asdf.txt","w",encoding = "utf-8")


def stem(text):
  rulesDict = None
  if rulesDict == None:
    rulesDict = LoadRules()
  #print rulesDict
  #text = text.strip()
  words = text.split(" ")
  #print words[0]
  for i in words:
    print i
  word_count = len(words)
  result_dict = dict()
  word_iter = 0
  word = ""
  while word_iter < word_count:
    word = words[word_iter]
    if word[-1]== '\n':
      word = word[:-1]
    print list(word)
    if('+' not in word):
      word_length = len(word)
      suffix_pos_itr = 2
      word_stemmed = ""
      while suffix_pos_itr < word_length:
        suffix = word[suffix_pos_itr:word_length]
        #suffix =  suffix[:-1]
        print suffix
        if suffix.encode("utf-8") in rulesDict:
          print "Here:"
          key = suffix.encode("utf-8")
          word_stemmed = word[0:suffix_pos_itr]+ rulesDict[key].decode("utf-8")
          #out.write(word_stemmed+" ")
          break;
        suffix_pos_itr = suffix_pos_itr+1
      if(word_stemmed == ""):
        word_stemmed = word
      result_dict[word] = word_stemmed
    else:
      result_dict[word] = word
    word_iter = word_iter+1
    out.write(word_stemmed+" ")
  for key,values in result_dict.iteritems():
    print values
  return result_dict

def LoadRules():
  rulefile = open('inflection.rules','r')
  rules_dict = dict()
  a = rulefile.read()
  a = a.split('\n')
  del a[-1]
  for i in a:
    #print i
    if "#" in i:
      continue
    b = i.split(" = ")
    # print "b = "
    #print b
    #raw_input()
    lhs = b[0]
    rhs = b[1]
    rules_dict[lhs]= rhs
    #print lhs
    #print rhs
  return rules_dict

#a = open("text.txt","r")
#txt = a.read().decode("utf-8")
#b = stem(txt)
