from flask import Blueprint, render_template, request, redirect, url_for
from models.warga.warga import Warga

user_view = Blueprint('user_view', __name__)


@user_view.route('/view')
def user():
    data = Warga.find_all()
    return render_template('login/user_view.html', data=data)


@user_view.route('/level')
def level():
    warga_obj = Warga.find_one_warga_by_id(request.args['idwarga'])
    warga_obj.update_level(request.args['level'])
    return redirect(url_for('.user'))
