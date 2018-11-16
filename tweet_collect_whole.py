def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    hashtag = file_path + "/hashtag_candidate_" + str(num_candidate) +".txt"

    try:
        hashtag_candidat = open(hashtag,'r')
        liste_hashtags = []
        for t in hashtag_candidat :
            liste_hashtags+= t.split(' ')
        return liste_hashtags

    except IOError:
        print('Cannot open')

#print(get_candidate_queries(1976143068,"Users/anne/Desktop/CandidateData"))



