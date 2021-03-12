from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from common.utils import Utlis
from flask import current_app as app
import os
from models.iuran_bulanan.iuran_bulanan import TahunIuran, Tahun, DataBulanan
from datetime import datetime
import json

konfirmasi_view = Blueprint('konfirmasi_view', __name__)


@konfirmasi_view.route('/iuranbulanan', methods=['POST', 'GET'])
def iuran_bulanan():
    try:
        idwarga = session['idwarga']
        norumah = session['norumah']
    except:
        return redirect(url_for('login_view.login_page'))
    #######START POST###########
    if request.method == 'POST':
        file = request.files['uploadbukti']
        print(request.form['databulan'])
        if request.form['databulan'] == 'kosong':
            return render_template('konfirmasi/iuranbulanan.html',
                                   error="Belum Pilih Bulan Pembayaran", data=request.form)
        databulan = request.form['databulan'].rsplit(',')
        if file and Utlis.allowed_file(file.filename):
            tahunbayar = request.form['tahunbayar']
            namapembayar = request.form['namapembayar']
            tanggalbayar = request.form['tanggalbayar']
            catatan = request.form['catatan']
            unik_name = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = secure_filename(f'{unik_name}_{file.filename}')
            file.save(os.path.join(app.config['BUKTI_BAYAR_IURAN'], filename))
            iuran_obj = TahunIuran.find_one_warga_by_idwarga(idwarga)
            if iuran_obj is not None:  # JIKA ADA IURAN
                tahun_fromdb = [d for d in iuran_obj.iuran if d['tahun'] == tahunbayar]
                if len(tahun_fromdb) == 0:
                    tahun_obj = Tahun(tahunbayar)
                    for bulan in databulan:
                        iuran_bulanan_obj = DataBulanan(bulan, catatan, tanggalbayar, namapembayar, filename)
                        tahun_obj.iuranbulanan.append(iuran_bulanan_obj.json())
                    iuran_obj.iuran.append(tahun_obj.json())
                    iuran_obj.update_db()
                else:
                    for bulan in databulan:
                        iuran_bulanan_obj = DataBulanan(bulan, catatan, tanggalbayar, namapembayar, filename)
                        tahun_fromdb[0]['iuranbulanan'].append(iuran_bulanan_obj.json())
                    iuran_obj.update_db()

                return redirect(url_for('home_view.home_warga', success="success"))
            else:  # JIKA TIDAK ADA IURAN
                tahuniuran_obj = TahunIuran(idwarga, norumah)
                tahun_obj = Tahun(tahunbayar)
                dataiuranbulanan = [DataBulanan(d, catatan, tanggalbayar, namapembayar, filename).json() for d in
                                    databulan]
                for iuranbulan in dataiuranbulanan:
                    tahun_obj.iuranbulanan.append(iuranbulan)
                tahuniuran_obj.iuran.append(tahun_obj.json())

                tahuniuran_obj.save_to_db()

                return redirect(url_for('home_view.home_warga', success="success!"))
    #######END POST###########
    try:
        bulan_from_home = request.args['bulan']
    except:
        bulan_from_home = None
    try:
        tahun_from_datetime = request.args['tahun']
    except:
        tahun_from_datetime = str(datetime.now().year)
    iuran_obj = TahunIuran.find_one_warga_by_idwarga(idwarga)
    if iuran_obj is None:
        return render_template('konfirmasi/iuranbulanan.html', bulan_from_home=bulan_from_home,
                               tahun=tahun_from_datetime)
    tahun_fromdb = [d for d in iuran_obj.iuran if tahun_from_datetime in d['tahun']]
    if len(tahun_fromdb) == 0:
        return render_template('konfirmasi/iuranbulanan.html', tahun=tahun_from_datetime,
                               bulan_from_home=bulan_from_home)
    else:
        bulan_data = []
        for bulan in tahun_fromdb[0]['iuranbulanan']:
            bulan_data.append(bulan['bulan'])
        return render_template('konfirmasi/iuranbulanan.html', dataiuran=json.dumps(bulan_data),
                               tahun=tahun_from_datetime, bulan_from_home=bulan_from_home)


@konfirmasi_view.route('/iurankas')
def iurankas():
    return render_template('konfirmasi/iurankas.html')
