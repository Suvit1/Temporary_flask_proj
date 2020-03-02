from app import app 
import os
from flask import request,redirect,url_for,Flask,send_from_directory,render_template
from werkzeug.utils import secure_filename

@app.route('/') 
@app.route('/index') 
def index():
        return "Hello, World!"
@app.route('/lodge_complaint',methods=['GET', 'POST'])
def file_fir():
    if request.method == 'GET':
        return render_template('file_complaint.html')
    if request.method == 'POST':
        fid = request.form["f_id"] 
        c_name = request.form["c_name"] 
        c_date= request.form["c_date"] 
        c_time = request.form["c_time"] 
        c_place = request.form["c_place"] 
        c_cat = request.form["cat"] 
        c_text = request.form["c_text"] 
        return ""+fid+" "+c_name+" "+c_date+" "+c_time+" "+c_place+" "+c_cat+" "+c_text 

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
