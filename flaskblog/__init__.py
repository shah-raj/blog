import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from urllib.request import Request, urlopen, URLError
from urllib.parse import urlparse
from flask_oauth import OAuth
from decouple import config as conf


app = Flask(__name__)
# app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SECRET_KEY'] = conf('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
# app.config['MAIL_USERNAME'] = 'shahraj0299@gmail.com'
app.config['MAIL_USERNAME'] = conf('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = 'zhsndsqvihcpewaq'
app.config['MAIL_PASSWORD'] = conf('MAIL_PASSWORD')
mail = Mail(app)



# GOOGLE_CLIENT_ID = '517233664391-ktt2qhaaujr9go5trld3rblnd1t9t7lc.apps.googleusercontent.com'
GOOGLE_CLIENT_ID = conf('GOOGLE_CLIENT_ID')
# GOOGLE_CLIENT_SECRET = 'EUobNJSxxdIw4lTNCqVxodWQ'
GOOGLE_CLIENT_SECRET = conf('GOOGLE_CLIENT_SECRET')
REDIRECT_URI = '/oauth2callback'  # one of the Redirect URIs from Google APIs console
oauth = OAuth()

google = oauth.remote_app('google',
base_url='https://www.google.com/accounts/',
authorize_url='https://accounts.google.com/o/oauth2/auth',
request_token_url=None,
request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email','response_type': 'code'},
access_token_url='https://accounts.google.com/o/oauth2/token',
access_token_method='POST',
access_token_params={'grant_type': 'authorization_code'},
consumer_key=GOOGLE_CLIENT_ID,
consumer_secret=GOOGLE_CLIENT_SECRET)

from flaskblog import routes