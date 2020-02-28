def cntWordOccur(sentences, word):
    list_of_words = sentences.split()
    count = 0
    for i in list_of_words:
        if i == word:
            count +=1
    return count
    
