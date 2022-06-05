import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = flask.Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cooking'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://skjelkjuitnsni:ddab36c82a87dd55a3612302fdee487e0eea5f11dd11449e322053edf74de0c5@ec2-52-48-159-67.eu-west-1.compute.amazonaws.com:5432/d4f1evpqdmj7ks'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

session = db.session()

