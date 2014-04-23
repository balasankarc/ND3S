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
    line1cnt = 1
    for file1_iter,file1_ngram_iter in ngramdict1.iteritems():
        commonlist = []
        line2cnt = 1
        for file2_iter,file2_ngram_iter in ngramdict2.iteritems():
            similar = [i for i in file1_ngram_iter if i in file2_ngram_iter]
            #print similar
            length_similar = len(similar)
            print "Length = " + str(length_similar)
            combined_list = file1_ngram_iter + file2_ngram_iter
            combined_list = uniq(combined_list)
            #print "Combined list"
            #print combined_list
            print "Line #" + str(line1cnt) + " with Line #" + str(line2cnt)
            length_total = len(combined_list)
            print "Length Total = " + str(length_total)
            if length_total == 0:
                line2cnt += 1
                continue
            else:
                similarity = round(decimal.Decimal(float(length_similar)/length_total),4) * 100
                print "Similarity = " + str(similarity)
                commonlist.append(similarity)
                line2cnt += 1
        commonlist.sort(reverse = True)
        #print commonlist
        highest_similar = commonlist[0]
        final_dict[file1_iter] = highest_similar
        line1cnt += 1
        print "Highest Similarity = " + str(highest_similar)
    sum_total = sum(final_dict.itervalues())
    count = len(final_dict)
    perc_similarity = round(decimal.Decimal(float(sum_total)/count),2)
    return perc_similarity
