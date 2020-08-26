# A function that stores new notes in a database

import sqlite3

def new_notes(s, a):

   conn = sqlite3.connect('Notes.db')
   cursor=conn.cursor()

   if(s=='Job'):
    cursor.execute("INSERT INTO Job (Name, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4]))
   elif(s=='FaF'):
        cursor.execute("INSERT INTO FaF (Name, Activity, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4], a[5]))
   elif(s=='School'):
        cursor.execute("INSERT INTO School (Name, Subject, Activity, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?, ?)",
                                                 (a[0], a[1], a[2], a[3], a[4], a[5], a[6]))
   elif(s=='Travel'):
        cursor.execute("INSERT INTO Travel (Name, Destination, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4], a[5]))
   elif(s=='Extracurricular'):
        cursor.execute("INSERT INTO Extracurricular (Name, Activity, Date, Time, Description) VALUES(?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4]))
   elif(s=='Passwords'):
        cursor.execute("INSERT INTO Passwords (Name,Website, Additional_info, Username, Mail, Password) VALUES(?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4]))
   elif(s=='House'):
        cursor.execute("INSERT INTO House (Name, Activity, Date, Time, Description) VALUES(?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4]))



   id=cursor.lastrowid
   conn.commit()
   conn.close()
   return id
