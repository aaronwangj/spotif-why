# Socio-historical Context and Impact Report

## Socio-historical Context ##
### Societal Factors ###
A few societal factors that could affect our prediction goal/hypothesis are:
* The correlation of race, musical popularity, and genres: Musical preferences differ across cultures and races- therefore, generalizing popularity based on musical parameters might be an incorrect approach. There might be different attributes that appeal to different races, and being able to understand those, along with the context of emergence of individual genres, might help us better understand what’s contributing to popularity. For example- certain genres emerge as forms of protest/rebellion against oppressive authorities, while others are linked to spirituality. For minority communities, their preferred form of music might not be popular for the general population, but ignoring this nuance will lead to an incorrect interpretation of what it means for music to be popular. This intertwining of race, popularity, and genres is evidenced in an article by Marshall and Naumann where they conclude “people have strong racial associations with certain music genres and thus may use music preferences to communicate about their racial identities.”
* Gender bias in the music industry: The American music industry deals with a huge amount of gender inequality. Women make up a tiny fraction of artists, songwriters, producers etc. As an Forbes’ article explains, women’s work is often discredited and dismissed, and they are often stereotyped and sexualized. Given this, it is likely that our data will be predominated by male artists and making a model like this, will reinforce the bias- because it will reaffirm the status quo instead of making way for change.

### Major Stakeholders ###
The major stakeholders in our project are the same as the major stakeholders in the music industry. These include singers, musicians, producers, songwriters, record labels, and consumers. Our project, if successful, directly impacts these stakeholders. It helps establish a baseline for what makes a song popular- thereby impacting who record labels and producers give work to among singers, musicians, and songwriters, and who consumers get to listen to. 

The project could both harm and benefit singers, musicians, and songwriters because it would tend to reinforce the status quo- giving more work to the already recognized artists and less work to upcoming ones. However, it can help highlight some underappreciated artists whose songs have the potential to become popular but they are not being given the chance to rise up- in this way, it could also help shatter the status quo.

### Impact of Research Findings on Our Project ###
In addition, we should present our results with a disclaimer - that they help determine general popularity and not race/culture specific one. A better determination of popularity would occur by looking at each genre in isolation, and for each genre looking at its popularity within each race. This kind of detailed analysis is beyond the scope of our project but is imperative for a better determination of popularity.

## Ethical Considerations ##
### Underlying Historical or Societal Biases ###
We can note that our data contains underlying societal biases, in that the systems and processes used to collect the data were biased towards certain groups. The most obvious of these biases is linguistic; both Billboard and Spotify are both companies based in English-speaking countries, and thus our data contains mainly songs written in English. This bias excludes many popular songs from non-English speaking countries where the music industry is particularly large, including India, China, and Korea.

### Interpretation Biases ###
Because we are using data from Spotify, we are assuming that the popularity index that Spotify creates for each song is ground truth; that is, we assume that Spotify’s popularity algorithm is an unbiased estimator of the true popularity of any given song. Thus, this will influence all results that we obtain from our regression analysis.

Because our project group consists entirely of Gen Z consumers of Spotify, we can use our identities to help understand any trends that we see emerge from our data. This informative approach to analysis will help us connect the dots outside of simply analyzing the causes of correlation (such as omitted variable bias, confounding variables, etc.)

### Is data being used in a manner agreed to by the individuals who provided the data? ###
Somewhat. If we consider Spotify as the "individual" providing the data, then we believe Spotify would have no issues with an analysis of popular music. Easy access to popularity charts and also providing a Web API makes it seem that Spotify wants developers to explore their data. On the other hand, we do not think any artist who releases music on Spotify explicitly consented to being a part of popularity analysis. However, we also think that artists would not be surprised to see their music be analyzed especially if it becomes popular. Even then, if this popularity prediction were to become an industry standard, we believe there would be artists who believe that their music was used for the wrong purposes and would disagree with being a part of the algorithm.

### Possible Misinterpretations or Misuses ###
Any possible misinterpretations of our project results would undoubtedly stem from the confusion between correlation and causation. For example, our project may find that there is a strong correlation between the race of an artist and the popularity of the artist’s song. People may misinterpret this result and instead believe that being one race or another boosts the chance of a song being popular, which is not true. We may also find that of the people who write popular songs, more of them are male than female, and thus there is a correlation between gender and song popularity. This does not imply that men write more popular songs, or that female artists are worse than male artists; these misinterpretations can be devastating if not prevented properly. In order to prevent such misinterpretations, we can include a “project results analysis” section which dissects what we found in our project. This way, we can push the correct narrative, thereby decreasing the prevalence of any possible misinterpretations of our project results.


## Works Cited ## 
* Marshall, Shantal R., and Laura P. Naumann. “What’s Your Favorite Music? Music Preferences Cue Racial Identity.” Journal of Research in Personality, vol. 76, 2018, pp. 74–91. Crossref, doi:10.1016/j.jrp.2018.07.008.

* Kelley, Caitlin. “The Music Industry Still Has A Long Way To Go For Gender Equality.” Forbes, 28 Apr. 2019, www.forbes.com/sites/caitlinkelley/2019/02/06/music-industry-study-annenberg-gender-equality/?sh=6180e37a5f81.

* Leight, E. (2020, August 13). The music industry was built on Racism. changing it will take more than donations. Retrieved March 07, 2021, from https://www.rollingstone.com/music/music-features/music-industry-racism-1010001/
