# Tech Report
## Where is the data from? ##
### Collection Method ###
First, we obtained weekly top 200 tracks from 12/23/2016 - 2/26/2021. This was done using Requests and BeautifulSoup on [Spotify Charts](https://spotifycharts.com/regional/us/weekly/latest). This gave us 218 csv files each with 200 tracks. We combined all of these csv files into one csv file using Pandas. 

After getting all the tracks, we obtained the tracks features using the Spotify Web API through the Spotipy library. Once again, we used Pandas to append the track features to each csv row containing a track. 

### Source Reputation ###
All the data comes from Spotify, and they are a reputable source. With over 50 million tracks and over 280 million active monthly users, they are the largest music streaming service with 36% claim of the global streaming market. Although we are assuming that music trends on Spotify are reflective of general music trends, we 
believe that the large user base will allow us to make this assumption. 

### About the Sample ### 
We simply took the first 50 rows. It is comparably small to the total tracks. It has a sampling bias since this is the top 50 tracks for the week of 2020-02-21 and will only capture the characteristics of popular music in early 2020. We considered taking a random sample of 50 tracks, but we believe that this sample of the first
50 rows is easier to interpret and gives a better intuitive sense of the data. 

### Other considerations ### 
We originally intended on joining two Kaggle datasets: one with the weekly tracks and another one with the track features. However, these datasets did not have Spotify IDs and joining by track name and artist name led to a loss of a lot of data. As a result, we switched to scraping and retreiving the data ourselves.





## How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? ##

We think that our data should be enough to complete the project we proposed. We have 43599 data points, 
each with more than 20 features. While we have enough data on songs that managed to become popular, 
we have no records of songs that failed to claim fame due to the nature of our sources. Data 
from the former group is more critical to our task than data from the latter, it would be 
ideal to have both. 

Only 5 rows out of 43599 are missing values. However, the missing values in these rows are usually 
the track name and artists, which are arguably the most important columns. We will throw these rows
out before we conduct analysis. There are no duplicate values. 

One small concern regarding the format of the data is that featuring artists are noted in the 
Track Name column, instead of the Artists column. (e.g. "Take What You Want (feat. Ozzy Osbourne & Travis Scott)" is the track name, and "Post Malone" is the artist.) We may want to parse the track name 
column to extract featuring arists and create a separate column for them. 

## Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. ##

One challenge we faced was that it was hard to find reliable data about the most recent music 
trends, specifically from TikTok. Since TikTok has recently driven so many songs up the charts,
we initially hoped to combine data from Spotify and TikTok, but found that the TikTok did not 
have an API as accessible and informative as Spotify's. However, our dataset is ripe with 
musical features to analyze, such as danceability, energy, key, loudness, acousticness, and more. 
We hope to fit a predictive model (the features are independent variables, and the popularity 
the dependent variable) like linear regression to our data. 