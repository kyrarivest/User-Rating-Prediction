import numpy as np
import pandas as pd
from statistics import variance

directory = "results/"
preds = ["distance_half.csv","distance_1.csv","distance_2.csv","distance_4.csv","distance_8.csv","distance_16.csv","distance_32.csv"]
preds = [directory+i for i in preds]

y_true = pd.read_csv("RATINGS_full.csv")
sorted_columns = sorted(y_true.columns[1:])
sorted_columns.insert(0, y_true.columns[0])
y_true = y_true.reindex(sorted_columns, axis=1)

row_index = []
column_index = []


for i in range(len(y_true)):
    for j in range(1, len(y_true.iloc[i])):
        if not np.isnan(y_true.iloc[i][j]):
            row_index.append(i)
            column_index.append(j)


powers = [0.5,2,4,8,16,32]
for i, pred in preds:
    y_pred = pd.read_csv(pred)
    sorted_columns = sorted(y_pred.columns[1:])
    sorted_columns.insert(0, y_pred.columns[0])
    y_pred = y_pred.reindex(sorted_columns, axis=1)

    denom = 0
    loss = 0
    for i in range(len(row_index)):
        y_true_val = y_true.iloc[row_index[i]][column_index[i]]
        y_pred_val = y_pred.iloc[row_index[i]][column_index[i]]
        denom += y_true_val**2
        loss += (y_pred_val - y_true_val)**2
    
    print()
    print("Power: " + str(powers[i]))
    print("Relative loss: " + str(loss/denom))
    print("Absolute loss: " + str(loss))