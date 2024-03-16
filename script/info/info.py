import requests
import json
import os
import tmdbsimple as tmdb
from icecream import ic

from model import Movie

tmdb.API_KEY = 'eb21fed20fe45dd84ca95914f57fcc86'
tmdb.REQUESTS_TIMEOUT = 5

HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYjIxZmVkMjBmZTQ1ZGQ4NGNhOTU5MTRmNTdmY2M4NiIsInN1YiI6IjY1ZjU3MWFhZDRkNTA5MDE0OWFhNjg3ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.d9ypY-ljv763VJWL9HDCbe5DRvzq4dpMDE7aYIozW7I"
}

DEFAULT_METADATA_URL = "https://api.themoviedb.org/3/movie/680?language=en-US"
DEFAULT_CREDITS_URL = "https://api.themoviedb.org/3/movie/680/credits?language=en-US"

def get_metadata(METADATA_URL=DEFAULT_METADATA_URL):
    response = requests.get(url=METADATA_URL, headers=HEADERS).text
    return json.loads(response)

def get_credits(CREDITS_URL=DEFAULT_CREDITS_URL):
    response = requests.get(url=CREDITS_URL, headers=HEADERS).text
    raw_credits_json = json.loads(response)
    # print(raw_credits_json.get('cast'))
    ret_credits_str = json.dumps(raw_credits_json.get('cast'))
    return json.loads(ret_credits_str)

def test():
    search = tmdb.Search()
    response = search.movie(query='Pulp Fiction')
    result = search.results[0]
    ic(result)
    
    movie = tmdb.Movies(result['id'])
    response = movie.info()
    response = movie.releases()
    ic(movie)
    ic(dir(movie))


def dump_info(movie_title):
    search = tmdb.Search()
    response = search.movie(query=movie_title)
    result = search.results[0]
    
    MOVIE_ID = result['id']
    METADATA_URL = f"https://api.themoviedb.org/3/movie/{MOVIE_ID}?language=en-US"
    CREDITS_URL = f"https://api.themoviedb.org/3/movie/{MOVIE_ID}/credits?language=en-US"
    
    movie = Movie(get_metadata(), get_credits())
    return movie.to_json()



if __name__ == '__main__':
    # test()
    # metadata_str = get_metadata()
    # print(metadata_str)
    # metadata_json = json.loads(metadata_str)
    # print(metadata_json)
    # print(type(metadata_json))
    # print(type(metadata_str))

    # credits_str = get_credits()
    # print(credits_str)

    movie_title = input('enter movie title: ')
    OUTPUT_PATH = './sample.json'
    with open(OUTPUT_PATH, 'r+') as f:
        f.write(dump_info(movie_title))
        f.flush()
