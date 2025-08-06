# Angel Chavez
# Aug 4th, 2025
# Python 3.13.5
# program that visualizes viewer data using Matplotlib and Pandas

import pandas as pd
import matplotlib.pyplot as plt

# store my data as a list of dictionaries
tv_show_data = [
    {
        'title': 'the office',
        'genre': 'comedy',
        'viewers_millions': 300,
        'avg_watch_time': 160
    },
    {
        'title': 'breaking bad',
        'genre': 'drama',
        'viewers_millions': 60,
        'avg_watch_time': 100
    },
    {
        'title': 'mr robot',
        'genre': 'thriller',
        'viewers_millions': 50,
        'avg_watch_time': 80
    },
    {
        'title': 'common side effects',
        'genre': 'comedy',
        'viewers_millions': 20,
        'avg_watch_time': 40
    },
    {
        'title': 'webdev challenge',
        'genre': 'educational',
        'viewers_millions': 5,
        'avg_watch_time': 30
    },
    {
        'title': 'rick and morty',
        'genre': 'comedy',
        'viewers_millions': 500,
        'avg_watch_time': 160
    }
]

# converted my list of dics to a pandas dataframe for convience and ease
df = pd.DataFrame(tv_show_data)

# count the number of shows per genre
genre_count = df['genre'].value_counts()

# bar chart showing total viewers per show
plt.bar(df['title'].str.title(), df['viewers_millions'])
plt.xlabel('TV Show')
plt.ylabel('Viewers (Millions)')
plt.title('TV Show Viewership')
plt.xticks(rotation=30)     # Rotates x-axis labels by 30 degrees for better readability
plt.tight_layout()

# pie chart showing the proportion of shows by genre
plt.figure()    # creates a new figure for the pie chart
plt.pie(genre_count, labels=genre_count.index, autopct='%1.1f%%')
plt.title('Proportion of Shows by Genre')
plt.tight_layout()

# line chart showing average watch time per show
plt.figure()
plt.plot(df['title'].str.title(), df['avg_watch_time'])
plt.xlabel('TV Show')
plt.ylabel('Avg Watch Time (Minutes)')
plt.title('Average TV Show Watch Time')
plt.xticks(rotation=30)
plt.tight_layout()

plt.show()