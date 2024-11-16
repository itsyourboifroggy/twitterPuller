# this is not useful but just practicing lol
import requests
from bs4 import BeautifulSoup

url = 'https://x.com/search?q=blue&src=typed_query'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
tweets = soup.find_all('p')

for tweet in tweets:
    text = tweet.get_text()
    print(text)