import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Secret keys on 100 days notes

class spp:
    def __init__(self):
        self.client_id = CLIENT_ID,
        self.client_secret = CLIENT_SECRET,
        self.redirect_uri = REDIRECT_URL,
        self.scope = SCOPE

    def create_spotipy(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri=REDIRECT_URL,
                                                       scope=SCOPE))
        self.sp = sp

    def get_id(self):
        user_id = self.sp.me()['id']  # get user id
        self.user_id = user_id
        return user_id

    def liked_track(self):
        results = self.sp.current_user_saved_tracks()
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])

    def create_playlist(self, date):
        c_playlist = f"Top 100 hits | {date}"
        created_uri = self.sp.user_playlist_create(
            self.user_id,
            c_playlist ,
            public=False,
            description="A Test Playlist")["id"]
        print(created_uri)

        self.created_playlist_id = created_uri

    def search_song(self, song_inp):
        song = self.sp.search(song_inp, type="track", limit=1)
        song_uri = [song['tracks']["items"][0]["uri"]]  # ["id"] ["uri"]
        # print(song)
        # print(song_uri)
        self.song_found_uri = song_uri
        # return song_uri

    def add_song(self):
        self.sp.user_playlist_add_tracks(
            self.user_id, self.created_playlist_id, self.song_found_uri)

