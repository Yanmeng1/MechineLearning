import numpy as np
from math import sqrt

def accuracy_score(y_true, y_predict):
    assert len(y_true) == len(y_predict), 'the size of y_true must be equal to the size of y_predict'
    return np.sum(y_true == y_predict) / len(y_true)

'''
    线性回归衡量指标
        accuracy
        RMSE / MSE (Root Mean Squared Error) 
        MAE (Mean Absolute Error)
        R^2 = 1 - (MSE / var)
'''
def mean_squared_error(y_true, y_predict):
    assert len(y_true) == len(y_predict), "the size of y_true must be equal to the size of y_predict"
    return np.sum((y_true - y_predict)**2) / len(y_true)

def root_mean_squared_error(y_true, y_predict):
    return sqrt(mean_squared_error(y_true, y_predict))

def mean_absolute_error(y_true, y_predict):
    assert len(y_true) == len(y_predict), "the size of y_true must be equal to the size of y_predict"
    return np.sum(np.absolute(y_true - y_predict)) / len(y_true)

def r2_score(y_true, y_predict):
    return 1 - mean_squared_error(y_true, y_predict) / np.var(y_true)