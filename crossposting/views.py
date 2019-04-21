from crossposting import app
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@app.route('/')
def index():
    return render_template('home.html')


