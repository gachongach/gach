from flask import render_template, Flask, request, url_for, current_app, flash, redirect
from apps import app
import random
import string
from google.appengine.api import mail
from models import User
from apps import db
import DAO


@app.route('/')
def index():
	return render_template("join.html")

from forms import *

@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template("login.html")

@app.route('/join', methods=['GET', 'POST'])
def join():
    return render_template("join.html")

@app.route('/user_join', methods=['GET', 'POST'])
def user_join():
    new_id = request.form['new_id']
    new_pw = request.form['new_pw']
    new_pwConfirm = request.form['new_pwConfirm']
    new_email = request.form['new_email']

    if new_pw != new_pwConfirm:
        return -1

    user = User(new_id, new_pw, 1, 0)

    if DAO.emailCheck(new_email) == False:
        return -1

    DAO.join(user)
    uniqueCode = createJoinCode()

    '''
    joining = joiningUsers(
        email=new_email,
        code = uniqueCode
    )
    '''
    #db.session.add(joiningUsers)
    #db.session.commit()

    sendEmail(new_email, new_id, uniqueCode)
    return render_template("index.html")

def createJoinCode():
    code  = ""
    for i in range(0, 32):
        code += random.choice(string.ascii_letters)
    return code

def sendEmail(address, userId,uniqueCode):
    fromAdd = "zeros19861@gmail.com"
    toAdd = address

    TO = [address] #must be a list
    SUBJECT = "Certify your account"
    TEXT = "Hello, " + userId + "\nTo certify your account" + ",click below link\n" + "http://gachongach.com/varify?code=" + uniqueCode

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
                """ % (fromAdd, ", ".join(TO), SUBJECT, TEXT)

    name = "gachongach"
    pw = "gachgachon2014"
    mail.send_mail(fromAdd, toAdd, SUBJECT, TEXT)

'''
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(name,pw)
    server.sendmail(fromAdd, toAdd, message)
    server.quit()
'''
	#GET

	# #old codes 
	# post_data = request.files['photo']
	# if post_data and allowed_file(post_data.filename):
	# 	filestream = post_data.read()

	# 	upload_data = Photo()
	# 	upload_data.photo = db.Blob(filestream)
	# 	upload_data.put()

	# 	comment = "uploaded!"

	# else:
	# 	comment = "please upload valid image file"

	#return render_template("accusation.html", comment=comment, all_list=Photo.all())


