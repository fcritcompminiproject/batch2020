import os
import sqlite3
from flask import Flask, request, render_template, send_from_directory, send_file
import aadhar
app = Flask(__name__)
 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#print(APP_ROOT)

@app.route("/")
def index(name=None):
	return render_template('home_2.html',name=name)


@app.route("/upload", methods=['POST','GET'])
def upload(name=None):

	target = os.path.join(APP_ROOT, 'images/')
	print(target)
	print(request.files.getlist("file"))
	for upload in request.files.getlist("file"):
		print(upload)
		print("{} is the file name".format(upload.filename))
		filename = upload.filename
		ext = os.path.splitext(filename)[1]
	if (ext == ".jpg") or (ext == ".png") or (ext == ".jpeg"):
	    	print("File supported moving on...")
	else:
		render_template("Error.html", message="Files uploaded are not supported...")
	destination = "/".join([target, filename])
	print("Accept incoming file:", filename)
	print("Save it to:", destination)
	upload.save(destination)
	return render_template('home_2.html',name=name)


@app.route("/result",methods=['GET'])
def result(name=None):
	aadhar.function()
	con = sqlite3.connect("example.db")
	con.row_factory = sqlite3.Row

	cur = con.cursor()
	cur.execute("SELECT * FROM data ORDER BY no DESC LIMIT 1;")

	rows = cur.fetchall(); 
	return render_template('home_2.html', name=name, rows = rows)


if __name__ == "__main__":
    app.run()