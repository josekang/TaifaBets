import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SECRET_KEY"] = "ERTYUI#45678CVBNMWRETRYYUIOP@#$%^&*(+_)(*&^%$#DFGHJCVBN)"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager.__init__(app)
login_manager.login_view = "login"
