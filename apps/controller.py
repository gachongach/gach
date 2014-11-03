from flask import render_template, Flask, request, url_for, current_app, flash, redirect
from apps import app
from apps.forms import AccForm

from google.appengine.ext import db



@app.route('/')
def index():
	return render_template("index.html")

from forms import *

@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template("login.html")

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


