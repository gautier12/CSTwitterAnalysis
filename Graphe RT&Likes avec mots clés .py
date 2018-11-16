from twitter_collect.twitter_connection_setup import *


def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    hashtag = file_path + "\\hashtag_candidate_" + str(num_candidate) +".txt"

    try:
        print(hashtag)
        hashtag_candidat = open(hashtag,'r')
        liste_hashtags = []
        for t in hashtag_candidat :
            liste_hashtags += t.split(' ')
        return liste_hashtags

    except IOError:
        print('Cannot open')



def graphe_tweets_mots_clefs(NumCandidat,filepath):
    """Retourne un dataframe avec les tweets contenant les mots clés stocké sur l'ordinateur"""
    connexion = twitter_setup()
    tweets = connexion.search('Emmanuel Macron',language="fr",rpp=50)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data


tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()
#Retourne l'évolution des RT et Likes des tweets contenants certains mots clés choisis
