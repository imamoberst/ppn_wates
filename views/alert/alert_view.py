from flask import Blueprint

alert_view = Blueprint('alert_view', __name__)


@alert_view.route('/allalert')
def allalert():
    return 'allaert'
