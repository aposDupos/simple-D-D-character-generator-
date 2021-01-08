from flask import Flask, render_template, url_for, request, jsonify, redirect
import json
from static.script import randoming
from pathlib import Path

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['post','get'])
def add_data():
    race = request.form.get('select-race')
    sex = request.form.get('answer')
    params = randoming(race, sex)
    del params['sex']
    del params['race']
    return render_template('index.html', ready=1, params=params)


if __name__ == '__main__':
    app.run()
