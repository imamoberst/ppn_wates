from flask import Blueprint, render_template
from models.warga.warga import Warga
from models.iuran_bulanan.iuran_bulanan import TahunIuran

verifikasi_view = Blueprint('verifikasi_view', __name__)


@verifikasi_view.route('/iuranbulanan')
def iuranbulanan():
    data = TahunIuran.find_all_iuran_warga()
    dataiuran = []
    for d in data:
        for tahun in d.iuran:
            for iuranbulan in tahun['iuranbulanan']:
                if iuranbulan['status'] == 'belum_bayar':
                    dataiuran.append(
                        {**iuranbulan, "norumah": d.norumah, "tahun": tahun['tahun'], "idwarga": d.idwarga})
    return render_template('verifikasi/iuranbulanan.html', data=dataiuran)


@verifikasi_view.route('/iurankas')
def iurankas():
    return render_template('verifikasi/iurankas.html')


@verifikasi_view.route('/wargabaru')
def wargabaru():
    data = Warga.find_one_warga_by_aktif()
    return render_template('verifikasi/wargabaru.html', data=data)
