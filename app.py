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

@app.route('/<int:Movie_id>')
def film_page():
    return f"your movie id is {str(Movie_id)}"
