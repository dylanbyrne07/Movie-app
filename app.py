
from importlib import import_module
from flask import Flask, render_template, request, jsonify
import requests
import json
import urllib.parse
from random import randint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    popular_movies_data = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=ca0668e9a773ee0bddc2b9e3a7fdacc7&language=en-US&page=1")
    popular_movies = json.loads(popular_movies_data.content)
    return render_template('index.html', popular_movies=popular_movies)

@app.route('/search', methods=['POST'])
def search():
    name_searched_not_encoded = request.form['searched']
    name_searched_words = name_searched_not_encoded.split()
    name_searched = ""
    for word in name_searched_words:
        name_searched = name_searched + word + "+"
    name_searched = name_searched.rstrip(name_searched[-1])

    searched_api_url = f"https://api.themoviedb.org/3/search/movie?api_key=ca0668e9a773ee0bddc2b9e3a7fdacc7&language=en-US&query={name_searched}&page=1&include_adult=false"
    searched_movies_raw = requests.get(searched_api_url)
    searched_movies = json.loads(searched_movies_raw.content)
    image_strings = [""]
    for movie in searched_movies['results']:
        image = "https://image.tmdb.org/t/p/w500/" +  str(movie['poster_path'])
        image_strings.append(image)


    return render_template('search.html', searched_movies=searched_movies, name_searched_title=name_searched_not_encoded, image_strings=image_strings)

@app.route('/movie/<int:Movie_id>')
def film_page(Movie_id):
    movie_id_str = str(Movie_id)
    api = f"https://api.themoviedb.org/3/movie/{Movie_id}?api_key=ca0668e9a773ee0bddc2b9e3a7fdacc7&language=en-US&append_to_response=videos"
    #get json data from the api and pass it into the html page so that it can be accesed and printed to screen
    film_data_raw = requests.get(api)
    film_data = json.loads(film_data_raw.content)
    backdrop_img = str(film_data['backdrop_path'])

    if len(film_data['videos']['results']) > 0:
        rand_vid_num = randint(0, len(film_data['videos']['results'])-1 )
        rand_vid_key = film_data['videos']['results'][rand_vid_num]['key']
        no_video_avaliable = False
    else:
        rand_vid_key = "no"
        no_video_avaliable = True

    recomended_movies_raw_name = f"https://api.themoviedb.org/3/movie/{Movie_id}/recommendations?api_key=ca0668e9a773ee0bddc2b9e3a7fdacc7&language=en-US&page=1"
    recomended_raw = requests.get(recomended_movies_raw_name)
    recomended_movies = json.loads(recomended_raw.content)
    image_strings_recomendations = [""]
    for movie in recomended_movies['results']:
        image = "https://image.tmdb.org/t/p/w500/" +  str(movie['poster_path'])
        image_strings_recomendations.append(image)

    where_to_watch_raw = f"https://api.themoviedb.org/3/movie/{Movie_id}/watch/providers?api_key=ca0668e9a773ee0bddc2b9e3a7fdacc7"
    where_to_watch = requests.get(where_to_watch_raw)
    where_to_watch_json = json.loads(where_to_watch.content)

    return render_template('movie_page.html', film_data=film_data, recomended_movies=recomended_movies ,backdrop_img=backdrop_img, image_strings=image_strings_recomendations, where_to_watch_json=where_to_watch_json, rand_vid_key=rand_vid_key, no_video_avaliable=no_video_avaliable)

@app.route('/collection/<int:Collection_id>')
def collection(Collection_id):
    Collection_id_str = str(Collection_id)
    collection_api = f"https://api.themoviedb.org/3/collection/{Collection_id}?api_key=ca0668e9a773ee0bddc2b9e3a7fdacc7&language=en-US"
    collection_id_requests = requests.get(collection_api)
    collection_id_json = json.loads(collection_id_requests.content)

    image_strings = [""]
    for movie in collection_id_json['parts']:
        image = "https://image.tmdb.org/t/p/w500/" +  str(movie['poster_path'])
        image_strings.append(image)

    return render_template('collections.html', collection_id_json=collection_id_json, image_strings=image_strings  )

@app.route('/trending')
def trending():
    trending_raw = requests.get("https://api.themoviedb.org/3/trending/movie/week?api_key=ca0668e9a773ee0bddc2b9e3a7fdacc7")
    trending = json.loads(trending_raw.content)
    return render_template('trending.html', trending=trending, page_heading="Trending", page_name="trending")

@app.route('/top_rated')
def top_rated():
    top_rated_raw = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=ca0668e9a773ee0bddc2b9e3a7fdacc7&language=en-US&page=1")
    top_rated = json.loads(top_rated_raw.content)
    return render_template('top_rated.html', top_rated=top_rated, page_heading="Top rated", page_name="Top_rated")

@app.route('/to_search')
def to_search():
    return render_template('to_search.html')



if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)

