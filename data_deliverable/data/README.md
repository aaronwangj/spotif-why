# Data Spec
Top weekly tracks and their features are in the file `weekly_tracks.csv`

[Link to download `weekly_tracks.csv`](https://drive.google.com/file/d/1qOpQ5nFf4N0ftxQbaPqnsU336Lq4z2CE/view?usp=sharing)

The sample of this data is in the file `weekly_tracks_sample.csv`

---------------------------------------------------------------------------

## I. Where the top weekly tracks and features are from ##

The tracks were scraped from US weekly rankings from [Spotify Charts](https://spotifycharts.com/regional/us/weekly/latest). The features were obtained from the [Spotify Web API](https://developer.spotify.com/documentation/web-api/).

## II. Format of the tracks ##

Each line in the file contains one track.  Below is an example:

Attribute | Value
------------- | -------------
Position | 1
Track Name | The Box
Artist | Roddy Ricch
Streams | 15981992
Week | 2020-02-21
id | 0nbXyq5TXYPCO7pr3N8S4I
danceability | 0.8959999999999999
energy | 0.586
key | 10
loudness | -6.687
mode | 0
speechiness | 0.0559
acousticness | 0.10400000000000001
instrumentalness | 0.0
liveness | 0.79
valence | 0.642
tempo | 116.971
duration_ms | 196653
time_signature | 4
artists | ['Roddy Ricch']
explicit | True
popularity | 87
artist_ids | ['757aE44tKEUQEqRuT6GnEB']

Descriptions are largely based on the descriptions by [Spotify](https://developer.spotify.com/documentation/web-api/reference/#object-audiofeaturesobject)

* Position - integer, the track's position for the specified week
  
	This value will range from 1 to 200 since Spotify Charts displays the
  top 200 songs for the week.

* Track Name - string, the track's name

* Artist - string, the track's artist
  
  Does not include feature artists

* Streams - integer, the track's number of streams for the week

* Week - string, YYYY-MM-DD, the week the track was in the top 200

* id - string, the track's unique id according to Spotify

* danceability - float, how suitable a track is for dancing
  
  Based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity
  Between 0.0 and 1.0, with 0.0 being least danceable and 1.0 being most danceable

* energy - float, measure of track's intensity
  
  Based on loudness, timbre, and general entropy
  Between 0.0 and 1.0, with 0.0 being least energetic and 1.0 being most energetic

* key - integer, the track's key
  
  Uses [standard Pitch Class notation](https://en.wikipedia.org/wiki/Pitch_class)

* loudness - float, the track's loudness in decibels
  
  Values typical range between -60 and 0 db.

* mode - integer, the track's modality (major or minor)
  
  Major is represented by 1 and minor is 0.

* speechiness - float, the presence of spoken words on the track
  
  Between 0.0 and 1.0, with 0.0-0.33 mostly being music, 0.33-0.66 mostly being rap, and 0.66-1.0 have mostly spoken words

* acousticness - float, a confidence measure of whether the track is acoustic
  
  Between 0.0 and 1.0, with 0.0 being low confidence in acousticness and 1.0 being high confidence

* instrumentalness - float, predicts if a track has no vocals
  
  Between 0.0 and 1.0, with 0.0 being low likelihood of instrumental and 1.0 being high likelihood

* liveness - float, detects the presence of a live audience
  
  Between 0.0 and 1.0, with 0.0 being low likelihood that the track is live and 1.0 being high likelihood

* valence - float, detects the track's positivity
  
  Between 0.0 and 1.0, with 0.0 being low valence (sad, depressed, angry) and 1.0 being high valence (happy, cheerful)

* tempo - float, the overall estimated tempo of the track in beats per minute

* duration_ms - integer, the duration of the track in milliseconds

* time_signature - integer, the estimated time signature of the track
  
  Specifies how many beats are in a measure

* artists - list of strings, the artists on the track
  
  Includes feature artists

* explicit - boolean, if the track contains explicit language or not
  
  True means track is explicit, False means track is not explicit

* popularity - integer, the popularity of the track as of March 1st, 2021
  
  Based mostly on the total number of plays the track has had and how recent those plays are.

* artist_ids - string, list of artists' Spotify IDs


----------------------------------------------------------------------