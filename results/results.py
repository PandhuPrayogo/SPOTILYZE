import pandas as pd

dataset = pd.read_csv('folder_file/All_Pokemon.csv')

print(dataset.describe())
print(dataset.info())
most = dataset.query('HP > 50', inplace = False).sort_values('HP', ascending=False)
print(most[0:5])