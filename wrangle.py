import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split


def acquire_wine():
    red = pd.read_csv('https://query.data.world/s/6ydfnt5m4fjpceorhly36l6wlw6kas?dws=00000')
    red['color'] = 'red'
    white = pd.read_csv('https://query.data.world/s/mw4h7fongq3w76kgxi376up7goebry?dws=00000')
    white['color'] = 'white'
    wines = pd.concat([red, white], ignore_index=True)
    return wines


def train_val_test(df):
    train_val, test = train_test_split(df,
                                       train_size=0.8,
                                       random_state=706)
    train, validate = train_test_split(train_val,
                                       train_size=0.7,
                                       random_state=706)
    return train, validate, test


def wrangle_wine():
    wines = acquire_wine()
    train, val, test = train_val_test(wines)
    return train, val, test
    
    
    
def remove_outliers(df, col_list, k=1.5):
    '''
    remove outliers from a dataframe based on a list of columns
    using the tukey method.
    returns a single dataframe with outliers removed
    '''
    col_qs = {}
    for col in col_list:
        col_qs[col] = q1, q3 = df[col].quantile([0.25, 0.75])
    for col in col_list:
        iqr = col_qs[col][0.75] - col_qs[col][0.25]
        lower_fence = col_qs[col][0.25] - (k*iqr)
        upper_fence = col_qs[col][0.75] + (k*iqr)
        print(type(lower_fence))
        print(lower_fence)
        df = df[(df[col] > lower_fence) & (df[col] < upper_fence)]
    return df
