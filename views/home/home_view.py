from flask import Blueprint

home_view = Blueprint('home_view', __name__)


@home_view.route('/')
def home_warga():
    return 'home warga'
