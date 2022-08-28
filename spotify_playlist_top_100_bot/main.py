from flask import redirect
import requests
from bs4 import BeautifulSoup
import re

from spotify import *


URL = "https://www.billboard.com/charts/hot-100/"


def get_song_list(date):
    input_date = date

    response = requests.get(URL + input_date + "/")
    website_html = response.text

    soup = BeautifulSoup(website_html, "html.parser")

    song_list = [] # EMPTY LIST
    for song in soup.find_all("h3" , id = "title-of-a-story" , class_ = re.compile("^c-title.a-no-trucate")): 
        song_list.append(song.get_text().rstrip().lstrip()) # r, l strip removes /n from the string scrapped
    
    return song_list


def main():
    inp_date = input("What Date do you like? YYYY-MM-DD : ")
    # inp_date = "2000-03-08"

    spot = spp()
    get_song_list(inp_date)

    spot.create_spotipy()
    spot.get_id()
    # spot.liked_track()
    spot.create_playlist(inp_date)

    for song in get_song_list(inp_date):
        spot.search_song(song)
        spot.add_song()


if __name__ == '__main__':
    main()