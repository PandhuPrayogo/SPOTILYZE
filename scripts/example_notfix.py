import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('folder_file/All_Pokemon.csv')

# Display the first 5 rows of the DataFrame
print("First 5 rows of the dataset:")
print(df.head())

# Get basic information about the DataFrame
print("\nInfo about the dataset:")
print(df.info())

# Get summary statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Example: Filter Pokémon with HP greater than 100
print("\nPokémon with HP > 100:")
print(df[df['HP'] > 100])

# Example: Group by 'Type 1' and get average Attack
print("\nAverage Attack by Type 1:")
print(df.groupby('Type 1')['Att'].mean())

# Example: Sort Pokémon by 'Speed' descending
print("\nTop 5 Strongest Pokémon:")
print(df.sort_values(by='Att', ascending=False).head())

# Save a filtered DataFrame to a new CSV file
filtered_df = df[df['Legendary'] == True]
filtered_df.to_csv('folder_file/Legendary_Pokemon.csv', index=False)
print("\nLegendary Pokémon saved to 'folder_file/Legendary_Pokemon.csv'")