# MATH122 Final Project - User Rating Prediction

Our final project for MATH 122 uses a K-nearest neighbors inspired model to predict product ratings for 4500 given users. For more information ont he theory behind our approach, please refer to our [final report](https://docs.google.com/document/d/1zeOJMtTpI13Hz6NleexRDa9FsI-tDtqm8mNVLc6mO4g/edit?usp=sharing). Here we given detailed description of our code that we used in the report.

The data we are given two data sets: 
- [user_history.csv](https://c569257608da4dcaafbc-my.sharepoint.com/:x:/g/personal/kyrarivest_brandeis_edu/ESnHmQiYEqtEuUTzZBAM9aMBa4lJ11yGAOXs3PN4rxFfKg?e=WGI6ZD): provides the browser history times of 4500 users for 100 different websites
- [user_ratings.csv](https://c569257608da4dcaafbc-my.sharepoint.com/:x:/g/personal/kyrarivest_brandeis_edu/Edf-Cftx1QBEg4nT0CrTVMABGhJfDwSN6SKW3Vd9Yry8RA?e=faePVb) : provides the product ratings of 3000 different users for 75 different products. All 3000 users provide the ratings of some but not all 75 products.

# File Descriptions

This repository includes four different files for the model.

### build_WEIGHT_matrix.py
This program takes in the given user_history data and produces a weight matrix for the user browser hisotry data. In our notation, a "weight" for a given user to another user is an inverse distance between the two users. And this distance is a sum of the difference in browsing times between the two users for every website. We raise this distance to a power which is a parameter in our model (see report for more details). These weights are used in **predict.py** to weight the different users' ratings for a particular product when predicting the rating for a given user i, thereby placing more importance on the ratings of users that are "closer" to user i than those that are farther.

Each row in the matrix represents a user. Each entry in a given row i is the distance of user i to another user. Therefore, we were able to significantly reduce the run time by eliminating redundancy in calculations. We did this by building an upper triangular matrix and then reflecting the entries onto the lower empty part of the matrix to create the full matrix. We then return the matrix to be used in **predict.py**.

### build_RATINGS_dfs.py
This program takes in both given data sets and produces pivot table style matrix containing all 4500 users and their ratings for each product. It first loads the data as *user_history_data* and *user_rating_data*, prepares the data files for processing, and then produces the ratings matrix. The resulting table contians all products as columns and all users as rows. This is the table that the predict.py program will fill in with missing ratings.

### predict.py
### main.py
