import sys
import os
import random
import markdown
from flask import Flask, render_template, jsonify, Markup,  send_file
from flask_misaka import Misaka

app = Flask(__name__)
Misaka(app,tables=True,autolink=True,wrap=True)
md_dir = "Stories/"

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

@app.route('/downloadapp')
def downloadapp():
    file_path = 'static/files/ChiAutNet Grant Application.pdf'
    return send_file(file_path, attachment_filename='ChiAutNet Grant Application.pdf', as_attachment=True)

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
    app.run(host='0.0.0.0',port=80)
    #app.run(debug=True)
