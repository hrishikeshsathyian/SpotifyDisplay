import json
import requests
from info import access_token, spotify_user_id
from refresh import Refresh
from PIL import Image
import urllib.request

class CurrentSong:
    def __init__(self):
        self.user_id = spotify_user_id
        self.token = ""
    def call_refresh(self):
        print("refreshing code")
        refreshCaller = Refresh()
        self.token = refreshCaller.refresh()

    def get_current_song(self):
        #get current song playing in users spotify_user_id
        self.call_refresh()
        print("Finding Current Song Playing in Hrishis Spotify Account")
        try:
            query = 'https://api.spotify.com/v1/me/player/currently-playing'
            response = requests.get(query,
            headers={"Content-Type": "application/json",
                     "Authorization" : "Bearer {}".format(self.token)})
            response_json = response.json()

            print("Filtering Image URL")
            album_image = response_json["item"]["album"]["images"][0]["url"]
            track_name = response_json["item"]["name"]
            artist = response_json["item"]["album"]["artists"][0]["name"]
            print("You are listening to " + track_name + " by " + artist)
            print("Album Cover URL: " + album_image)
            urllib.request.urlretrieve(album_image,"current.png")
            img = Image.open('current.png')
            img.show()
        except:
            print("Oops! You are either disconnected or No Song Playing")

a = CurrentSong()
a.get_current_song()
