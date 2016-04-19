from flask import Flask, render_template
from Tkinter import *
import time
import MySQLdb 

app = Flask(__name__)
db = MySQLdb.connect ("localhost","root","root","student")
root = Tk()
time1 = ''
clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)


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



