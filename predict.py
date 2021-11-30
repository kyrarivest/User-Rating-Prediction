import numpy as np
import pandas as pd
import pickle

#with open('DISTANCES_full.pkl', 'rb') as f:
#   user_distances = pickle.load(f)

#user_ratings = pd.read_csv("RATINGS_short.csv")



def run(WEIGHT_matrix, RATINGS_matrix):
    #Prepare data for processing
    complete_matrix = RATINGS_matrix.copy()
    total_error = 0
    total_error_count = 0 



    #_________Main Loop_________
    for prod in RATINGS_matrix:  #for each product
        if not prod == "USER ID": #skip the first column

            print("___________________(PRODUCT: " + str(prod) + ")___________________")
            print()

            for j in range(len(RATINGS_matrix)): #for each user for that product column, generate a rating
                user_j_rating = RATINGS_matrix[prod][j]
                #print("Predicting for user " + str(j))

                rating_predicted = 0
                sum_W_r = 0
                sum_W = 0
                mean_squared_error = 0
                W = 0

                for k in range(len(RATINGS_matrix)): #go through each user that is not user j
                    user_k_rating = RATINGS_matrix[prod][k]
                    #print("     user " + str(k))
                    #print("     rating: " + str(user_ratings[prod][k]))
                    #print("     "+ str(user_ratings["USER ID"][j] != user_ratings["USER ID"][k]))

                    if((RATINGS_matrix["USER ID"][j] != RATINGS_matrix["USER ID"][k]) and (not np.isnan(user_k_rating))):
                        W = WEIGHT_matrix[j][k+1]
                        sum_W_r += W * (user_k_rating)
                        sum_W += W
                        W = 0

                    #print("     User distance: " + str(user_distances[j][k+1]))
                    #print("     W: " + str(W))
                    #print("     sum_W: " + str(sum_W))
                    #print("     sum_W_r: " + str(sum_W_r))
                    #print()

        
                if(sum_W_r == 0):
                    #print("Inconclusive, no ratings for this product exist")
                    rating_predicted = -1
                else:
                    rating_predicted = sum_W_r / sum_W 


                if((not np.isnan(user_j_rating)) and (not rating_predicted == -1)):
                    mean_squared_error = (rating_predicted - RATINGS_matrix[prod][j]) ** 2
                    total_error += mean_squared_error
                    total_error_count += 1

                complete_matrix[prod][j] = rating_predicted


                #print("User " + str(int(user_ratings["USER ID"][j])) + " rating: " + str(rating_predicted))
                #print("True rating: " + str(user_ratings[prod][j]))
                #print("Error: " + str(mean_squared_error))
                #print("Total error: " + str(total_error))
                #print()
            


    complete_matrix.to_csv("RATINGS_complete_short.csv", index=False)


    #open_file = open("RATINGS_complete_full2.pkl", "wb")
    #pickle.dump(complete_matrix, open_file)
    #open_file.close()


    print("___________________DONE___________________")
    print("Average Error: " + str(total_error / total_error_count))
    print("Total error: " + str(total_error))
    

    #print(complete_matrix)










   