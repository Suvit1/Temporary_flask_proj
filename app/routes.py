from app import app 
import os
from flask import request,redirect,url_for,Flask,send_from_directory,render_template
from werkzeug.utils import secure_filename
from app import db_functions

@app.route('/') 
@app.route('/index') 
def homepage():
        return render_template('index1.html')

@app.route('/lodge_complaint',methods=['GET', 'POST'])
def file_fir():
    if request.method == 'GET':
        return render_template('file_complaint.html')
    if request.method == 'POST':
        form = []
        fid = request.form["f_id"] 
        c_name = request.form["c_name"] 
        c_date= request.form["c_date"] 
        c_time = request.form["c_time"] 
        c_place = request.form["c_place"] 
        c_cat = request.form["cat"] 
        c_text = request.form["c_text"] 
        form.append(fid)
        form.append(c_name )
        form.append(c_date)
        form.append(c_time )
        form.append(c_place)
        form.append(c_cat)
        form.append(c_text )
        db_functions.insert_fir(form)
        csv_text= fid+","+c_name+","+c_date+","+c_time+","+c_place+","+c_cat+","+c_text 
        hashval = db_functions.store_csv(fid,csv_text)
        return csv_text+" "+hashval

@app.route('/tab')
def tabnew():
    firs=db_functions.select_firs('new')
    print(firs)
    return render_template('tab.html')

@app.route('/tab1')
def tab1new():
    firs=db_functions.select_firs('new')
    print(firs)
    return render_template('tab1.html',firs=firs)

@app.route('/search')
def search_fir():
    return render_template('firdisplay.html')

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
