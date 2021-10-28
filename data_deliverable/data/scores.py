import pandas as pd

df1 = pd.read_csv('clean.csv', index_col=0)

df1 = df1[['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'id',
           'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
           'popularity', 'speechiness', 'tempo', 'valence', 'Track Name', 'Artist']]
print(df1.shape)


df2 = pd.read_csv('data.csv', converters={'artists': eval})
df2 = df2[['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'id',
           'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
           'popularity', 'speechiness', 'tempo', 'valence', 'name', 'artists']]
print(df2.shape)
df2.rename(columns={'name': 'Track Name', 'artists': 'Artist'}, inplace=True)
df2['Artist'] = df2['Artist'].apply(lambda x: x[0])

combined = pd.concat([df1, df2])
# print(combined.size)
combined.drop_duplicates(subset=['id'], inplace=True)
combined = combined.sort_values('popularity', ascending=False).drop_duplicates(
    subset=['Track Name', 'Artist']).sort_index()
# print(combined.size)
# combined.to_csv('big_combined.csv')

# ids = df[df['popularity'] < 30][['id', 'popularity', 'artist_ids']]
# ids['id'] = ids['id'].apply(lambda x: f'https://open.spotify.com/track/{x}')
# ids.to_csv('links.csv')
# print(ids)

# df = pd.read_csv('weekly_tracks.csv', index_col=0)
