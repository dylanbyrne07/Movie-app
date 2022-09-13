from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

def rand_int():
    rand_int = random.randrange(0, 100)
    return "<p>hello</p>"
    