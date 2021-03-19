from flask import Flask
from views.login.login_view import login_view
from views.home.home_view import home_view
from views.konfirmasi.konfirmasi_view import konfirmasi_view
from views.verifikasi.verifikasi_view import verifikasi_view
from views.alert.alert_view import alert_view
from views.report.report_view import report_view
from uuid import uuid4
from views.login.user_view import user_view

BUKTI_BAYAR_IURAN = './static/upload/bukti_bayar_iuran'
BUKTI_BAYAR_KAS = './static/upload/bukti_bayar_kas'

app = Flask(__name__)
app.secret_key = uuid4().hex
app.config['BUKTI_BAYAR_IURAN'] = BUKTI_BAYAR_IURAN
app.config['BUKTI_BAYAR_KAS'] = BUKTI_BAYAR_KAS

app.register_blueprint(user_view, url_prefix='/userview')
app.register_blueprint(login_view, url_prefix='/auth')
app.register_blueprint(home_view)
app.register_blueprint(konfirmasi_view, url_prefix='/konfirmasi')
app.register_blueprint(verifikasi_view, url_prefix='/verifikasi')
app.register_blueprint(alert_view, url_prefix='/alert')
app.register_blueprint(report_view, url_prefix='/report')
# app.register_blueprint(user_view, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
