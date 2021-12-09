# MATH122 Final Project - User Rating Prediction

Our final project for MATH 122 uses a K-nearest neighbors inspired model to predict product ratings for 4500 given users. For more information ont he theory behind our approach, please refer to our [final report](https://docs.google.com/document/d/1zeOJMtTpI13Hz6NleexRDa9FsI-tDtqm8mNVLc6mO4g/edit?usp=sharing). Here we given detailed description of our code that we used in the report.

The data we are given two data sets: 
- [user_history.csv](https://c569257608da4dcaafbc-my.sharepoint.com/:x:/g/personal/kyrarivest_brandeis_edu/ESnHmQiYEqtEuUTzZBAM9aMBa4lJ11yGAOXs3PN4rxFfKg?e=WGI6ZD): provides the browser history times of 4500 users for 100 different websites
- [user_ratings.csv](https://c569257608da4dcaafbc-my.sharepoint.com/:x:/g/personal/kyrarivest_brandeis_edu/Edf-Cftx1QBEg4nT0CrTVMABGhJfDwSN6SKW3Vd9Yry8RA?e=faePVb) : provides the product ratings of 3000 different users for 75 different products. All 3000 users provide the ratings of some but not all 75 products.

# File Descriptions

This repository includes four different files and two folders for the model.

### build_WEIGHT_matrix.py
This program takes in the given user_history data and produces a weight matrix for the user browser hisotry data. In our notation, a "weight" for a given user to another user is an inverse distance between the two users. And this distance is a sum of the difference in browsing times between the two users for every website. We raise this distance to a power which is a parameter in our model (see report for more details). These weights are used in **predict.py** to weight the different users' ratings for a particular product when predicting the rating for a given user i, thereby placing more importance on the ratings of users that are "closer" to user i than those that are farther.

Each row in the matrix represents a user. Each entry in a given row i is the distance of user i to another user. Therefore, we were able to significantly reduce the run time by eliminating redundancy in calculations. We did this by building an upper triangular matrix and then reflecting the entries onto the lower empty part of the matrix to create the full matrix. We then return the matrix to be used in **predict.py**.


### build_RATINGS_matrix.py
This program takes in both given data sets and produces pivot table style matrix containing all 4500 users and their ratings for each product. It first loads the data as *user_history_data* and *user_rating_data*, prepares the data files for processing, and then produces the ratings matrix. The resulting table contians all products as columns and all users as rows. This is the table that the predict.py program will fill in with missing ratings.

### predict.py
This program contains two methods. The **run** method is the main loop that runs the prediction algorithm. It first copies the user rating matrix so that the newly predicted ratings wont affect the future predictions. It loops through each user and for each user predicts all the user's ratings for all products based on the distance of that user to all other users who have a existing product prediction (meaning it will skip a user if that user hasn't given a rating for the product). After the loop finishes and the table has been filled, it will be returned for analysis.

The helper method of the **run** method is **pred_ratings**. This is the method taht does the heavy-lifting computation portion of the algorithm. For a specified user i and a specified product j, it will compute weighted rating of user i by multiplying all other user ratings (from user rating matrix) by the user distance to user i (from weight matrix). It then scales the final score and returns it. Tis way, the predicted rating is normalized.

### main_method.py
This program runs all the other three programs. We broke the model up like this so that we could test different powers for the distance weight. 

### analyze_results.py
This program runs error analysis on the raw resulting prediction csv files. Calculates realtive absolute error, realtive error, and absolute errors as given in the report. These errors will be printed to the console. The raw prediction files will then be converted to the final format which is the same as the original user_ratings file.

### results_for_analysis
This will hold the resulting raw prediction files that come out of **predict.py**. These files will be in the form of the pivot table so that error analysis can be run on them.

### results_FINAL
This will hold the final prediction files after error analysis has been run on them. These files will be in the form of the original user_ratings file.

### Extracode
Holds extra pieces of code that are relevant to individual contirbutions to the project.

# To run the code
In order to run this code, you will only have to run the **main.py** file to reproduce what we have already included.

```python
python main.py
```

This will run all powers in one loop so it will take awhile. But for each power, we have calculated about how long it will take (these times are also documented within the code so when it is run, it will print the runtime)

- build_WEIGHT_matrix.py: building the weight matrix takes 2 hours
- predict.py: predicting the ratings takes about 40 minutes
- analyze_results.py: doing error analysis and formatting the final results takes about 30sec

So in total, each round should take around 2.5 hours, so to run 7 different powers would take about 17.5 hours.

The resulting prediction files will be saved to the **results_for_analysis** folder. After **predict.py** runs, **main.py** will run **analyze_results.py** and the errors will be printed to the console.
