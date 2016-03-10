import sqlite3
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
def connect_db():
    c = sqlite3.connect('DATABASE')
    cur = c.cursor()
    q = cur.execute('SELECT * FROM login')
    for row in q:
    	print row


if __name__ == '__main__':
	app.run(debug = True)

