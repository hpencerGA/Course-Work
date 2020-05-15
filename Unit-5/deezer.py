import requests
import json

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "5c1506d255msh3a068fd74628662p1ed5aajsn04920b5323ec"
    }

querystring = {"q":"eminem"}
eminem = requests.request("GET", url, headers=headers, params=querystring).json()

querystring = {"q":"cardi b"}
cardi_b = requests.request("GET", url, headers=headers, params=querystring).json()

querystring = {"q":"ed sheeran"}
ed_sheeran = requests.request("GET", url, headers=headers, params=querystring).json()

print(response.json)


song_count = {"eminem": len(eminem["data"]), "cardi_b": len(cardi_b["data"]), "ed sheeran":len(ed_sheeran["data"])}
explicit_count = {"eminem": 0, "cardi_b": 0, "ed sheeran":0}
album_list = {"eminem": [], "cardi_b": [], "ed sheeran":[]}
most_recent = {"eminem": 0, "cardi_b": 0, "ed sheeran":0}


for song in eminem["data"]:

    if song ["album"] not in album_list["eminem"]:
        album_list["eminem"].append(song["eminem"])
    
    if song ["explicit_count"]:
        explicit_count["eminem"] += 1

print(song_count["eminem"],len(album_list['eminem'],explicit_count["eminem"]))




'''
Build a playlist of 10 songs from these 3 artists. Take songs randomly from
each artist until you have 10. For each track store the artists name along
with the following data: id readable title title_short title_version
link duration rank explicit_lyrics explicit_content_lyrics
'''