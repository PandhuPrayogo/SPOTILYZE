# SPOTILYZE
# File: For best practice, place your data file in the 'folder_file' directory using JSON format.

## This script analyzes your Spotify 'Extended Streaming History' data using the pandas library.

## Libraries
import pandas as pd 

# --- Configuration ---
file_path = 'folder_file/StreamingHistory_music_1.json' # Change this to your file path
# ---------------------

## Main Program
print("# SPOTILYZE - ANALYZE YOUR SPOTIFY DATA")
print("--------------------------------------")
try:
  df = pd.read_json(file_path)
  print(f"'{file_path}' load succes\n")
  print("# Print the 5 rows top of the data frame")
  print("--------------------------------------")
  print(df.head().to_string()) # to_string = avoid cutting data print
  print("--------------------------------------\n")
  print("# Print the 5 rows bottom of the data frame")
  print("--------------------------------------")
  print(df.tail().to_string())
  print("--------------------------------------\n")
except FileNotFoundError:
  print(f"{file_path} not found. Please try again!")
  exit()
except Exception as e:
  print(f"{file_path} load error. Please change your file or try again!")
  exit()

## 1. Explore Data: Top and Bottom Rows
### You can adjust the number of rows displayed by changing the argument in `head()` and `tail()`.
print("## 1. Read the top and bottom of the data\n")
print("## 1a. Print top rows of the dataframe")
print("--------------------------------------")
print(df.head(5).to_string()) # Read the top 5 rows
print("--------------------------------------\n")
print("## 1b. Print bottom rows of the dataframe")
print("--------------------------------------")
print(df.tail(5).to_string()) # Read the bottom 5 rows
print("--------------------------------------\n")



## 2. Most Played Songs
# value_counts() sorts by default in descending order (most frequent first)
print("## 2. Read most played songs on data")
print("----------------- Most Played Songs ---------------------")
most_played = df['trackName'].value_counts() # Default: Descending
print(most_played)
print("--------------------------------------\n")


## 3. Most Listened Artists
print("## 3. Read most artist recently on data")
print("----------------- Most Artist Recently ---------------------")
most_artist = df['artistName'].value_counts()
print(most_artist)
print("--------------------------------------\n")

## 4. Analyze Play Duration
print("## 4. Status of Duration Played on data")
print("----------------- Status Played ---------------------")
#### Conditions: Categorizing songs based on `msPlayed`
df['Real Time'] = df['msPlayed'] / 1000
df.loc[df['msPlayed'] < 5000, 'Status'] = 'Skip'
df.loc[df['msPlayed'] >= 5000, 'Status'] = 'Partial Play' # Play not until end of the song
df.loc[df['msPlayed'] >= 45000, 'Status'] = 'Full Play'
#### Result: Displaying DataFrame with new 'Play Status' column
print(df)
print("--------------------------------------\n")

## 5. Listening Trends by Time
print("## 5. Tren based on time on data")

df['endTime'] = pd.to_datetime(df['endTime'])
df['Hour'] = df['endTime'].dt.hour # Return value using .dt and .hour used to extracting the hour (0-23)
df['Day'] = df['endTime'].dt.day_name() # Return value using .dt and .day_name used to extracting the day of the week as a string ("Monday" - "Sunday")
hour_listening = df['Hour'].value_counts() 
dayof_listening = df['Day'].value_counts() 
print("----------------- Hours in a day ---------------------")
print(hour_listening.sort_values()) # Defaul Descending
print("--------------------------------------\n")
print("----------------- Days in a week ---------------------")
# Define a specific order for days of the week
print(dayof_listening.sort_values()) 
print("--------------------------------------\n")

## 6. Final DataFrame Overview
print("## 6. Final Result")
print("----------------- Final Result ---------------------")
print(df) # Print 5 top and bottom of data

## Save Results
# Saving the final processed DataFrame to a CSV file in the 'results' folder.
df.to_csv('results/final_result.csv', index=False)
print("Your analyzed data has been saved to 'results/final_result.csv'")
