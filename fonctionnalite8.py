from textblob import TextBlob
from textblob import Word
from twitterPredictor.Sprint1 import *

import pandas as pd


stop_words = ['CC','DT','EX','IN','POS','PRP','TO','UH','WDT','WP','WP$','WRB']

def texte_tweets():
   """Retourne un dataframe avec les tweets contenant les mots clés stocké sur l'ordinateur"""
   connexion = twitter_setup()
   tweets = connexion.search('Emmanuel Macron',language="fr",rpp=50)
   data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
   resultat = ''
   for tweet in tweets :
       resultat += tweet.text
   return(resultat)

def arobase(mot):
    return mot[0]!= '@'

def liste_en_texte(l):
   text = ''
   for mot in l :
       text += ' ' + mot
   return(text)

tweets_studied = texte_tweets()

def extraction_vocabulaire(tweets_under_study) :
    """
    Extraire le vocabulaire d'un ensemble de tweets en récupérant les mots uniques et lemmatisés.
    Supprimer de la liste obtenue les mots fréquents ou stop-words.
    :param tweets : ensemble des tweets à analyser
    :return: liste des mots uniques lemmatisés
    """
    tweet_tb = TextBlob(tweets_under_study)
    tweets = []
    for couple in tweet_tb.tags :
        (mot,tag) = couple
        if arobase(mot) and tag not in stop_words :
            tweets.append(mot)
    tweets_sous_forme_de_string = liste_en_texte(tweets)
    tweets_tb = TextBlob(tweets_sous_forme_de_string)
    mots = tweets_tb.words
    lemmatized_words = []
    for mot in mots :
        if tweets_tb.words.count(mot) == 1 :
            mot = Word(mot)
            mot.lemmatize()
            lemmatized_words.append(mot)
    return lemmatized_words


#print(extraction_vocabulaire(tweets_studied))
