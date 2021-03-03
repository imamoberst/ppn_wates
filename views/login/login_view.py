from flask import Blueprint, render_template, request
import json

login_view = Blueprint('login_view', __name__)


@login_view.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        return request.form
    return render_template('login/login.html')


@login_view.route('/register', methods=['GET', 'POST'])
def register_warga():
    if request.method == 'POST':
        datakel = request.form['datakel']
        for d in json.loads(datakel):
            print(d)
        return request.form
    return render_template('login/register.html')
