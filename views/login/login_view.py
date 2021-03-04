from flask import Blueprint, render_template, request
import json
from models.warga.warga import Warga

login_view = Blueprint('login_view', __name__)


@login_view.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        return request.form
    return render_template('login/login.html')


@login_view.route('/register', methods=['GET', 'POST'])
def register_warga():
    if request.method == 'POST':
        nama_depan = request.form['namadepan']
        nama_belakang = request.form['namabelakang']
        nik = request.form['nik']
        alamat_ktp = request.form['alamatktp']
        blok_ppn = request.form['blokppn']
        no_ppn = request.form['noppn']
        email = request.form['alamatemail']
        tempat_lahir = request.form['tempatlahir']
        tanggal_lahir = request.form['tanggallahir']
        no_hp = request.form['nohp']
        agama = request.form['agama']
        pekerjaan = request.form['pekerjaan']
        password = request.form['password']
        jumlah_penghuni = request.form['jmlpenghuni']
        rincian_penghuni = json.loads(request.form['datakel'])
        warga_obj = Warga(nama_depan, nama_belakang, nik, alamat_ktp, blok_ppn, no_ppn, email, tempat_lahir,
                          tanggal_lahir, no_hp, agama, pekerjaan, password, jumlah_penghuni, rincian_penghuni)
        cari_warga_ppn = warga_obj.find_one_warga_from_db()
        if cari_warga_ppn is None:
            warga_obj.save_one_to_db()
            messsage_succes = "Berhasil Mendaftar Dan Akan Di Verifikasi Oleh Petugas Terkait"
            return render_template('login/register.html', messsage_succes=messsage_succes)
        else:
            messsage_error = f"No Rumah {cari_warga_ppn['blok_ppn']}{cari_warga_ppn['no_ppn']} di PPN sudah terdaftar atas nama {cari_warga_ppn['nama_depan']} {cari_warga_ppn['nama_belakang']}"
            return render_template('login/register.html', messsage_error=messsage_error, data=request.form)
    return render_template('login/register.html')
