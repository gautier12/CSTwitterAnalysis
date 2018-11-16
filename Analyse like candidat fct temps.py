from tweet_analysis.create_dataframe import *
import matplotlib.pyplot as plt

# DEUXIÈME FONCTION D'ANALYSE


def dataframe_activite_candidate():
   #Créer un dataframe avec les 200 derniers tweets d'un candidat
   connexion = twitter_setup()
   tweets = connexion.user_timeline(id = num_candidate, count = 200)
   data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
   data['len']  = np.array([len(tweet.text) for tweet in tweets])
   data['ID']   = np.array([tweet.id for tweet in tweets])
   data['Date'] = np.array([tweet.created_at for tweet in tweets])
   data['Source'] = np.array([tweet.source for tweet in tweets])
   data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
   data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
   return data

data2 = dataframe_activite_candidate()

tfav2 = pd.Series(data = data2['Likes'].values, index = data2['Date'])

# Likes visualization:
tfav2.plot(figsize=(16,4), label="Likes", legend=True)

plt.show()

##Retourne le nombre de likes des posts d'un candidat en fonction du temps
