from flask import render_template, Flask, request, url_for, current_app, flash, redirect
from apps import app
from apps.forms import AccForm
from models import User
from models import joiningUsers
from models import joinedUsers
from google.appengine.ext import db
import random
import string
import smtplib


@app.route('/user_join', methods=['GET', 'POST'])
def join():
    new_id = request.form['new_id']
    new_pw = request.form['new_pw']
    new_email = request.form['new_email']
    user = User(
        id=new_id,
        pw=new_pw,
        status=0,
        score=0
    )
    db.session.add(user)
    db.session.commit()
    user_id = new_id
    uniqueCode = createJoinCode()
    joining = joiningUsers(
        email=new_email,
        code = uniqueCode
    )
    db.session.add(joiningUsers)
    db.session.commit()

    sendEmail(new_email, new_id, uniqueCode)

    return render_template("index.html")

def createJoinCode():
    code  = ""
    for i in range(0, 32):
        code += random.choice(string.ascii_letters)
    return code

def sendEmail(address, userId,uniqueCode):
    fromAdd = "gachongach@gmail.com"
    toAdd = address
    FROM = 'gachongach@gmail.com'
    TO = [address] #must be a list
    SUBJECT = "Certify your account"
    TEXT = "Hello, " + userId + "\nTo certify your account" + ",click below link\n" + "http://gachongach.com/varify?code=" + uniqueCode

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
                """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    name = "gachongach"
    pw = "gachgachon2014"

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(name,pw)
    server.sendmail(fromAdd, toAdd, message)
    server.quit()

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


