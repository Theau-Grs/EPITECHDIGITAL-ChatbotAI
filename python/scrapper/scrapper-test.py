import requests
import csv
import json
import html5lib
from bs4 import BeautifulSoup

API_TOKEN_FILE = open('token.txt', 'r')
API_TOKEN = API_TOKEN_FILE.read()
URL_BASE = 'https://api.the-odds-api.com/v4/sports/'

URL_REQUEST = URL_BASE + '?apiKey=' + API_TOKEN

request = requests.get(URL_REQUEST)
soup = BeautifulSoup(request.content, 'html.parser')
print(request.content)
print('///////////////////////////////\n')
print(soup)

