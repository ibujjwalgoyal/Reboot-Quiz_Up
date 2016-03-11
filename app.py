from flask import Flask
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import os
 
mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
 
@app.route("/")
def hello():
    return "Welcome to QuizUp!"

@app.route("/ques/<int:number>")
def Authenticate():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from login")
    data = cursor.fetchall()
    if data is None:
     return "404 error"
    else:
    	return "Successfull fetch"

if __name__ == '__main__':
	app.run(debug = True)


