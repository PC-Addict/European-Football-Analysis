import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/jayan/Desktop/euro analysis/european_league.csv')
df.index = np.arange(1, len(df) + 1)


def preprocess():
    global df
    return df


epl_df = pd.read_csv('C:/Users/jayan/Desktop/euro analysis/england/epl.csv')
epl_df.index = np.arange(1, len(epl_df) + 1)


def preprocess_epl():
    global epl_df
    return epl_df


france_df = pd.read_csv('C:/Users/jayan/Desktop/euro analysis/france/ligue1.csv')
france_df.index = np.arange(1, len(france_df) + 1)


def preprocess_ligue1():
    global france_df
    return france_df


spain_df = pd.read_csv('C:/Users/jayan/Desktop/euro analysis/spain/spain.csv')
spain_df.index = np.arange(1, len(spain_df) + 1)


def preprocess_laliga():
    global spain_df
    return spain_df


german_df = pd.read_csv('C:/Users/jayan/Desktop/euro analysis/germany/germany.csv')
german_df.index = np.arange(1, len(german_df) + 1)


def preprocess_bundesliga():
    global german_df
    return german_df


italy_df = pd.read_csv('C:/Users/jayan/Desktop/euro analysis/italy/italy.csv')
italy_df.index = np.arange(1, len(italy_df) + 1)


def preprocess_sa():
    global italy_df
    return italy_df
