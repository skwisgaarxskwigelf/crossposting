from flask import render_template

from . import index


@index.route('/')
def homepage():
    return render_template('index.html')
