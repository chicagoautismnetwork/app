import sys
import random
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'

db = SQLAlchemy(app)

BASECOORDS = [41.8781, -87.6298]

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/map')
#def map():
#    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
