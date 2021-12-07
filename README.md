# MATH122 Final Project - User Rating Prediction

Our final project for MATH 122 uses a K-nearest neighbors inspired model to predict product ratings for 4500 given users.

The data we are given two data sets: 
- [user_history.csv](https://c569257608da4dcaafbc-my.sharepoint.com/:x:/g/personal/kyrarivest_brandeis_edu/ESnHmQiYEqtEuUTzZBAM9aMBa4lJ11yGAOXs3PN4rxFfKg?e=WGI6ZD): provides the browser history times of 4500 users for 100 different websites
- [user_ratings.csv](https://c569257608da4dcaafbc-my.sharepoint.com/:x:/g/personal/kyrarivest_brandeis_edu/Edf-Cftx1QBEg4nT0CrTVMABGhJfDwSN6SKW3Vd9Yry8RA?e=faePVb) : provides the product ratings of 3000 different users for 75 different products. All 3000 users provide the ratings of some but not all 75 products.

# File Descriptions

This repository includes four different files for the model.

### build_WEIGHT_matrix.py

### build_RATINGS_dfs.py
This program takes in both given data sets and produces pivot table style matrix containing all 4500 users and their ratings for each product. It first loads the data as *user_history_data* and *user_rating_data*, prepares the data files for processing, and then produces the ratings matrix. The resulting table contians all products as columns and all users as rows. This is the table that the predict.py program will fill in.

### predict.py
### main.py
