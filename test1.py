from flask import Flask, render_template
import MySQLdb 

app = Flask(__name__)
db = MySQLdb.connect ("localhost","root","root","student")

@app.route("/")
def hello():
	return "Welcome To Quiz Up"

@app.route("/ques")
def call():
	cursor = db.cursor()
	cursor.execute("Select * from question")
	data = cursor.fetchall()
	if data is None:
		return "Empty"
	else:
		for row in data:
			print str(row)
    	return render_template("template1.html",data = data)

if __name__ == '__main__':
	app.run(debug = True)



