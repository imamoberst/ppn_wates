from flask import Blueprint, render_template, session, redirect, url_for
from models.warga.warga import Warga

home_view = Blueprint('home_view', __name__)


@home_view.route('/')
def home_warga():
    try:
        warga_obj = Warga.find_one_warga_by_blok(session['norumah'])
        return render_template('home/home.html', data=warga_obj.iuran)
    except Exception as e:
        print(e)
        return redirect(url_for('login_view.login_page'))
    # return render_template('home/home.html')
