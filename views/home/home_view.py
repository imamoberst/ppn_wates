from flask import Blueprint, render_template

home_view = Blueprint('home_view', __name__)


@home_view.route('/')
def home_warga():
    return render_template('home/home.html')
