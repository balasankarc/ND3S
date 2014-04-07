import decimal

def uniq(lst):
    a = list()
    length = len(lst)
    for i in range(0,length):
        item = lst[i]
        if item not in lst[i+1:length]:
            a.append(item)
    return a

def comparator(ngramdict1, ngramdict2):
    final_dict = dict()
    for file1_iter,file1_ngram_iter in ngramdict1.iteritems():
        commonlist = []
        for file2_iter,file2_ngram_iter in ngramdict2.iteritems():
            similar = [i for i in file1_ngram_iter if i in file2_ngram_iter]
            print similar
            length_similar = len(similar)
            print "Length = " + str(length_similar)
            combined_list = file1_ngram_iter + file2_ngram_iter
            combined_list = uniq(combined_list)
            print "Combined list"
            print combined_list
            length_total = len(combined_list)
            print "Length Total = " + str(length_total)
            similarity = round(decimal.Decimal(float(length_similar)/length_total),4) * 100
            print "Similarity = " + str(similarity)
            commonlist.append(similarity)
        commonlist.sort(reverse = True)
        print commonlist
        highest_similar = commonlist[0]
        final_dict[file1_iter] = highest_similar
    sum_total = sum(final_dict.itervalues())
    count = len(final_dict)
    perc_similarity = sum_total/count
    return perc_similarity
