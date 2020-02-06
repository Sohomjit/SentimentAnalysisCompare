# -*- coding: utf-8 -*-
"""vaderSentiment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FV1ypkh0p6jqkB2lo03wo09jv0wb-vs7
"""

!pip install nltk
!pip install vaderSentiment

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence): 
  
    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 
  
    # polarity_scores method of SentimentIntensityAnalyzer 
    # oject gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
      
    print("Overall sentiment dictionary is : ", sentiment_dict) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
  
    print("Sentence Overall Rated As", end = " ") 
  
    # decide sentiment as positive, negative and neutral 
    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive") 
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative") 
  
    else : 
        print("Neutral")

#@title Enter Text For Analysis
first_line = "Wonderful day it is !" #@param {type:"string"}
second_line = "I just hate my life !" #@param {type:"string"}
third_line = "Ok it seems I will Live this time !" #@param {type:"string"}

if __name__ == "__main__" : 
  
    print("\n1st statement :") 
    print(first_line)
    # function calling 
    sentiment_scores(first_line) 
  
    print("\n2nd Statement :") 
    print(second_line)
    # function calling 
    sentiment_scores(second_line) 
  
    print("\n3rd Statement :") 
    print(third_line)
    # function calling 
    sentiment_scores(third_line)

