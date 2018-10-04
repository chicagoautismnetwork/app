import sys
import os
import random
import markdown
from flask import Flask, render_template, jsonify, Markup
from flask.ext.misaka import Misaka
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Misaka(app,tables=True,autolink=True,wrap=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'

db = SQLAlchemy(app)

BASECOORDS = [41.8781, -87.6298]
md_dir = "Stories/"

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(md_dir, filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/blog')
def blog():
    content = get_file('our_autism_story.md')
    content = Markup(markdown.markdown(content))
    return render_template('blog.html',content=content)

@app.route('/grants')
def grants():
    return render_template('grants.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/about')
def about():
    return render_template('team.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/what_is_autism')
def what_is_autism():
    with open("Stories/autism_info.md", "r") as f:
        content = f.read()
    return render_template('markdown_render.html',content=content)

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=80)
    app.run(debug=True)
