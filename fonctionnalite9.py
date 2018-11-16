from textblob import TextBlob

tweets = ["negative","hatred","pessimism"]

def opinion_surcandidat(liste_tweets) :
   """ A partir d'une liste de tweet ce programme retourne 3 listes contenant respectivement les tweets positifs négatif et neutre"""
   tweets_pos = []
   tweets_neg = []
   tweets_neutr = []
   for tweet in liste_tweets :
       blob = TextBlob(tweet)
       if blob.sentiment.subjectivity > 0.45 :
           break
       elif blob.sentiment.polarity > 0.33 :
           tweets_pos.append(tweet)
       elif blob.sentiment.polarity < -0.33 :
           tweets_neg.append(tweet)
       else :
           tweets_neutr.append(tweet)
    return (tweets_pos,tweets_neutr,tweets_neg)

(pos_tweets,neu_tweets,neg_tweets) = opinion_surcandidat(tweets)

print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(tweets)))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(tweets)))
print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(tweets)))



