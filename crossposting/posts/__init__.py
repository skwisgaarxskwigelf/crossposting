from flask import Blueprint

posts_page = Blueprint('posts_page', __name__)

from . import views