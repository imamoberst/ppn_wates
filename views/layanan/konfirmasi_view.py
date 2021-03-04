from flask import Blueprint, render_template

konfirmasi_view = Blueprint('konfirmasi_view', __name__)


@konfirmasi_view.route('/iuranbulanan')
def iuran_bulanan():
    return render_template('layanan/konfirmasi.html')


@konfirmasi_view.route('/iurankas')
def iurankas():
    return render_template('layanan/iurankas.html')
