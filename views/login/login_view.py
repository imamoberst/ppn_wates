from flask import Blueprint, render_template, request, session, redirect, url_for
import json
from models.warga.warga import Warga

login_view = Blueprint('login_view', __name__)


@login_view.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        blokppn = request.form['blokrumah'].upper()
        password = request.form['password']
        warga_obj = Warga.is_valid_login(blokppn, password)
        if warga_obj:
            session['name'] = f'{warga_obj.nama_depan} {warga_obj.nama_belakang}'
            session['level'] = warga_obj.level
            session['idwarga'] = warga_obj._id
            session['norumah'] = f"{warga_obj.blok_ppn}{warga_obj.no_ppn}"
            return redirect(url_for('home_view.home_warga'))
        else:
            message = "Username or Password Salah"
            return render_template('login/login.html', message=message)
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
            warga_obj.hash_password()
            warga_obj.tanggal_awal_daftar()
            warga_obj.save_one_to_db()
            messsage_succes = "Berhasil Mendaftar Dan Akan Di Verifikasi Oleh Petugas Terkait"
            return render_template('login/register.html', messsage_succes=messsage_succes)
        else:
            messsage_error = f"No Rumah {cari_warga_ppn['blok_ppn']}{cari_warga_ppn['no_ppn']} di PPN sudah terdaftar atas nama {cari_warga_ppn['nama_depan']} {cari_warga_ppn['nama_belakang']}"
            return render_template('login/register.html', messsage_error=messsage_error, data=request.form)
    return render_template('login/register.html')


@login_view.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('.login_page'))


@login_view.route('/user_profile')
def user_profile():
    try:
        warga_obj = Warga.find_one_warga_by_blok(session['norumah'])
        return render_template('login/user_profile.html', data=warga_obj.json())
    except:
        return redirect(url_for('home_view.home_warga'))
