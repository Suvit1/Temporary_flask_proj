from app import app 
import os
from flask import request,redirect,url_for,Flask,send_from_directory,render_template
from werkzeug.utils import secure_filename

@app.route('/') 
@app.route('/index') 
def index():
        return "Hello, World!"

@app.route('/upload')
def load_file():
    if request.method == 'GET':
        return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join("/home/suvit/flask_setup/test/img_up",secure_filename(f.filename)))
        return 'file uploaded successfully'
