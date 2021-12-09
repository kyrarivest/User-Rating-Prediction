import numpy as np
import pandas as pd
import pickle
import datetime

#Author: Kyra Rivest
#See README.md for description and purpose



#Main function that builds the user ratings matrix
#user_history_data: the original user_history.csv file
#user_ratings_data: the original user_ratings.csv file
#Returns the user ratings matrix with all 4500 users, each as one row
#Note: for those users that are in the user_history file but not the user_ratings file, they are added as a user with a completely blank row.
def build(user_history_data, user_ratings_data):
    begin_time = datetime.datetime.now()
    print("Begin building ratings matrix...")
    
    
    # load data as a dataframe with pandas
    user_history = user_history_data
    user_ratings = user_ratings_data

    
    #Create the pivot table matrix for the 3000 users in user_ratings
    user_ratings_table = pd.pivot_table(user_ratings,values='RATING', index='USER ID', columns='PRODUCT')

    
    #Create a seperate dataframe for the extra 1500 users not in user_ratings
    extra_users = np.empty((1500,75,))
    extra_users[:] = np.nan
    indices =[]
    user_ratings_indices = user_ratings_table.index
    
    for user, data in user_history.iterrows():
       if user_history["USER ID"][user] not in user_ratings_indices:
           indices.append(user_history["USER ID"][user])


    extra_df = pd.DataFrame(extra_users, columns=user_ratings_table.columns, index=indices)

    
    #Combine the two dataframes 
    RATING_full_df = user_ratings_table.append(extra_df)
    RATING_full_df.index.name = "USER ID"


    print('Completed building weight matrix')
    print("Execution time = " + str(datetime.datetime.now() - begin_time))
    print()
    
    
    #save ratings matrix as a csv and pkl file if needed
    """
    RATING_full_df.to_csv("RATINGS_full.csv", index=False)

    open_file = open("RATINGS_full.pkl", "wb")
    pickle.dump(RATING_full_df, open_file)
    open_file.close()
    """

    return RATING_full_df

    

    

    


    

    

