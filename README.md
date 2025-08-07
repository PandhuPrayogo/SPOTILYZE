# SPOTILYZE: Analyze Your Spotify Activity

**See Your Spotify Listening Habits in a Simple Way**

---

## Table of Contents

1. About
2. Features
3. Requirements
4. Installation
5. Project Structure
6. Examples

---

## About

SPOTILYZE is a Python tool that helps you understand your Spotify listening history. It takes your Spotify data and shows you what songs and artists you listen to the most, when you listen, and how often you skip or finish songs.

---

## Features

- **Easy Data Loading:** Quickly load your Spotify streaming history (JSON file).
- **Top Songs & Artists:** Find out your most-played songs and favorite artists.
- **Play Status:** See if you usually skip, partially play, or fully play songs.
- **Listening Trends:** Check what time of day and which days you listen to music the most.
- **CSV Output:** Get a detailed CSV file with all your analyzed data.
- **NEW: Data Visualization (v1.3):** See your listening habits with easy-to-read charts using matplotlib.  
  You can view bar charts and histograms for your top songs, artists, play durations, and listening times.

---

## Update v1.3

**What’s new:**

- Added feature to visualize your Spotify data with matplotlib charts.
- Now you can see your listening patterns in colorful graphs, making your data easier to understand.
- Make sure you have installed the required libraries:
  ```
  pip install matplotlib numpy pandas
  ```

...

## Requirements

You need these to run SPOTILYZE:

### Software

- **VS Code:** Version 1.57 or newer
- **Python:** Version 3.1 or newer
- **Pandas Library:** Version 1.2.0 or newer

### Data

You need your [Spotify Extended Streaming History](https://www.spotify.com/us/account/privacy/).

**How to get your data:**

1. Go to the Spotify Privacy Settings page and log in.
2. Request your "Extended Streaming History.
3. Spotify will email you a ZIP file in 1-7 days.
4. Unzip it and find files like `StreamingHistory_music_0.json`, `StreamingHistory_music_1.json`. Pick one to use.

---

## Installation & Usage

1. **Download the Project:**  
   Open your terminal or command prompt and run:
   ```bash
   git clone https://github.com/PandhuPrayogo/SPOTILYZE.git
   ```
2. **Install Python:**  
   Download from [python.org](https://www.python.org/downloads/)
3. **Install Pandas:**  
   In your terminal, run:
   ```bash
   pip install pandas
   ```
4. **Open in VS Code:**  
   Open the project folder in VS Code. Check your Python and Pandas versions:
   ```bash
   python --version
   ```
   ```python
   import pandas as pd
   print(pd.__version__)
   ```
5. **Add Your Data:**  
   Put your `StreamingHistory_music_X.json` file in the `folder_file/` folder.
6. **Set the File Name:**  
   Open `scripts/spotify_analyst.py` and change the `file_path` variable to match your JSON file name.
7. **Run the Script:**  
   In the `scripts/` folder, run:
   ```bash
   python spotify_analyst.py
   ```

---

## Project Structure

```
SPOTILYZE/
├── folder_file/
│   └── StreamingHistory_music_1.json    # Your Spotify data
├── results/
│   └── final_result.csv                 # Output file
├── scripts/
│   └── spotify_analyst.py               # Main script
└── README.md                            # This file
```

**What’s in your data file:**

- `endTime`: When the song finished playing
- `msPlayed`: How long you listened (in milliseconds)
- `artistName`: Artist or band name
- `trackName`: Song title

---

## Examples

**Top Rows of Data:**

```
             endTime                  artistName              trackName  msPlayed
0 2025-01-06 02:45                   GFRIEND           Sunny Summer      1230
1 2025-01-06 02:45  Red Velvet - IRENE & SEULGI                Jelly      1068
2 2025-01-06 02:49                   GFRIEND            FINGERTIP     210102
```

**Most Played Songs:**

```
trackName
Memories of Summer    138
Season of Memories    111
Butterflies            79
...
```

**Most Listened Artists:**

```
artistName
Red Velvet    628
GFRIEND       445
TWICE         383
...
```

**Play Duration Status:**

```
             endTime    artistName    trackName    msPlayed    Real Time    Status
0 2025-01-06 02:45    GFRIEND       Sunny Summer  1230        1.230        Skipped
1 2025-01-06 02:45    Red Velvet    Jelly         1068        1.068        Skipped
2 2025-01-06 02:49    GFRIEND       FINGERTIP     210102      210.102      Full Play
...
```

**Listening Trends by Time:**

```
Hour
21      2
22    137
17    155
...
Day
Friday      1093
Sunday      1119
...
```

**Final Data Example:**

```
endTime              artistName    trackName    msPlayed    Real Time    Status      Hour    Day
2025-01-06 02:45     GFRIEND       Sunny Summer 1230        1.230        Skipped     2       Monday
...
```

---

## Support

If you like this project, you can support me or give feedback!  
Buy me a coffee: [https://saweria.co/Yewonnie](https://saweria.co/Yewonnie)
