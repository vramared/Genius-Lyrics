import requests
from bs4 import BeautifulSoup

tok_file = open("tok", "r")
token = tok_file.read()
token = token.rstrip('\n')

base_url = "http://api.genius.com"
headers = {'Authorization': 'Bearer ' + token}
search_url = base_url + "/search?"

song_title = input("Enter Song Name: ")
#song_title = "SAD!"
params = {'q': song_title}
response = requests.get(search_url, params=params, headers=headers)
json = response.json()

url = json['response']['hits'][0]['result']['api_path']
song_path = base_url + url

get_lyrics = requests.get(song_path, headers=headers)
json_lyrics = get_lyrics.json()
path = json_lyrics['response']['song']['path']

page_url = "http://genius.com" + path
page = requests.get(page_url)
html = BeautifulSoup(page.text, "html.parser")
[h.extract() for h in html('script')]
lyrics = html.find("div", class_="lyrics").get_text()
print(lyrics)

#for x in json['response']['hits'][0]['result']['url']:
#	print(x)
