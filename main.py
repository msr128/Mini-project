import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open('read.txt', encoding='utf-8').read()
lower_text = text.lower()
cleaned_text = lower_text.translate(str.maketrans('', '', string.punctuation))
token_words = word_tokenize(cleaned_text, "english")



def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative")
    elif pos > neg:
        print("Positive")
    else:
        print("Neutral")




sentiment_analyse(cleaned_text)