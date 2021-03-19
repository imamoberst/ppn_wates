from flask import Blueprint, render_template, request
from models.iuran_bulanan.iuran_bulanan import TahunIuran
from datetime import datetime
import json
from models.warga.warga import Warga

report_view = Blueprint('report_view', __name__)


@report_view.route('/')
def home_report():
    data = TahunIuran.find_all_iuran_warga()
    datasemuaiuran = []
    for d in data:
        datasemuaiuran.append(d.json())
    try:
        tahun = request.args['tahun']
    except:
        tahun = str(datetime.now().year)
    return render_template('report/report.html', data=datasemuaiuran, tahunreport=tahun)


@report_view.route('/warga')
def warga_report():
    warga_all_obj = Warga.find_all()
  
    return render_template('report/warga.html', data=warga_all_obj)


@report_view.route('/verifikasi')
def verifikasi():
    return render_template('report/verifikasi.html')
