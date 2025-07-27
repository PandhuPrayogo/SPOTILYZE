# SPOTILYZE: Analyze Your Spotify Activity

**Uncover Your Listening Habits**

---

## Table of Contents

1.  [About](https://www.google.com/search?q=%23about)
2.  [Features](https://www.google.com/search?q=%23features)
3.  [Requirements](https://www.google.com/search?q=%23requirements)
4.  [Installation](https://www.google.com/search?q=%23installation)
5.  [Project Structure](https://www.google.com/search?q=%23project-structure)
6.  [Examples](https://www.google.com/search?q=%23examples)

---

## About

Have you ever wondered about your unique music listening patterns? **SPOTILYZE** is a Python script designed to help you analyze your **Spotify streaming history**. In today's world, online music streaming is incredibly popular, and Spotify offers a rich dataset of user activity. This project focuses on analyzing that data to provide insights into your **listening habits**.

SPOTILYZE empowers casual listeners to transform their raw **Spotify JSON data** into meaningful insights. Discover your **top tracks**, identify **peak listening hours** and **days**, and understand how often you **skip** songs, partially listen, or enjoy **full plays**.

---

## Features

SPOTILYZE offers the following key features:

- **Data Loading & Preview:** Easily load and preview your **Spotify Extended Streaming History** data (in JSON format).
- **Most Played Analysis:** Quickly identify your **most-played tracks** and **top artists**.
- **Play Status Categorization:** Understand how you interact with songs by categorizing plays as **skipped**, **partial play**, or **full play**.
- **Listening Trends:** Visualize your **listening trends** based on the hour of the day and the day of the week.
- **Comprehensive Output:** Generates a detailed final output in CSV format for deeper **Spotify data analysis**.

---

## Requirements

To run SPOTILYZE, you'll need the following software and data:

### Software Requirements

- **VS Code:** Version 1.57 or newer (`x ≥ 1.57`)
- **Python:** Version 3.1 or newer (`x ≥ 3.1`)
- **Pandas Library:** Version 1.2.0 or newer (`x ≥ 1.2.0`)

### Data Requirements

You'll need your **Spotify Extended Streaming History** data. This is a JSON file containing your streaming activity.

- **How to Get Your Data:**
  1.  Visit the Spotify Privacy Settings page (you'll need to log in).
  2.  Follow the instructions to request your "Extended Streaming History."
  3.  Spotify will send a ZIP file containing your data to your registered email address. This process can take 1-7 days.
  4.  Inside the ZIP file, look for files named `StreamingHistory_music_X.json` (e.g., `StreamingHistory_music_0.json`, `StreamingHistory_music_1.json`). Choose the one you want to analyze.

---

## Installation & Usage

Follow these steps to set up and run SPOTILYZE:

1.  **Clone the Repository:** Open your command prompt, terminal, or Git Bash and navigate to the folder where you want to save the project. Then run:
    ```bash
    git clone https://github.com/PandhuPrayogo/SPOTILYZE.git
    ```
2.  **Install Python:** If you don't have Python installed, download it from the official website: [Python 3.13 Downloads](https://www.python.org/downloads/)
3.  **Install Pandas:** Open your command prompt, terminal, or Git Bash and install the pandas library:
    ```bash
    pip install pandas
    ```
4.  **Open in VS Code:** Launch VS Code. You can verify your Python and Pandas installations in the integrated terminal:
    ```bash
    python --version
    import pandas as pd
    print(pd.__version__)
    ```
5.  **Place Your Data:** Extract the `StreamingHistory_music_X.json` file you downloaded from Spotify. Place this file inside the `folder_file/` directory within your cloned `SPOTILYZE` project.
6.  **Update File Path:** Open the `spotify_analyst.py` script located in `scripts/`. Find the line `file_path = 'folder_file/StreamingHistory_music_1.json'` and change `StreamingHistory_music_1.json` to the exact name of your JSON file.
7.  **Run the Program:** Execute the script from your terminal within the `scripts/` directory:
    ```bash
    python spotify_analyst.py
    ```

---

## Project Structure

This project is organized as follows:

```
SPOTILYZE/
├── folder_file/
│   └── StreamingHistory_music_1.json    # Your Spotify streaming data (JSON)
├── results/
│   └── final_result.csv                 # Analyzed data output (CSV format)
├── scripts/
│   └── spotify_analyst.py               # The core analysis script
└── README.md                            # This README file
```

### DataFrame Structure from JSON Data:

The script processes your JSON data, which typically contains these key fields:

- **endTime:** The date and time when the track finished playing.
- **msPlayed:** How long you listened to the track, measured in milliseconds. (e.g., 300,000 ms = 300 seconds = 5 minutes).
- **artistName:** The name of the artist or band.
- **trackName:** The title of the song or track.

---

## Examples

Here's what the output looks like after running the SPOTILYZE script:

### Example: Top Rows of DataFrame

```
             endTime                  artistName              trackName  msPlayed
0 2025-01-06 02:45                   GFRIEND           Sunny Summer      1230
1 2025-01-06 02:45  Red Velvet - IRENE & SEULGI                Jelly      1068
2 2025-01-06 02:49                   GFRIEND            FINGERTIP     210102
3 2025-01-06 02:50                     I.O.I  Whatta Man (Good man)      59306
4 2025-01-06 02:51                     WENDY           The Road      61138
```

### Example: Bottom Rows of DataFrame

```
             endTime artistName             trackName  msPlayed
9702 2025-07-21 22:38       FLOW                COLORS    104675
9703 2025-07-21 22:40    GFRIEND    Season of Memories    148119
9704 2025-07-21 22:44      RIIZE      Boom Boom Bass     21508
9705 2025-07-21 22:44    GFRIEND             Eclipse    205013
9706 2025-07-21 22:46       QWER           FAKE IDOL     72773
```

### Example: Most Played Songs

```
trackName
Memories of Summer                138
Season of Memories                111
Butterflies                        79
Heaven                             69
Shhh!                              58
...
Baby Sleep BN Twelve                1
Cozy Brown Noise 125 Hz Q 0.5 - Seamless      1
Brown Noise Naps                    1
Calm and Steady Brown Noise         1
Brown Noise B                       1
Name: count, Length: 2582, dtype: int64
```

### Example: Most Listened Artists

```
artistName
Red Velvet             628
GFRIEND                445
TWICE                  383
アトラスサウンドチーム         316
VIVIZ                  255
...
IV Of Spades             1
Christian Kuria          1
Seo In Guk               1
Natsound                 1
Audioable Noise          1
Name: count, Length: 854, dtype: int64
```

### Example: Play Duration Status

```
             endTime                  artistName              trackName  msPlayed  Real Time      Status
0 2025-01-06 02:45                   GFRIEND           Sunny Summer      1230      1.230     Skipped
1 2025-01-06 02:45  Red Velvet - IRENE & SEULGI                Jelly      1068      1.068     Skipped
2 2025-01-06 02:49                   GFRIEND            FINGERTIP     210102    210.102   Full Play
3 2025-01-06 02:50                     I.O.I  Whatta Man (Good man)      59306     59.306   Full Play
4 2025-01-06 02:51                     WENDY           The Road      61138     61.138   Full Play
...                                     ...                  ...           ...        ...         ...   ...       ...
9702 2025-07-21 22:38                   FLOW                COLORS    104675    104.675   Full Play
9703 2025-07-21 22:40                GFRIEND    Season of Memories    148119    148.119   Full Play
9704 2025-07-21 22:44                  RIIZE      Boom Boom Bass     21508     21.508 Partial Play
9705 2025-07-21 22:44                GFRIEND             Eclipse    205013    205.013   Full Play
9706 2025-07-21 22:46                   QWER           FAKE IDOL     72773     72.773   Full Play
```

### Example: Listening Trends by Time

```
Hour
21      2
22    137
17    155
16    225
23    319
8     345
11    349
7     362
15    488
10    491
0     504
9     516
6     538
12    544
4     562
2     637
5     646
1     675
13    714
14    734
3     764
Name: count, dtype: int64
---
Day
Friday      1093
Sunday      1119
Thursday    1222
Tuesday     1390
Wednesday   1450
Monday      1639
Saturday    1794
Name: count, dtype: int64
```

### Example: Final Result DataFrame

```
                 endTime                  artistName              trackName  msPlayed  Real Time      Status  Hour       Day
0    2025-01-06 02:45:00                   GFRIEND           Sunny Summer      1230      1.230     Skipped     2    Monday
1    2025-01-06 02:45:00  Red Velvet - IRENE & SEULGI                Jelly      1068      1.068     Skipped     2    Monday
2    2025-01-06 02:49:00                   GFRIEND            FINGERTIP     210102    210.102   Full Play     2    Monday
3    2025-01-06 02:50:00                     I.O.I  Whatta Man (Good man)      59306     59.306   Full Play     2    Monday
4    2025-01-06 02:51:00                     WENDY           The Road      61138     61.138   Full Play     2    Monday
...                  ...                          ...                  ...       ...        ...         ...   ...       ...
9702 2025-07-21 22:38:00                      FLOW                COLORS    104675    104.675   Full Play    22    Monday
9703 2025-07-21 22:40:00                   GFRIEND    Season of Memories    148119    148.119   Full Play    22    Monday
9704 2025-07-21 22:44:00                     RIIZE      Boom Boom Bass     21508     21.508 Partial Play    22    Monday
9705 2025-07-21 22:44:00                   GFRIEND             Eclipse    205013    205.013   Full Play    22    Monday
9706 2025-07-21 22:46:00                      QWER           FAKE IDOL     72773     72.773   Full Play    22    Monday
```

---

## Support

Feel free to support my work and provide feedback\!
Buy me a coffee: [https://saweria.co/Yewonnie](https://saweria.co/Yewonnie)

---
