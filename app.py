from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    popular_movies_data = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=ca0668e9a773ee0bddc2b9e3a7fdacc7&language=en-US&page=1")
    popular_movies = json.loads(popular_movies_data.content)
    print(popular_movies)
    for movie in popular_movies['results']:
        print(movie['original_title'])
    return render_template('index.html', popular_movies=popular_movies)

@app.route('/movie/<int:Movie_id>')
def film_page(Movie_id):
    movie_id_str = str(Movie_id)
    api = f"https://api.themoviedb.org/3/movie/{Movie_id}?api_key=ca0668e9a773ee0bddc2b9e3a7fdacc7&language=en-US"
    #get json data from the api and pass it into the html page so that it can be accesed and printed to screen
    print(type(api))
    film_data_raw = requests.get(api)
    print(film_data_raw)
    film_data = "hello"
    film_data = json.loads(film_data_raw.content)
    
    return render_template('movie_page.html', film_data=film_data)

