from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators   #this is to handle the forms
from passlib.hash import sha256_crypt   #this is for encypting our passwords
import os
import pymysql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:C7nW8HJtlEuBftF95ALs@containers-us-west-31.railway.app:6301/railway'

db=SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))
	username = db.Column(db.String(30), unique=True)
	password = db.Column(db.String(150))
#	register_date = db.Column(db.String(20))
	
	def __init__(self, name, email, username, password):
		self.name = name
		self.email = email
		self.username = username
		self.password = password
#		self.register_date = register_date


# Variables to Connect to the database
#conn = pymysql.connect(host= "containers-us-west-96.railway.app",
#    port= 6155,
#    user= "seunjonathan",
#    password= "Gre@tness123",
#    charset= "utf8mb4",
#    cursorclass= pymysql.cursors.DictCursor,
#    database= "railway")


#Home
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#Registration Form class
#class RegisterForm(Form):
#    name = StringField('Name', [validators.Length(min=1, max=50)])
#    username  = StringField('Username', [validators.Length(min=4, max=25)])
#    email  = StringField('Email', [validators.Length(min=6, max=50)])
#    password  = PasswordField('Password', [
#        validators.DataRequired(),
#        validators.EqualTo('confirm', message='Passwords do not match')
#    ])
#    confirm = PasswordField('Confirm password')

#@app.route('/register', methods = ['GET', 'POST'])
#def register():
#    form = RegisterForm(request.form)
#    if request.method == 'POST' and form.validate():
#        name = form.name.data
#        email = form.email.data
#        username = form.username.data
#        password = sha256_crypt.encrypt(str(form.password.data))

@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    
    data = User(name, email, username, password)
    db.session.add(data)
    db.session.commit()
        
        
        
#create cursor
        #conn = pymysql.connect(conf)
#        cur = conn.cursor()
#        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
#        conn.commit()
#        conn.close()

#    flash('You are now registered and can log in', 'success')

        
    return redirect(url_for('index'))

#    return render_template('treg.html')
#    return render_template('register.html', form=form)



if __name__ == '__main__':    #saying if this flie was selected to run, execute whats below, but if it was ref as a library, dont run
    app.secret_key='secret123'
    app.run(debug=True, port=os.getenv("PORT", default=6155))
