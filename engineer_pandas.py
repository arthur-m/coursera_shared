import pandas as pd
import matplotlib.pyplot as plt

filename = 'text_files/more_hubble.csv'

headers = ['dist', 'rec_vel']

data = pd.read_csv(filename, names=headers)     # this version of the csv has no headers, so we add them manually

print(data.head())

data.set_index('dist', inplace=True)        # change  the index to the 'dist' column

print(data.head())

