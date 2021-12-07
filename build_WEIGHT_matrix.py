import numpy as np
import pandas as pd
import pickle

#Author: Daniel Hariyanto
#See the README.md for description and purpose of this file




#Returns the inverse of the weighted distance between the absolute distance of two user's browser times
#To be used in the build function to create the weight matrix
#abs_diff: the absolute distance of two user's website browsing times for a particualr website
#exp: the specified power to raise the abs_diff by. This is a parameter of the model that is varied
def get_weights_distance(abs_diff, power):
    tot_abs_diff = np.sum(abs_diff)
    if tot_abs_diff == 0:
        return 0
    return 1/tot_abs_diff**power



#The main function that builds the weight matrix
#user_history: the given user_history csv file
def build(user_history, power):
    print("Begin building weight matrix...")
    weight_matrix = []

    
    for u in range(len(user_history)):  #for each user row
        weight_matrix.append([float(0) for i in range(u)])
        
        for v in range(u, len(user_history)):   #go through every user
            print('     comparing User #' + str(u) + ' and ' + 'User #' + str(v))
            abs_diff = np.absolute(user_history.iloc[u, 1:] - user_history.iloc[v, 1:])
            tot_abs_diff = get_weights_distance(abs_diff, power)
            weight_matrix[u].append(tot_abs_diff)

    #Create matrix
    X = np.array(weight_matrix)
    X = X + X.T - np.diag(np.diag(X))

    weight_matrix = {}
    for i in range(len(X)):
        weight_matrix[int(user_history.iloc[i][0])] = X[i]

        
        
    #Create dataframe for weight matrix
    weight_matrix = pd.DataFrame(weight_matrix)
    
    #Save weight matrix as csv file
    #weight_matrix.to_csv('weight_matrix.csv')

    print('completed finding weight matrix')
    return weight_matrix
