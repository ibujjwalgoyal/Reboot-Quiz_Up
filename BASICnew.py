import sqlite3 as sql
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = '~/home/GIT/Reboot-Quiz_up/database1.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
q = {}

@app.route('/')
def select_account_holder(params=()):
    con = sql.connect("DATABASE")
    cur = con.cursor()
    if params==():
        cur.execute("select * from login")
    else:
        string = "select"
        for i in xrange(len(params)-1):
            string += "%s,"
        string += "%s"
        string += " from login"

        result = cur.execute(string)
        con.close()
        return result.fetchall()



if __name__ == '__main__':
	app.run(debug = True)