
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
  ques_number = 1
  print session['questions']
  return render_template("start.html",ques = ques_number)

@app.route("/ques/<int:ques_number>") 
def call(ques_number):
    if session['questions'] is None:
      return "Empty"
    else:
      print ques_number
      return render_template("template1.html",data = session['questions'],ques_number=ques_number)

@app.route("/end")
def end():
    return render_template("end.html")       
if __name__ == '__main__':
  app.run(debug = True)


