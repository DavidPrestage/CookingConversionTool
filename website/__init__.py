import flask
from flaskext.mysql import MySQL

app = flask.Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '6xCQXFD8'
app.config['MYSQL_DATABASE_DB'] = 'cooking'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
