import numpy as np
import pandas as pd
from statistics import variance

def run(RATINGS_matrix):

    #Prepare to load data
    directory = "results_for_analysis/"
    preds = ["raw_results_power_half.csv","raw_results_power_1.csv","raw_results_power_2.csv","raw_results_power_4.csv","raw_results_power_8.csv","raw_results_power_16.csv","raw_results_power_32.csv"]
    preds = [directory+i for i in preds]

    
    #Prepare the true data
    y_true = RATINGS_matrix
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


                
                
    #For each power, calculate errors
    powers = [0.5,1,2,4,8,16,32]
    for pred in preds:
        print("Analyzing results for power: " + str(powers[preds.index(pred)]))
        y_pred = pd.read_csv('results_for_analysis/' + str(pred))
        sorted_columns = sorted(y_pred.columns[1:])
        sorted_columns.insert(0, y_pred.columns[0])
        y_pred = y_pred.reindex(sorted_columns, axis=1)

        denom = 0
        denom_squared = 0
        loss = 0
        loss_squared = 0
        abs_loss = 0
        for i in range(len(row_index)):
            y_true_val = y_true.iloc[row_index[i]][column_index[i]]
            y_pred_val = y_pred.iloc[row_index[i]][column_index[i]]
            denom += y_true_val
            denom_squared += y_true_val**2
            loss += (y_pred_val - y_true_val)
            loss_squared += (y_pred_val - y_true_val)**2
            abs_loss += abs(y_pred_val - y_true_val)

            
        #Print errors to console
        print("Absolute Relative loss: " + str(abs_loss/denom))
        print("Relative loss: " + str(loss_squared/denom_squared))
        print("Absolute loss: " + str(abs_loss))
        print()
        print()
        
        
        
        #Save data to results_FINAL
        y_pred.reset_index(inplace=True)
        user_ratings_back_to_orig = y_pred.melt(id_vars = 'USER ID', var_name = 'PRODUCT', value_name = 'RATING')
        user_ratings_back_to_orig.sort_values(by=['USER ID'], inplace=True)
        user_ratings_back_to_orig = user_ratings_back_to_orig[user_ratings_back_to_orig['PRODUCT'] != 'index']


        if(powers[i] == 0.5):
            user_ratings_back_to_orig.to_csv('results_FINAL/final_results_0.5.csv', index=False)
        else:
            user_ratings_back_to_orig.to_csv('results_FINAL/final_results_' + str(2) + '.csv', index=False)
            
            
"""
RESULTS:
Analysing results for power: 0.5
Total Execution Time: 2:40:20

Absolute Relative loss: 0.445464213095741
Relative loss: 0.22496504789801816
Absolute loss: 74155.98208983491

Analysing results for power: 1
Total Execution Time: 2:44:15

Absolute Relative loss: 0.44709021395312915
Relative loss: 0.2260853002874098
Absolute loss: 74426.66082656346

Analysing results for power: 2
Total Execution Time: 2:33:17

Absolute Relative loss: 0.45325729221829714
Relative loss: 0.23491250718891812
Absolute loss: 75453.28817828771

Analysing results for power: 4
Total Execution Time: 2:32:15

Absolute Relative loss: 0.4812942417911362
Relative loss: 0.2803563732593066
Absolute loss: 80120.57113672866


Analysing results for power: 8
Total Execution Time: 2:40:07

Absolute Relative loss: 0.5285239608087979
Relative loss: 0.35576954987977644
Absolute loss: 87982.85523187979


Analysing results for power: 16
Total Execution Time: 2:29:34

Absolute Relative loss: 0.5580353965647471
Relative loss: 0.39943284038112653
Absolute loss: 92895.59443073688


Analysing results for power: 32
Total Execution Time: 2:29:10

Absolute Relative loss: 0.5703427832756094
Relative loss: 0.4164919844977325
Absolute loss: 94944.39278910741

"""
        
