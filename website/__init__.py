import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cooking'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

session = db.session()


#mysql = MySQL()


#app.config['MYSQL_DATABASE_PASSWORD'] = '6xCQXFD8'
#app.config['MYSQL_DATABASE_DB'] = 'cooking'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)

#conn = mysql.connect()
#cursor = conn.cursor()
