import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://www.google.com/",
        client_id="952b08f3bcd94b958253654f830e3a94",
        client_secret="ad86a39612064a31bccc650336247fb5",
        show_dialog=True,
        cache_path="token.txt",
        username="31ml3mx7pqv7wzaoqz4o6z7owhfa",
    )
)
user_id = sp.current_user()["id"]


date =  input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)