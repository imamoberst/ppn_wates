from flask import Blueprint, render_template, request, redirect, url_for
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
    data = TahunIuran.find_all_iuran_warga()
    datakas = []
    for d in data:
        for tahun in d.iuran:
            for iurankas in tahun['iurankas']:
                if iurankas['status'] == 'belum_bayar':
                    datakas.append(
                        {**iurankas, "norumah": d.norumah, "tahun": tahun['tahun'], "idwarga": d.idwarga})
    return render_template('verifikasi/iurankas.html', data=datakas)


@verifikasi_view.route('/wargabaru')
def wargabaru():
    try:
        success = request.args['success']
    except:
        success = None
    data = Warga.find_one_warga_by_aktif()
    return render_template('verifikasi/wargabaru.html', data=data, success=success)


@verifikasi_view.route('/iuranbulanan_details')
def iuranbulanan_details():
    idwarga = request.args['idwarga']
    bulan = request.args['bulan']
    tahun = request.args['tahun']
    iuran_warga_obj = TahunIuran.find_one_warga_by_idwarga(idwarga)
    iuran_bulan_details = [iuran['iuranbulanan'] for iuran in iuran_warga_obj.iuran if iuran['tahun'] == tahun]
    data_iuran_bulan = {"idwarga": iuran_warga_obj.idwarga, "norumah": iuran_warga_obj.norumah, "tahun": tahun}
    for bulan_iuran in iuran_bulan_details[0]:
        if bulan_iuran['bulan'] == bulan:
            data_iuran_bulan = {**data_iuran_bulan, **bulan_iuran}
    return render_template('verifikasi/iuranbulanandetails.html', data=data_iuran_bulan)


@verifikasi_view.route('/iurankas_details')
def iurankas_details():
    idwarga = request.args['idwarga']
    bulan = request.args['bulan']
    tahun = request.args['tahun']
    iuran_warga_obj = TahunIuran.find_one_warga_by_idwarga(idwarga)
    iuran_kas_details = [iuran['iurankas'] for iuran in iuran_warga_obj.iuran if iuran['tahun'] == tahun]
    data_kas_bulan = {"idwarga": iuran_warga_obj.idwarga, "norumah": iuran_warga_obj.norumah, "tahun": tahun}
    for bulan_iuran in iuran_kas_details[0]:
        if bulan_iuran['bulan'] == bulan:
            data_kas_bulan = {**data_kas_bulan, **bulan_iuran}
    return render_template('verifikasi/iurankasdetails.html', data=data_kas_bulan)


@verifikasi_view.route('/warga_details', methods=['GET', 'POST'])
def warga_details():
    warga_obj = Warga.find_one_warga_by_id(request.args['idwarga'])
    if request.method == 'POST':
        warga_obj.aktivasi_warga()
        return redirect(
            url_for('.wargabaru',
                    success=f'Selamat Datang Warga Baru {warga_obj.blok_ppn}{warga_obj.no_ppn} - {warga_obj.nama_depan} {warga_obj.nama_belakang}'))
    return render_template('verifikasi/wargadetails.html', data=warga_obj)
