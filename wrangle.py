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
    