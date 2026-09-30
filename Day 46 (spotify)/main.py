import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic, OAuthCredentials

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36", 
}

response = requests.get(URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")

top_music = []
musics = soup.find_all("h3")

for songs in musics:
    music_chart = songs.getText()
    top_music.append(music_chart)
# print(top_music)

yt = YTMusic("browser.json")

playlist_id = None
playlist_name = f"{date} Billboard 100"


if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        playlist_name,
        f"Playlist with the hottest songs from {date}",
        privacy_status="PRIVATE",
    )
    print("Playlist created.")

print("Playlist ID:", playlist_id)
# print(top_music)
for song in top_music:
    try:
        search = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search[0]["videoId"]])
        # print("song", song)
        # print("search", search)    
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")
# playlists = yt.get_library_playlists()
# print(f"Found {len(playlists)} playlists in your library.")