import pandas as pd

songs = pd.read_csv('./Spotify/data.csv')
print(songs.columns)
print(songs.head()[['name', 'artists']])

weeks = pd.read_csv('./BillboardFromLast20/spotifyWeeklyTop200Streams.csv')
print(weeks.columns)
print(weeks.shape)

weeks = weeks.drop_duplicates(subset=['Name', 'Artist'])
print(weeks.head())
print(weeks.shape)
combined = weeks.merge(songs, how='left', left_on='Name', right_on='name')
for row in combined.loc[combined['artists'].isnull(), 'artists'].index:
    combined.at[row, 'artists'] = []
print(combined.head(10)[['artists']])
combined = combined[combined.apply(
    lambda x: x['Artist'] in x['artists'], axis=1)]
combined = combined.drop_duplicates(subset=['Name', 'Artist'])
combined.to_csv('combined.csv')
print(combined.shape)

# df = pd.read_csv('combined.csv')
# print(df.shape)
