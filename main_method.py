import numpy as np
import pandas as pd
import pickle

import build_WEIGHT_matrix
import build_RATINGS_dfs
import predict
import analyze_results



user_history = pd.read_csv("user_history.csv")
user_ratings = pd.read_csv("user_ratings.csv")


#__________________MAIN METHOD__________________#

powers = [0.5,2,4,8,16,32]
RATINGS_matrix = build_RATINGS_dfs.build(user_history, user_ratings)

for power in powers:

  WEIGHT_matrix = build_WEIGHT_matrix.build(user_history, power)
  predicted_ratings = predict.run(WEIGHT_matrix, RATINGS_matrix, power)
  analyze_results.run()
