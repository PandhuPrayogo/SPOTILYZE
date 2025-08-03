# SPOTILYZE
# For best practice, place your data file in the 'folder_file' directory using JSON format.

## This script analyzes your Spotify 'Extended Streaming History' data using the pandas library.

## Libraries
import pandas as pd
import numpy as np 

# --- Configuration ---
file_path = 'folder_file/StreamingHistory_music_1.json' # Change this to your file path
# ---------------------

## Main Program
print("# SPOTILYZE - ANALYZE YOUR SPOTIFY DATA")
print("--------------------------------------")
try:
  df = pd.read_json(file_path)
  print(f"<'{file_path}' loaded successfully>\n")
  print("# Display the top 5 rows of the data frame")
  print("--------------------------------------")
  print(df.head().to_string()) # to_string = prevents truncated output
  print("--------------------------------------\n")
  print("# Display the bottom 5 rows of the data frame")
  print("--------------------------------------")
  print(df.tail().to_string())
  print("--------------------------------------\n")
# Exception handling
except FileNotFoundError:
  print(f"{file_path} not found. Please try again!")
  exit()
except Exception as e:
  print(f"Error loading {file_path}. Please change your file or try again!")
  exit()

# ...existing code...
print(f"{df.info()}\n")
### Check for missing values in each row
check_values = df.isnull()
print(f"{check_values.sum()}")
if check_values.sum().sum() == 0:
    print("Note: There are no missing values in this data.\n")
else:
    print("Note: Some rows have missing values.\n")
# ...existing code...

## 1. Explore Data: Top and Bottom Rows
### You can adjust the number of rows displayed by changing the argument in `head()` and `tail()`.
print("## 1. View the top and bottom of the data\n")
print("# 1a. Display the top rows of the dataframe")
print("----------------- Top 5 Rows ---------------------")
print(df.head(5).to_string()) # Display the top 5 rows
print("--------------------------------------\n")
print("# 1b. Display the bottom rows of the dataframe")
print("----------------- Bottom 5 Rows ---------------------")
print(df.tail(5).to_string()) # Display the bottom 5 rows
print("--------------------------------------\n")

## 2. Most Played Songs
# value_counts() sorts by default in descending order (most frequent first)
print("## 2. View the most played songs in the data")
print("----------------- Most Played Songs ---------------------")
most_played = df['trackName'].value_counts() # Default: Descending
print(most_played)
print("------------------ Conclusion --------------------")
print(f"-> Most Played Song: {most_played.head(1)}")
print(f"-> Least Played Song: {most_played.tail(1)}")
print("--------------------------------------\n")

## 3. Most Listened Artists
print("## 3. View the most listened artists in the data")
print("----------------- Most Listened Artists ---------------------")
most_artist = df['artistName'].value_counts()
print(most_artist)
print("------------------ Conclusion --------------------")
print(f"-> Most Played Artist: {most_artist.head(1)}")
print(f"-> Least Played Artist: {most_artist.tail(1)}")
print("--------------------------------------\n")

## 4. Analyze Play Duration
print("## 4. Analyze play duration in the data")
print("----------------- Play Duration Status ---------------------")
# Categorize songs based on `msPlayed`
df['Real Time'] = df['msPlayed'] / 1000
df.loc[df['msPlayed'] < 5000, 'Status'] = 'Skip'
df.loc[df['msPlayed'] >= 5000, 'Status'] = 'Partial Play' # Not played until the end
df.loc[df['msPlayed'] >= 45000, 'Status'] = 'Full Play'
# Display DataFrame with new 'Status' column
print(df)
# Use numpy to get mean, max, min, and std of msPlayed
msplayed = np.asarray(df['msPlayed'], dtype='i')
print("------------------ Conclusion --------------------")
print(f"-> Max value of msPlayed: {msplayed.max()}")
print(f"-> Min value of msPlayed: {msplayed.min()}")
print(f"-> Mean value of msPlayed: {int(msplayed.mean())}")
print(f"-> Std value of msPlayed: {int(msplayed.std())}")
print("--------------------------------------\n")

## 5. Listening Trends by Time
print("## 5. Trends based on time in the data")
df['endTime'] = pd.to_datetime(df['endTime'])
df['Hour'] = df['endTime'].dt.hour # Extract the hour (0-23)
df['Day'] = df['endTime'].dt.day_name() # Extract the day of the week as a string ("Monday" - "Sunday")
hour_listening = df['Hour'].value_counts() 
dayof_listening = df['Day'].value_counts()
print("# 5a. Trends based on hours in a day") 
print("----------------- Hours in a Day ---------------------")
print(hour_listening.sort_values()) # Ascending order
print("--------------------------------------\n")
print("# 5b. Trends based on days in a week") 
print("----------------- Days in a Week ---------------------")
# Display listening counts for each day of the week
print(dayof_listening.sort_values()) 
print("------------------ Conclusion --------------------")
print(f"-> Peak Hour: {hour_listening.head(1)}")
print(f"-> Lowest Hour: {hour_listening.tail(1)}")
print("--------------------------------------\n")

## 6. Final DataFrame Overview
print("## 6. Final Result")
# Clean Data Process
df = df.drop_duplicates(subset=['artistName', 'trackName']) # Remove duplicate data
df = df.drop(columns=['endTime', 'msPlayed'])
print("----------------- Final Result ---------------------")
final_result = df.sort_values(['artistName'], ascending=True)
print(final_result) # Show the DataFrame
# Summary Data Frame
conclusion = {
    "Top Artist": most_artist.head(1).index[0],
    "Top Song": most_played.head(1).index[0],
    "Total Real Time (sec)": int(df['Real Time'].sum()),
    "Peak Hour": hour_listening.head(1).index[0],
    "Peak Day": dayof_listening.head(1).index[0]
}
final_conclusion = pd.DataFrame([conclusion])
print(final_conclusion)
## Save Results
# Save the final processed DataFrame to a CSV file in the 'results' folder.
final_result.to_csv('results/final_result.csv', index=False)
print("Your analyzed data has been saved to 'results/final_result.csv'")