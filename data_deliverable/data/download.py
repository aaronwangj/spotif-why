import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen  # Python 3


r = requests.get(
    'https://spotifycharts.com/regional/us/weekly/2016-12-23--2016-12-30')
soup = BeautifulSoup(r.text, 'html.parser')


def weeks_filter(tag):
    return tag.has_attr('data-type') and tag['data-type'] == 'date'


all_dates = soup.find(weeks_filter).findAll('li')
all_dates = [x['data-value'] for x in all_dates]

for date in all_dates:
    a = Request(
        f"http://spotifycharts.com/regional/us/weekly/{date}/download")
    a.add_header('User-Agent',
                 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
    content = urlopen(a)
    df = pd.read_csv(content)
    df.to_csv(f'./weekly/{date}.csv')
