import numpy as np
import pandas as pd
import pickle
import datetime

#Author: Daniel Hariyanto
#See the README.md for description and purpose of this file




#Returns the inverse of the weighted distance between the absolute distance of two user's browser times
#To be used in the build function to create the weight matrix
#abs_diff: the absolute distance of two user's website browsing times for a particualr website
#power: the specified power to raise the abs_diff by. This is a parameter of the model that is varied
def get_weights_distance(abs_diff, power):
    tot_abs_diff = np.sum(abs_diff)
    if tot_abs_diff == 0:
        return 0
    return 1/tot_abs_diff**power



#The main function that builds the weight matrix
#user_history: the original user_history csv file
#power: specify which power to build the matrix for
def build(user_history, power):
    begin_time = datetime.datetime.now()
    print("Begin building weight matrix...      (This step will take about 2.5 hours)")
    weight_matrix = []

    
    for u in range(len(user_history)):  #for each user row
        weight_matrix.append([float(0) for i in range(u)])
        
        for v in range(u, len(user_history)):   #go through every user
            
            #Turn this on if you want to keep track of user's being processed
            #print('     comparing User #' + str(u) + ' and ' + 'User #' + str(v))
            
            abs_diff = np.absolute(user_history.iloc[u, 1:] - user_history.iloc[v, 1:])
            tot_abs_diff = get_weights_distance(abs_diff, power)
            weight_matrix[u].append(tot_abs_diff)

            
    #Create upper triangular matrix and reflect it to create full matrix
    X = np.array(weight_matrix)
    X = X + X.T - np.diag(np.diag(X))

    weight_matrix = {}
    for i in range(len(X)):
        weight_matrix[int(user_history.iloc[i][0])] = X[i]

        
        
    #Create dataframe for weight matrix
    weight_matrix = pd.DataFrame(weight_matrix)


    #Save weight matrix as a csv and pkl file if needed
    """
    if(power == 0.5):
        weight_matrix.to_csv('weight_matrix_half.csv')

        open_file = open('weight_matrix_half.pkl', "wb")
        pickle.dump(weight_matrix, open_file)
        open_file.close()

    else:
        weight_matrix.to_csv('weight_matrix_' + str(power) + '.csv')

        open_file = open('weight_matrix_' + str(power) + '.pkl', "wb")
        pickle.dump(weight_matrix, open_file)
        open_file.close()
    """
   

    print('Completed building weight matrix')
    print("Execution time = " + str(datetime.datetime.now() - begin_time))
    print()
    return weight_matrix
