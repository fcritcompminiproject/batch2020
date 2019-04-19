import os
from flask import Flask, render_template, request

app = Flask(__name__)


UPLOAD_FOLDER = os.path.basename('data')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    file.filename = 'test.png'
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)
    os.system('python main.py')
    p=open("out.txt","r")
    if p.mode == "r":
	    oph = p.read()
    p.close()
    return render_template('result.html', result = oph, image_file_name = file.filename)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

