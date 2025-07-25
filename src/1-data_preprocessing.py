## importing libraries
import pandas as pd
import numpy as np


## loading the dataset
def load_data():
    df = pd.read_paruqet(r'C:\Users\himan\Desktop\Projects\Energy_Forecasting_System\data\raw-data\est_hourly.paruqet', parse_dates=['Date'], index_col='Date')
    return df


## cleaning the dataset
def clean_data(df):
    if df.isnull().values.any():
        df = df.fillna(method='ffill')
    df = df.drop_duplicates()


## splitting the dataset into train and test sets
def split_data(df, target_column):
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    train_size = 0.8  ## 80% for training, 20% for testing
    size = int(len(df) * train_size)
    X_train, X_test = df[:size], df[size:]
    y_train, y_test = y[:size], y[size:]

    return X_train, y_train, X_test, y_test
