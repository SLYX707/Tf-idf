# Tf-idf


## Introduction
  
Tf-idf represents "term frequency – Inverse Document Frequency" which is a numeric statistic that intended to reflect the importance of a word in the collection or corpus and is calculated by the equation: Term Frequency (TF) * Inverse Document Frequency (IDF). This method is a widely used technique all over the world in information retrieval and text mining.

## Design & Implementation
A represents a collection of documents which are represented by a document-by-word matrix.
A = (aik) 
N = the number of documents in the dataset
fik represents the frequency of word k in document i.
fik = number of words appears in document I / the length of document i
nk represents the total number of times word k occurs in the dataset.
nk = whether the word appear in the document, if appeared, the count plus one / the number of all the documents in the dataset(N)
aik = fik * log(N/nk)
Aik = aik/sqrt(aij^2)

## Test

### 1.1 read the text files from 5 sub directions in dataset
Using os.listdir function to read the paths from the documents.
 

### 1.2 split the document text into words
Secondly, I use the subpath to output all the txt document and gathered them into the list subfile. The length of this list is the same number of all the txts which is 2726.
 

### 2. remove the stopwords & convert words into their lower cases form & delete all non-alphabet characters from the text
First, I input the stop words from the path and store them in the ‘stopwords’
 
 
Then I choose to transfer the file in to lower cases and remove the non-alphabet words in advance.
 
After that I create the nostopwords list to store the out come of the removed file.
By using the if and for function to choose the word that not in the stopwords file and gather.
 

### 3. Stemmer
Then come to the third process, using the nltk package and store the file result in the singles list.


### 4.1 the outcomes of N
To calculate the TFIDF, there is a few things should be calculated:
Firstly, is the N, which is the # of all the documents, this can be figured out.

### 4.2 calculate idf/nk: the total number of times word K occurs in the dataset
Then, calculating the DF which is also called Nk in the task sheet, and is the the total number of times word k occurs in the dataset called the document frequency.
 
Create dic DF. For I in 0-2726, if the word does exist in the txt then the count will add 1, otherwise the count will not change. 
 
 
Moreover, through this DF we can also get the outcome that there are 23130 unique words in the txt file.
 
Then I calculate the idf in this step, by the equation that idf = log(N/nk)
 
 

### 4.3 calculate tf/fik: the frequency of word k in document I
By using the uniquewords, we can quickly get through all the files. And do the calculation that the number of K which appeared in one document / the length of the document to get the frequency.
 

### 4.4 Calculating the aik(A)
For the equation that aik = idf * tf. The code is at below. The two For loop is to take the number from each sublist in the tf out to do the calculation.
 
### 4.5 Calculating the Aik(the final result)
Firstly, the total sum is calculated and then it is used to do the final calculation.By taking out the number from the 2726 sublist and do the calculation.
 
By giving out 4 list and fill in the blankest, the result for the first sublist were in the PDF file.

## Conclusion
In conclusion, there is no denying that stemmer is a useful package to arrange the documents and td-idf is a powerful method to see the word frequency. By rearranging these tests, we can get better understanding on the weight to each word in the document and corpus. 

0.060085
##  P.S.More details are available in the PDF file
