from flask import Flask
from views.login.login_view import login_view
from views.home.home_view import home_view

app = Flask(__name__)

app.register_blueprint(login_view, url_prefix='/auth')
app.register_blueprint(home_view)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
