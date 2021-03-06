#!/usr/bin/env python
import sqlite3

db = sqlite3.connect('bukutamu.db',isolation_level=None)
cursor = db.cursor()
cursor.execute("create table if not exists tamu(nama varchar(16), alamat varchar(16), nim varchar(11))")

while True:
    print "1. add"
    print "2. view"
    print "3. remove"

    try:
        menu_in = raw_input("enter a choice: ")
    except KeyboardInterrupt:
        print "bye"
        break
    
    #print("your choice is {} {} {}".format(menu_in,aa,b,c).center(20))
    #print("your choice is " + menu_in)

    if menu_in == "1":
        #print("do add new data")
        data_nama = raw_input("Nama:".ljust(15))
        data_alamat = raw_input("Alamat:".ljust(15))
        data_nim = raw_input("NIM:".ljust(15))
        cursor.execute("insert into tamu values ('{}', '{}', '{}')".format(data_nama, data_alamat, data_nim))
        #db.commit()
        print("data baru berhasil ditambahkan")
    elif menu_in == "2":
        #print("do view all data")
        result = cursor.execute("select rowid, * from tamu")
        result = result.fetchall()
        header = "rowid|{}|{}|{}".format("nama".center(10), "alamat".center(10), "nim".center(10))
        print header
        print '=' * len(header)
        for r in result:
            print("{}|{}|{}|{}".format(str(r[0]).ljust(5),r[1].ljust(10), r[2].ljust(10), r[3].ljust(10)))
    elif menu_in == "3":
        print("remove a data")
        rowid_hapus = raw_input("rowid to delete: ")
        cursor.execute("delete from tamu where rowid = {}".format(rowid_hapus))
    else:
        print(" invalid choice, try again")
