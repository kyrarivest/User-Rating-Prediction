import numpy as np
import pandas as pd
import pickle
import datetime

#Author: Kyra Rivest
#See README.md for description and purpose



def build(user_history_data, user_ratings_data):
    begin_time = datetime.datetime.now()
    print("Begin building ratings matrix...")
    # load data as a dataframe with pandas
    user_history = user_history_data
    user_ratings = user_ratings_data

    #Prepare data
    #product_names = np.concatenate( (["USER ID"], user_ratings["PRODUCT"].unique()) )
    product_names = user_ratings["PRODUCT"].unique()
    users_in_ratings = user_ratings["USER ID"].unique()
    ratings_by_user = user_ratings.groupby("USER ID")
    RATINGS_full = []


    #_________Main Loop_________
    #for each user, make a row for that user and add it to ratings matrix
    #user_id type = int 0, 1, 2, 3, ...
    #user_data type = Series
    for user_id, user_data in user_history.iterrows(): #for each user
        print("Processing user " + str(user_history.iloc[user_id][0]) + ", " + str(user_id))

        user_i = [] #will contain user_i's ratings of all products
        #user_i.append(user_id) 
        
    
        #If the user is in both the user_history and the user_ratings data
        if(user_history.iloc[user_id][0] in users_in_ratings):
            user_i_ratings = ratings_by_user.get_group(int(user_history.iloc[user_id][0])) #Dataframe containing all user_i's ratings

            for i in range(len(product_names)): #for each product column, fill in with the rating the user gave, or NaN if no rating is given
                prod = product_names[i]
                if user_i_ratings["PRODUCT"].str.contains(prod).any():

                    user_i.append(int(user_i_ratings.loc[user_i_ratings["PRODUCT"] == prod, "RATING"].iloc[0]))
                else:
                    user_i.append(np.nan)

            RATINGS_full.append(user_i) #add the row to the full matrix


        #If the user is in the user hsitory but not the user ratings data
        else:
            for i in range(len(product_names)):
                user_i.append(np.nan)

            RATINGS_full.append(user_i) #add the row to the full matrix



    #convert matrix to a dataframe and return
    RATING_full_df = pd.DataFrame(RATINGS_full, columns=product_names, index=list(user_history["USER ID"]))
    
    print('Completed building weight matrix')
    print("Execution time = " + str(datetime.datetime.now() - begin_time))
    
    #save RATINGS df as a pkl file
    #RATING_full_df.to_csv("RATINGS_full.csv", index=False)

    #open_file = open("RATINGS_full.pkl", "wb")
    #pickle.dump(RATING_full_df, open_file)
    #open_file.close()

    
    return RATING_full_df


    
