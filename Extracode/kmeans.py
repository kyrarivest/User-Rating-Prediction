from sklearn.cluster import KMeans
import numpy as np
import pandas as pd


user_history = pd.read_csv("user_history.csv")
kmeans = KMeans(n_clusters=3).fit_predict(user_history)

user_to_cluster = {user_history['USER ID'][i]: kmeans[i] for i in range(len(user_history['USER ID']))}


### USER RATINGS FORMATTING
user_ratings = pd.read_csv("user_ratings.csv")
user_ratings_table = pd.pivot_table(user_ratings,values='RATING', index='USER ID', columns='PRODUCT')

all_user_ids = list(user_history['USER ID'])
all_rating_user_ids = user_ratings_table.index

missing_ids = set(all_user_ids).difference(all_rating_user_ids)

for id in missing_ids:
    user_ratings_table = user_ratings_table.append(pd.Series(name=id))

user_ratings_table = user_ratings_table.sort_values(by=['USER ID'])



### Predicting ratings based on weights matrix

def pred_ratings(cluster_id, weights_index, weights_vector, ratings_index, ratings_vector):
    # assumes that len(weights_vector) > len(ratings_vector)
    # assumes that ratings_index is a subset of weights_index
    
    pred = 0
    new_weights_vector = []
    
    for r, rating in enumerate(ratings_vector):
        if weights_index[r] == ratings_index[r]:
            if not np.isnan(rating):
                if user_to_cluster[weights_index[r]] == cluster_id:
                    new_weights_vector.append(weights_vector[r])
                    pred += weights_vector[r] * rating
        else:
            print(weights_index[r])
    
    weight_tot = 0
    for weight in new_weights_vector:
        weight_tot += weight

    if weight_tot == 0:
        rating_score = 0
    else:
        rating_score = pred/weight_tot
    
    return rating_score


print('predicting ratings')


columns = [col for col in user_ratings_table.columns]

weights = ["half", "1", "2", "4", "8", "16", "32"]
for weight in weights:
    weight_matrix = pd.read_csv("../trials_new/weight_matrix_distance_"+weight+".csv")
    weight_matrix = weight_matrix.to_dict()
    user_ratings_table_pred = user_ratings_table.copy()

    for u in range(len(user_ratings_table)):
        for p in range(len(user_ratings_table.iloc[u])):
            cluster_id = user_to_cluster[list(user_ratings_table.index)[u]]
            pred = pred_ratings(cluster_id, list(user_history['USER ID']), weight_matrix[str(list(user_ratings_table.index)[u])], list(user_ratings_table[columns[p]].index), user_ratings_table[columns[p]])
            user_ratings_table_pred.iloc[u][p] = pred

    print('completed predicting ratings')

    user_ratings_table_pred.to_csv('distance_'+weight+'.csv')

    print('output to csv file')