from flask import Blueprint, render_template, request

login_view = Blueprint('login_view', __name__)


@login_view.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        return request.form
    return render_template('login/login.html')
