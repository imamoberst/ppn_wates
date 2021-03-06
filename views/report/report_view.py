from flask import Blueprint, render_template

report_view = Blueprint('report_view', __name__)


@report_view.route('/')
def home_report():
    return render_template('report/report.html')
