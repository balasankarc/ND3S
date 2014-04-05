# -*- coding: utf-8 -*-


def stem(text):
    rulesDict = None
    rulesDict = LoadRules()
    words = text.split(" ")
    word_count = len(words)
    root_list = list()
    word_iter = 0
    while word_iter < word_count:
        found = 0
        current_word = words[word_iter]
        word_length = len(current_word)
        suffix_pos_itr = 2
        word_stemmed = ""
        while suffix_pos_itr < word_length:
            suffix = current_word[suffix_pos_itr:word_length]
            if suffix in rulesDict:
                found = 1
                key = suffix
                word_stemmed = current_word[0:suffix_pos_itr] + rulesDict[key]
                if ' ' in word_stemmed:
                    stemlist = word_stemmed.split(' ')
                    root_list += stemlist
                else:
                    root_list.append(word_stemmed)
                break
            suffix_pos_itr += 1
        if found == 0:
            root_list.append(current_word)
        word_iter += 1
    return root_list


def LoadRules():
    rulefile = open('inflection.rules', 'r')
    rules_dict = dict()
    a = rulefile.read()
    a = a.split('\n')
    del a[-1]
    for i in a:
        if "#" in i:
            continue
        b = i.split("=")
        try:
            lhs = b[0]
            rhs = b[1]
            rules_dict[lhs] = rhs
        except:
            print "Exception in loadrules"
            continue
    rulefile.close()
    return rules_dict
