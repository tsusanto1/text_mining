
########## Text analysis and Sentiment by Theresia Susanto & Josephine Boenawan ###########
# WARNING: running this program takes around 2 minutes and 45 seconds.
import urllib.request
import string
import math
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


tale_of_two_cities = 'http://www.gutenberg.org/files/98/98-0.txt'
great_expectations = 'http://www.gutenberg.org/files/1400/1400-0.txt'
oliver_twist = 'http://www.gutenberg.org/cache/epub/730/pg730.txt'

def url_text(url):
    """ Downloads and reads the text
    url = link to the text file
    returns a ing of text
    """
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    return text
#print(text) # for testing

def process_file(text, skip_header):
<<<<<<< HEAD
    """hello"""
=======
    """
    text: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: dictionary from each word to the number of times it appears.
    """
>>>>>>> origin/master
    dic = {}


    #text = text.lower()
    if skip_header:
        text = skip_gutenberg_header_and_tail(text)
    text = text.lower()
    text = remove_stopwords(text)

    for i in text:
        i = i.replace("--","  ")
        i = i.replace("/"," ")
        new_i = i.split()
        for j in new_i:
            while(len(j) > 0 and not(j[0].isalnum())):
                j = j[1:]
            while(len(j) > 0 and not(j[-1].isalnum())):
                j = j[:-1]

            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1
    del dic['']
    return dic

def skip_gutenberg_header_and_tail(text):
    """Reads from text until it finds the start and end of processed text.
    text: open file object
    Returns a string of text without the header and tail. 
    """
    start = 'Chapter XV     The Footsteps Die Out For Ever'
    i = text.find(start)
    end = 'End of the Project Gutenberg EBook of A Tale of Two Cities, by Charles Dickens'
    j = text.find(end)

    return text[i+len(start):j]

def remove_stopwords(text):
    """Removes stopwords defined by nltk program
    text = open file object
    returns a filtered string without stopwords
    """
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(text)
 
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
    return filtered_sentence

def sentiment_analysis(text):
    """ Returns sentiment analysis score 
    text = string of processed text
    """
    return SentimentIntensityAnalyzer().polarity_scores(skip_gutenberg_header_and_tail(text))
    
    

def freq_of_words_in_order(dic):
    """ returns a 
    """
    frequency = dic.values()
    words = dic.keys()
    return sorted(list(zip(frequency,words)), reverse=True)

def print_top_50(dic, title):
    tup_word = freq_of_words_in_order(dic)
    if title == "TalesDat": 
        print(" A Tale of Two Cities")
    elif title == "GreatExpDat":
        print("\n Great Expectations")
    elif title == "OliverDat":
        print("\n Oliver Twist")
    print("Word","\t","Frequency")
    for i in range(0,50):
        print("{0:10}    {1}".format(tup_word[i][1], tup_word[i][0]))

def innerProduct(dictA, dictB):
    num = 0
    for word in dictA:
        if word in dictB:
             num += dictA[word]*dictB[word]
    return num

def docDist(dictA, dictB):
    num = innerProduct(dictA, dictB)
    denom = math.sqrt(innerProduct(dictA,dictB)*innerProduct(dictB,dictB))
    return (math.acos(num/denom))/(math.pi/2)*100

def main():
    txt = url_text(tale_of_two_cities)
    txt1 = url_text(great_expectations)
    txt2 = url_text(oliver_twist)
    TalesDat = process_file(txt, skip_header=True)

    no_stopwords = ' '.join(remove_stopwords(skip_gutenberg_header_and_tail(txt)))
    
    TaleofTwoCities = sentiment_analysis(no_stopwords)
    GreatExpDat = process_file(txt1, skip_header=True)
    OliverDat = process_file(txt2, skip_header=True)
     
    no_stopwords = ' '.join(remove_stopwords(skip_gutenberg_header_and_tail(txt1)))
    GreatExpectations = sentiment_analysis(no_stopwords)
    no_stopwords = ' '.join(remove_stopwords(skip_gutenberg_header_and_tail(txt2)))
    OliverTwist = sentiment_analysis(no_stopwords)
    
    print_top_50(TalesDat, "TalesDat")
    print("Sentiment analysis of Tale of Two Cities is",TaleofTwoCities)
    print_top_50(GreatExpDat, "GreatExpDat")
    print("Sentiment analysis of Great Expectations is",GreatExpectations)
    print_top_50(OliverDat, "OliverDat")
    print("Sentiment analysis of Oliver Twist is",OliverTwist)
    print("------------------------------------")
    
    print ("The difference between A Tale of Two Cities and Great Expectations is {:.2f}%".format(docDist(TalesDat,GreatExpDat)))
    print ("The difference between A Tale of Two Cities and Oliver Twist is {:.2f}%".format(docDist(TalesDat, OliverDat)))
    print ("The difference between Oliver Twist and Great Expectations is {:.2f}%".format(docDist(OliverDat,GreatExpDat)))

    

if __name__ == '__main__':
    main()