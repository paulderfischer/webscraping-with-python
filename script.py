# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup
from bs4 import BeautifulSoup
import sys
import requests

if len(sys.argv) != 2:
    print('usage: python3 script.py <track query>')
    sys.exit(1)

# fetch website
page = requests.get(f'https://www.beatport.com/search?q={sys.argv[1]}')
# parse website
doc = BeautifulSoup(page.content, 'html.parser')

# find span with data in document
genre_elem = doc.find(
    'div', class_='buk-track-meta-parent').find('p', class_='buk-track-genre').a
# get elements text
genre = genre_elem.string

print(genre)
