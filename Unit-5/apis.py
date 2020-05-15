#api is an application programming interface
#if see code 200 means that the data is there
#strings in JSON have to be double quotes
'''
import requests

response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

print(response.json())
#if organized as json you do response.json
#we are gonna focus on json organized  API's
'''

import requests
import json
import random   

url = "https://deezerdevs-deezer.p.rapidapi.com/search"
headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "d23b618a4cmsh1d6eb705ebd5503p1a74acjsnaf9ba0ec4cd9"
    }
querystring = {"q":"eminem"}
eminem = requests.request("GET", url, headers=headers, params=querystring).json()

querystring = {"q":"cardi b"}
cardi_b = requests.request("GET", url, headers=headers, params=querystring).json()

querystring = {"q":"ed sheeran"}
ed_sheeran = requests.request("GET", url, headers=headers, params=querystring).json()

song_count = { "eminem": len(eminem["data"]), "cardi b": len(cardi_b["data"]), "ed sheeran": len(ed_sheeran["data"])}
album_list = { "eminem": [], "cardi b": [], "ed sheeran": []}
explicit_count = { "eminem": 0, "cardi b": 0, "ed sheeran": 0}
most_recent_album = { "eminem": 0, "cardi b": 0, "ed sheeran": 0}

for song in eminem["data"]:
    if song["album"] not in album_list["eminem"]:
        album_list["eminem"].append(song["album"])
    if song["explicit_lyrics"]:
        explicit_count["eminem"] += 1
    #skipping year because it's not in the api

for song in cardi_b["data"]:
    if song["album"] not in album_list["cardi b"]:
        album_list["cardi b"].append(song["album"])
    if song["explicit_lyrics"]:
        explicit_count["cardi b"] += 1
    #skipping year because it's not in the api

for song in ed_sheeran["data"]:
    if song["album"] not in album_list["ed sheeran"]:
        album_list["ed sheeran"].append(song["album"])
    if song["explicit_lyrics"]:
        explicit_count["ed sheeran"] += 1
    #skipping year because it's not in the api

print(song_count["eminem"], len(album_list["eminem"]), explicit_count["eminem"])
print(song_count["cardi b"], len(album_list["cardi b"]), explicit_count["cardi b"])
print(song_count["ed sheeran"], len(album_list["ed sheeran"]), explicit_count["ed sheeran"])
url = "https://deezerdevs-deezer.p.rapidapi.com/album/103248"
eminem_show = requests.request("GET", url, headers=headers).json()
print(eminem_show["release_date"])


#empty list before the for loop

        #stop the list after 10 songs

#1) take the 3 lists and merge together 
#2)tell python to give random number between 0 and max number of list and grab song at that position 
#3)repeat 10 times  
#how to merge a list in python? 

song_list = eminem["data"] + cardi_b["data"] + ed_sheeran["data"] #Instead of creating seperate list, add them all together 
playlist = [] #new playlist where the 10 songs will go 

for i in range(0,10):                   #i is convention for an integer 
    index = random.randint(0,len(song_list))   #want to make it the length of the song list
    song_data = {}  #use dictionary to store some data 
    song = song_list[index]   #index is the random number between 0 and the last song 
    #Need to filter the fields so not to dump all if it in 
    song_data['artist'] = song['artist']['name']  #looked at the data and saw the artist name has to be accessed byusing the dict arist then name
    song_data['id'] = song['id']
    song_data['title_short'] = song['title_short']
    song_data['title_version'] = song['title_version']
    song_data['duration'] = song['duration']
    song_data['explicit_lyrics'] = song['explicit_lyrics']
    song_data['explicit_content_lyrics'] = song['explicit_content_lyrics']

    playlist.append(song_data) #add the song data to the playlist 
    

name, id readable title title_short title_version, link duration rank explicit_lyrics explicit_content_lyrics
         
songs = ['song1','song2', 's3']
songs[0]


'''
Build a playlist of 10 songs from these 3 artists. Take songs randomly from
each artist until you have 10. For each track store the artists name along
with the following data: id readable title title_short title_version
link duration rank explicit_lyrics explicit_content_lyrics
When building your playlist, you can generate a random number between 1 and
3 inclusive to determine which arrtist’s data you will pick from. Then, generate
another random number between 0 and the size of that artist’s data list to then
pick a song from the list.
Simply repeat this until you have ten items in your own playlist!
'''
