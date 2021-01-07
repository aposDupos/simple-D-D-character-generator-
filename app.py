from flask import Flask, render_template, url_for, request, jsonify
import json
from static.script import randoming
from pathlib import Path

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['post', 'get'])
def add_data():
    race = request.form.get('select-race')
    sex = request.form.get('answer')
    randoming(race, sex)
    return race


if __name__ == '__main__':
    app.run()
