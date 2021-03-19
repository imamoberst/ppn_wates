from flask import Blueprint, render_template

user_view = Blueprint('user_view', __name__)


@user_view.route('/view')
def user():
    return render_template('login/user_view.html')
