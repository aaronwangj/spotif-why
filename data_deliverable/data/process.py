import os
import pandas as pd
import glob
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from progressbar import progressbar


def add_week():
    directory = './weekly/'
    for filename in os.listdir(directory):
        week = filename.split('--')[0]
        df = pd.read_csv(directory + filename)
        headers = df.iloc[0]
        new_df = pd.DataFrame(df.values[1:], columns=headers)
        new_df['Week'] = week
        # new_df.rename(columns={0: "Rank"}, inplace=True)
        new_df.drop(0, axis=1, inplace=True)
        # print(new_df)
        new_df.to_csv(directory+filename)


def combine():
    path = r'./weekly/'
    all_files = glob.iglob(os.path.join(path, "*.csv"))

    df_from_each_file = (pd.read_csv(f, index_col=0) for f in all_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
    print(concatenated_df.shape)
    print(concatenated_df.head())
    concatenated_df.to_csv('all_weekly.csv')


def get_features():
    load_dotenv()
    df = pd.read_csv('all_weekly.csv', index_col=0)
    print(df.shape)

    df.drop_duplicates('URL', inplace=True)
    print(df.head())
    print(df.shape)
    # return
    # url = df.iloc[0, 4]
    # print(os.getenv('SPOTIPY_CLIENT_ID'))
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    # ret = sp.audio_features(url)

    gen = [sp.audio_features(url) for url in progressbar(df['URL'])]

    gen = [item for sublist in gen for item in sublist]
    features_df = pd.DataFrame(gen)
    features_df.to_csv('all_features.csv')
    print(gen[:5])
    print(features_df.shape)


def get_tracks():
    load_dotenv()
    df = pd.read_csv('all_weekly.csv', index_col=0)
    df.drop_duplicates('URL', inplace=True)
    # return
    # urls = df.iloc[0:10, 4]
    # print(urls)
    # print(os.getenv('SPOTIPY_CLIENT_ID'))
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    tracks = [sp.track(url) for url in progressbar(df['URL'])]
    tracks = [{k: track.get(k, None) for k in ('artists', 'explicit', 'popularity', 'id')}
              for track in tracks]

    def filter_artists(track):
        artists = track['artists']
        artists_names = [artist['name'] for artist in artists]
        artist_ids = [artist['id'] for artist in artists]
        track['artists'] = artists_names
        track['artist_ids'] = artist_ids
        return track

    tracks = [filter_artists(track) for track in tracks]

    # tracks = [for track in tracks]  # explode artists

    # gen = [sp.audio_features(url) for url in progressbar(df['URL'])]

    # gen = [item for sublist in gen for item in sublist]
    tracks_df = pd.DataFrame(tracks)
    print(tracks_df)
    tracks_df.to_csv('all_tracks.csv')
    print(tracks[:5])
    print(tracks_df.shape)


def join():
    df = pd.read_csv('all_features.csv', index_col=0, usecols=['Unnamed: 0', 'danceability', 'energy', 'key', 'loudness', 'mode',
                                                               'speechiness', 'acousticness', 'instrumentalness', 'liveness',
                                                               'valence', 'tempo', 'id',
                                                               'duration_ms', 'time_signature'])
    print(df.columns)
    print(df.shape)
    print(df.head()[['id']])
    print(df.dtypes)

    weekly = pd.read_csv('all_weekly.csv', index_col=0)
    weekly['id'] = weekly['URL'].apply(lambda x: x.split('/')[-1])
    print(weekly.dtypes)
    joined = weekly.merge(df, how='left', on='id')
    print(joined.head())
    joined.to_csv('all_weekly_features.csv')


def join_artists():
    df = pd.read_csv('all_weekly_features.csv', index_col=0)
    tracks = pd.read_csv('all_tracks.csv', index_col=0)
    print(df.head()[['id']])
    print(tracks.head())
    joined = df.merge(tracks, how='left', on='id')
    print(joined.head())
    print(joined.columns)
    joined.to_csv('all_weekly_tracks.csv')


# unique_data()


# df = pd.read_csv('all_features.csv')
# # print(df[df['danceability'].isnull()])
# print(df.shape)

df = pd.read_csv('weekly_tracks.csv', index_col=0)
print(df.shape[0] // 200)
# sample = df[:50]
# sample.to_csv('weekly_tracks_sample.csv')
