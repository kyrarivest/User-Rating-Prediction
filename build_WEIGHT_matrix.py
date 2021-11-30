import numpy as np
import pandas as pd
import pickle


def get_weights_distance(abs_diff, exp):
    tot_abs_diff = np.sum(abs_diff)
    if tot_abs_diff == 0:
        return 0
    return 1/tot_abs_diff**exp



def build(user_history):
    ### Finding weight matrix

    weight_matrix = []

    print('finding weight matrix')

    for u in range(len(user_history)):
        weight_matrix.append([float(0) for i in range(u)])
        for v in range(u, len(user_history)):
            print('comparing User #' + str(u) + ' and ' + 'User #' + str(v))
            abs_diff = np.absolute(user_history.iloc[u, 1:] - user_history.iloc[v, 1:])
            tot_abs_diff = get_weights_distance(abs_diff, 2)
            weight_matrix[u].append(tot_abs_diff)

    X = np.array(weight_matrix)
    X = X + X.T - np.diag(np.diag(X))

    weight_matrix = {}
    for i in range(len(X)):
        weight_matrix[int(user_history.iloc[i][0])] = X[i]

    weight_matrix = pd.DataFrame(weight_matrix)
    weight_matrix.to_csv('weight_matrix.csv')

    print('completed finding weight matrix')