from flask import Blueprint, render_template, session, redirect, url_for, request
from models.iuran_bulanan.iuran_bulanan import TahunIuran
from datetime import datetime

home_view = Blueprint('home_view', __name__)


@home_view.route('/')
def home_warga():
    # start Message dari konfirmasi view jika sukses
    try:
        message = request.args['success']
    except:
        message = None
    # end Message dari konfirmasi view jika sukses

    # start jika ada tahun dari input tahun home
    try:
        tahun_from_datetime = request.args['tahun']
    except:
        tahun_from_datetime = str(datetime.now().year)
    # end jika ada tahun dari input tahun home

    # start cari 1 warga
    try:
        tahun_obj = TahunIuran.find_one_warga_by_idwarga(session['idwarga'])
        if tahun_obj is None:
            return render_template('home/home.html', data=[], tahun=tahun_from_datetime)
        tahun_fromdb = [d['tahun'] for d in tahun_obj.iuran if d['tahun'] == tahun_from_datetime]
        if len(tahun_fromdb) == 0:  # Jika tidak ada warga di db
            return render_template('home/home.html', data=tahun_fromdb, tahun=tahun_from_datetime)
        else:  # Jika ada warga di db
            datatahun = [d['iuranbulanan'] for d in tahun_obj.iuran if d['tahun'] == tahun_from_datetime][0]
            return render_template('home/home.html', data=datatahun, message=message, tahun=tahun_from_datetime)
    except Exception as e:
        print('error di home view home page => ', e)
        return redirect(url_for('login_view.login_page'))
    # end cari 1 warga
