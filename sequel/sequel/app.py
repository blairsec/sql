from flask import Flask
from flask import request, session
from flask import redirect, render_template

import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'

def db():
	return sqlite3.connect('file:static.db?mode=ro', uri=True)

@app.route('/', methods=['GET'])
def index():
	if session.get('auth'):
		search = request.args.get('search', '')
		query = "SELECT title, author FROM sequels WHERE title LIKE '%" + search + "%'"
		try:
			result = list(db().cursor().execute(query))
		except Exception as e:
			result = [('error', e)]
		return render_template('index.html', search=search, result=result)
	return render_template('login.html')

@app.route('/', methods=['POST'])
def login():
	username = request.form.get('username', '')
	password = request.form.get('password', '')
	query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
	print(query)
	result = list(db().cursor().execute(query))
	print(result)
	if result:
		session['auth'] = True
	return redirect('/')

if __name__ == '__main__':
	app.run()
