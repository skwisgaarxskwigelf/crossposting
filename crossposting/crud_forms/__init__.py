from flask import Blueprint

crud_forms = Blueprint('crud_forms', __name__)

from . import views
