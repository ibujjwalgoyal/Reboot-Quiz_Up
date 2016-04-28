
from flask import Flask, render_template,session,request
import MySQLdb 

app = Flask(__name__)
db = MySQLdb.connect ("localhost","root","root","student")
app.secret_key = 'F122r47j\3yX R~X@H!jmM]Lwf/,?KT'

@app.route("/")
def hello():
	data = {}
	cursor = db.cursor()
	cursor.execute("Select * from question order by rand() limit 1,6")
	data = cursor.fetchall()
	session['questions']=data
	session['Score']=0
	ques_number = 1
	print session['questions']
	return render_template("start.html",ques = ques_number)

@app.route("/ques/<int:ques_number>",methods=['GET','POST']) 
def call(ques_number):
	if ques_number==1:
		session['Score']=0
	#print request.json['Score']
	if request.method=='POST':
		try:
			session['Score']+=request.json['Score']
		except:
			session['Score']=request.json['Score']

	if session['questions'] is None:
		return "Empty"
	else:
		return render_template("template1.html",data = session['questions'],ques_number=ques_number)

@app.route("/end")
def end():
	try:
		print session['Score']
	except:
		pass
	return render_template("end.html",score=session['Score'])       

if __name__ == '__main__':
	app.run(debug=True)