import re 
import requests 
from bs4 import BeautifulSoup 

site = 'https://www.wikipedia.org/' 

response = requests.get(site) 

soup = BeautifulSoup(response.text, 'html.parser') 
img_tags = soup.find_all('img') 

urls = [img['src'] for img in img_tags]

print(urls)