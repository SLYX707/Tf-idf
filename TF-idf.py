if __name__ == '__main__':
    ## Feature generation
    import os
    import codecs
    from nltk.stem.porter import *
    import math
    import numpy as np

    # Read the stop words from the 'stopwords.txt'
    # (I read the stopwords fist is because next two big loops will use it)
    stop_path = 'D:/pythonProject/stopwords'
    readstopwordFile = []
    stopwords = codecs.open('stopwords.txt', 'r', 'Latin1')
    stopwords = [''.join(s for s in k if s.isalpha()) for k in stopwords.read().split()]
    print(len(stopwords)) # Check the length of the stopwords
    print(stopwords[0:5])

    # Read the name of 5 subdirectories in dataset
    path = 'D:/pythonProject/dataset'
    file1 = []
    for i in os.listdir(path):
        file1.append(i)

    # Read all the text in the documents, form a list with 2726 sub lists in it.
    file2 = []
    nestlist = []
    file_count = 0
    for k in range(0, 5):  # 5 loops for 5 subdirectories
        path2 = 'D:/pythonProject/dataset/' + file1[k]
        for file3 in os.listdir(path2):
            fname = path2 + '/' + file3   # Get each path for every document
            with open(fname, "r", encoding='utf-8') as f:
                f = codecs.open(fname, 'r', encoding='Latin1') #  Read all the text into variable 'data'
                word = f.read()
                words_clean_lower = re.sub(r'[^a-z]', ' ', word.lower()).strip() # Split the document text into words and convert to lower case form
                words_clean_lower = words_clean_lower.split() # Split the text into words
                # Remove the stopwords from the list
                word_nostops = []
                for word_nostop_single in words_clean_lower:
                    if word_nostop_single not in stopwords:
                        word_nostops.append(word_nostop_single)
                # Remove word suffix
                stemmer = PorterStemmer()
                word_final = [stemmer.stem(word_nostop) for word_nostop in word_nostops]
                nestlist.append(word_final)
    # Check the the nestlist
    print(len(nestlist))
    #print(nestlist[0:1])

    # This part is for the unique word of the whole datasets.
    function = lambda x: [y for k in x for y in function(k)] if type(x) is list else [x]
    word_final = function(nestlist)
    unique_word = set(word_final) # Remove repetitive words using set(), get the unique words.
    unique_word = sorted(unique_word) # Rearrange them alphabetically(a-z).
    print(len(unique_word)) # Check unique_word

    # fik
    fik = []
    for i in range(0, 2726):
        row_frequency = []
        for j in range(0, 23130):
            frequency = nestlist[i].count(unique_word[j])
            row_frequency.append(frequency)
        fik.append(row_frequency)
    print(len(fik))

    #nk
    nk = []
    for i in range(0,23130):
        a = 0
        for j in range(0,2726):
            check = 0
            check = nestlist[j].count(unique_word[i])
            if check > 0:
                a += 1
        nk.append(a)
    print(len(nk))
    print(nk)

    #aik
    aik = []
    print(k)
    for i in range(0, 2726):
        t=[]
        t= [math.log(2726/q) for q in nk]
        a = np.multiply(np.array(fik[i]),np.array(t))
        aik.append(a)
    aik = np.array(aik)
    print(aik[0:1])

    #Aik
    A=[]
    for i in range(0, 2726):
        b = float(sum([c * c for c in aik[i]]) ** 0.5)
        A_row = [q/b for q in aik[i]]
        A.append(A_row)
    A = np.array(A)
    print(A[0:1])
    np.savez('train-20ng.npz', X=A)
    matrix = np.load('train-20ng.npz')











































