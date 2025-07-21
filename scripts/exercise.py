# Exercising to learn pandas as data analyst

import pandas as pd

df = pd.read_csv('folder_file/All_Pokemon.csv') # df = pd.read_excel('folder_file/All_Pokemon.xlsx)
# Read the csv
print(df)
# Read the top of data in csv
print(df.head(3))
# Read the bottom of data in csv
print(df.tail(3))
# Read each row (selected condition) of data in csv
print(df.iloc[0:3]) # Evolution of bulbasaur
print(df.iloc[2, 1]) # Read final evolution of bulbasaur
print(df.iloc[1]) # Print row number 2 in csv
# Read eaxh row with complicated condition
print(df.loc[0:3, ['Name', 'Type 1']]) # Print with specific condition
print(df['Name']) # Print info of columns
print(df.loc[df['HP'] > 50]) # Print with specific condition based on column
# Sorted
print(df.head())
print(df.tail())
print(df.sort_values('HP',ascending=True))
# Print Columns
print(df.columns)
# Iterate of data
#for index, row in df.iterrows():
  #index+=0
  #print(f"{index}. {row['Name'], row['HP']}")
# Add Column
total_stats = df['HP'] + df['Att']
df['Total'] = total_stats
# Add Column 2nd method
df.loc[df['Total'] >= 100, 'Status'] = 'Normal'
df.loc[df['Total'] <= 100, 'Status'] = 'Anomaly'
print(df)
# df = df.drop(df['Total'])
print(df)
# Change data
df.loc[2, 'Name'] = 'Charmender'
print(df)
# Group and Aggregate
## Group
df_group = df.groupby(['Type 1'])
print(df_group)
## Aggregate
df_agg = df.groupby('Type 1').agg({
    'HP': ['count', 'min', 'max', 'mean']
})
print(df_agg)
df_count = df.groupby('Type 1').count()
print(df_count)
df_mean = df.groupby('Type 1').mean(numeric_only=True)
print(df_mean)
df_min = df.groupby('Type 1').min(numeric_only=True)
print(df_min)
df_max = df.groupby('Type 1').max(numeric_only=True)
print(df_max)

for rows in df.iterrows():
    rows['HP'] += 10

print(df)