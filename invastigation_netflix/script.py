# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv('netflix_data.csv')
netflix_subset = netflix_df[netflix_df['genre'] != 'International TV']

# Fixed the line below by completing the condition and closing the brackets
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]
print(netflix_movies.columns)
short_movies = netflix_movies[netflix_movies["duration"] < 60]

colors = []

for index, row in netflix_movies.iterrows():
    genre = row['genre']
    
    if genre == 'Children':
        colors.append('blue')
    elif genre == 'Documentaries':
        colors.append('green')
    elif genre == 'Stand-Up':
        colors.append('red')
    else:
        colors.append('gray') 
import matplotlib.pyplot as plt


fig, ax = plt.subplots()


ax.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)


ax.set_xlabel('Release year')
ax.set_ylabel('Duration (min)')
ax.set_title('Movie Duration by Year of Release')


plt.show()
answer = 'no'
