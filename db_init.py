import sqlite3 

db_path = r'/home/suvit/flask_setup/test/police.db'
conn = sqlite3.connect(db_path) 
c = conn.cursor()

c.execute('''Create table Civilian (uid integer primary key, name text, phone text ,email text, dob text)''') 
c.execute('''Create table Police (pid integer primary key,name text , designation text)''') 
c.execute('''Create table Pol_station (station_id integer primary key, address text )''') 
c.execute('''Create table Reports (FIR_id integer primary key , station_id integer , uid integer, category text , complaint_text text , status text)''')

conn.commit()

c.close()
