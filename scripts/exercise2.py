import pandas as pd
print(pd.__version__)

df = pd.read_csv('folder_file/All_Pokemon.csv')

df_mean = df.groupby('Type 1').mean()