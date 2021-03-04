from flask import Blueprint, render_template

verifikasi_view = Blueprint('verifikasi_view', __name__)


@verifikasi_view.route('/iuranbulanan')
def iuranbulanan():
    return render_template('verifikasi/iuranbulanan.html')


@verifikasi_view.route('/iurankas')
def iurankas():
    return render_template('verifikasi/iurankas.html')


@verifikasi_view.route('/wargabaru')
def wargabaru():
    return render_template('verifikasi/wargabaru.html')
