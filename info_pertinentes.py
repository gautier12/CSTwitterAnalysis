import numpy as np

def max_RT(data) :
   """
   Extrait le tweet qui a le plus de mention de RT et renvoie le nombre maximal de RT
   :param data : the dataframe with the tweets under study
   :return: nombre max de RT
   """
   rt_max  = np.max(data['RTs'])
   rt  = data[data.RTs == rt_max].index[0]

   # Max RTs:
   print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
   print("Number of retweets: {}".format(rt_max))
   print("{} characters.\n".format(data['len'][rt]))
   return(rt_max)


def n_meilleurstweets_RT(data,n):
   """
   Renvoie les n meilleurs tweets
   :param data : the dataframe with the tweets under study
   :return: nombre max des n meilleurs RT
   """
   (i,j) = np.shape(data)
   if n > 0 and n < i :
      rt_max = max_RT(data)
      np.delete(data,data.RTs==rt_max,axis = 0 )




def max_Likes(data) :
   """
    Extrait le tweet qui a le plus de likes et renvoie le nombre maximal de likes
    :param data : the dataframe with the tweets under study
    :return: nombre max de likes
    """
    like_max  = np.max(data['Likes'])
    like  = data[data.Likes == like_max].index[0]

    # Max RTs:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][like]))
    print("Number of retweets: {}".format(like_max))
    print("{} characters.\n".format(data['len'][like]))
    return(like_max)



def n_meilleurstweets_like(data,n):
    """
   Renvoie les n meilleurs tweets selon le nombre de like
   """
    (i,j) = np.shape(data)
    if n > 0 and n < i :
        like_max = max_Likes(data)
        np.delete(data,data.Likes==like_max,axis = 0 )
        n_meilleurstweets_like(data,n-1)
