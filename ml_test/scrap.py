import requests
from bs4 import BeautifulSoup

# Get the HTML content of the BBC news webpage
url = 'https://www.bbc.com/news'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the news headlines
headlines = soup.find_all('h3')

# Print the headlines
for headline in headlines:
    print(headline.text)
