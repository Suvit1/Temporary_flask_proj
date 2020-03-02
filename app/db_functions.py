import sqlite3
import os
import hashlib

def select_firs(fir_status):
    fir_list = []
    try:
        sqliteConnection = sqlite3.connect('police.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        if fir_status=='new':
            sel_statement="select FIR_ID, date, location , category, station_id from FIR_table where status='new'"
        elif fir_status=='rejected':
            sel_statement="select FIR_ID, date, location , category, station_id from FIR_table where status='rejected'"
        elif fir_status=='accepted':
            sel_statement="select FIR_ID, date, location , category, station_id from FIR_table where status='approved'"

        cursor.execute(sel_statement)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        
        for row in records:
            print(row)
            ele ={}
            ele['fir_id']=row[0]
            ele['date'] = row[1] 
            ele['place'] = row[2]
            ele['category']= row[3]
            ele['station']= row[4]
            fir_list.append(ele)
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return fir_list  

        

def insert_fir(fir_form):
    try:
        sqliteConnection = sqlite3.connect('police.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sel_statement=" INSERT INTO FIR_table (FIR_id , complaint_filer_name ,date ,station_id , time,location, category , complaint_text  , status) Values ("+str(fir_form[0])+",'"+str(fir_form[1]) +"','"+str(fir_form[2])+"','Mahadevpura PS','"+str(fir_form[3])+"','"+str(fir_form[4])+"','"+str(fir_form[5])+"','"+str(fir_form[6])+"','new') "
        print(sel_statement)
        count = cursor.execute(sel_statement)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
    
def store_csv(fid,csv_text):
    file_hash = hashlib.sha256()
    file_hash.update(csv_text.encode('utf-8'))
    with open('tmp.csv', 'wb') as f:
        f.write(csv_text.encode('ascii'))
        # ...and read it back into a blob
    with open('tmp.csv', 'rb') as f:
        ablob = f.read()

    # OK, now for the DB part: we make it...:
    sqliteConnection = sqlite3.connect('police.db')
    cursor = sqliteConnection.cursor()
    sql = '''INSERT INTO record_table
        (FIR_id, FIR_form)
        VALUES(?, ?);'''
    count = cursor.execute(sql,[fid,sqlite3.Binary(ablob)])
    sqliteConnection.commit()
    print("Record inserted successfully into Records table ", cursor.rowcount)
    cursor.close()
    if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return file_hash.hexdigest()

    
