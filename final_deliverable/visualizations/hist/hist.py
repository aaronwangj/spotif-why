import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../code//data/clean.csv')
df = df[['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness',
         'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo', 'valence']]

atts = ['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness',
        'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo', 'valence']
for att in atts:
    df.hist(column=att)
    plt.show()
    plt.savefig(f'hist_{att}.png')
