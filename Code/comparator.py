def comparator(ngramdict1, ngramdict2):
    final_dict = dict()
    for file1_iter,file1_ngram_iter in ngramdict1.iteritems():
        commonlist = []
        for file2_iter,file2_ngram_iter in ngramdict2.iteritems():
            similar = [i for i in file1_ngram_iter if i in file2_ngram_iter]
            length_similar = len(similar)
            length_total = len(file1_ngram_iter) + len(file2_ngram_iter)
            similarity = length_similar/length_total
            commonlist.append(similarity)
        highest_similar = commonlist.sort(reverse = True)[0]
        final_dict[file1_iter] = highest_similar
    sum_total = sum(final_dict.itervalues())
    count = len(final_dict)
    perc_similarity = sum_total/count
    return perc_similarity
    



