import numpy as np
import pandas as pd
import pickle
import datetime

#Authors: Daniel Hariyanto and Kyra Rivest
#See the README.md for description and purpose of this file




#Predict rating for a specified user and product based on weights matrix
#Ex. Predict rating for user 1, product 1, returns predicted rating

#weights_index: a list of all user IDs in order
#weights_vector: a vector of distances of a given user to all other users
#ratings_index:a list of all user IDs for a specified product column
#ratings_vector: a specified product column
def pred_ratings(weights_index, weights_vector, ratings_index, ratings_vector):
    # assumes that len(weights_vector) > len(ratings_vector)
    # assumes that ratings_index is a subset of weights_index
    
    pred = 0
    new_weights_vector = []
    counter = 0
    
    for r, rating in enumerate(ratings_vector):
        if weights_index[r+counter] == ratings_index[r]:
            if not np.isnan(rating):
                new_weights_vector.append(weights_vector[r+counter])
                pred += weights_vector[r+counter] * rating
        else:
            counter += 1
    
    weight_tot = 0
    for weight in new_weights_vector:
        weight_tot += weight

    if weight_tot == 0:
        rating_score = 0
    else:
        rating_score = pred/weight_tot
    
    return rating_score




#Predicts the ratings for every user for every product (predicts regardless of whether or not the rating is missing or not).
#user_history: the original user_history data
#weight_matrix: the weight matrix of user distances
#user_ratings_table: the ratings matrix of user and product ratings
#power: specifies the power parameter
def run(user_history, weight_matrix, user_ratings_table, power):
    begin_time = datetime.datetime.now()
    print('Begin predicting ratings...')


    columns = [col for col in user_ratings_table.columns]   #list of all product columns

    user_ratings_table_pred = user_ratings_table.copy()     #copy of the user_ratings table to be filled in with ratings

    for u in range(len(user_ratings_table)):       #for each user
        
        #Turn this on if you want to keep track of which users are being processed in real time
        #print("Processing user: " + str(u))
        
        
        for p in range(len(user_ratings_table.iloc[u])):    #predict rating for each product
            pred = pred_ratings(list(user_history['USER ID']), weight_matrix[list(user_ratings_table.index)[u]], list(user_ratings_table[columns[p]].index), user_ratings_table[columns[p]])
            user_ratings_table_pred.iloc[u][p] = pred
            
            

    print()
    print('Completed predicting ratings')
    print("Execution time = " + str(datetime.datetime.now() - begin_time))

    
    
    #Save rating results table as a csv file and a pkl file to the results_for_analysis file
    if(power == 0.5):
        user_ratings_table_pred.to_csv('results_for_analysis/raw_results_power_half.csv')
        open_file = open('results_for_analysis/raw_results_power_half.pkl', "wb")
        pickle.dump(user_ratings_table_pred, open_file)
        open_file.close()

    else:
        user_ratings_table_pred.to_csv('results_for_analysis/raw_results_power_' + str(power) + '.csv')

        open_file = open('results_for_analysis/raw_results_power_' + str(power) + '.pkl', "wb")
        pickle.dump(user_ratings_table_pred, open_file)
        open_file.close()

        
        
        
    return user_ratings_table_pred








   
