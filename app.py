import sys
import random
from flask import Flask, render_template, jsonify, Markup
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'

db = SQLAlchemy(app)

BASECOORDS = [41.8781, -87.6298]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/grants')
def grants():
    return render_template('grants.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=80)
    app.run(debug=True)
