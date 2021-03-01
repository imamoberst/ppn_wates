from flask import Flask
from views.login.login_view import login_view

app = Flask(__name__)

app.register_blueprint(login_view, urlprefix='/login')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
