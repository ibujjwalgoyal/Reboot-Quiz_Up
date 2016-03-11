from flask import Flask
import MySQLdb
from werkzeug import generate_password_hash, check_password_hash
import os
 
app = Flask(__name__)
db = MySQLdb.connect("localhost","root","root","student" )

@app.route("/")
def hello():
    return "Welcome to QuizUp!"

@app.route("/ques")
def Authenticate():
    cursor = db.cursor()
    cursor.execute("SELECT * from user")
    data = cursor.fetchall()
    if data is None:
     return "404 error"
    else:    	
    	for row in data:
    		print row,
    	return data[0][0]

if __name__ == '__main__':
	app.run(debug = True)


