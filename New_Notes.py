# A function that stores new notes in a database

import sqlite3

def New_Notes(s, a): 
  conn = sqlite3.connect('Notes.db')
  
  if(s=='Job'):
    conn.execute("INSERT INTO Job (Topic, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?)", 
                                                  (a[0], a[1], a[2], a[3], a[4]))     
    elif(s=='FaF'):
        conn.execute("INSERT INTO FaF (Name, Activity, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?)", 
                                                  (a[0], a[1], a[2], a[3], a[4], a[5])) 
    elif(s=='School'):
        conn.execute("INSERT INTO School (Topic, Subject, Activity, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?, ?)", 
                                                 (a[0], a[1], a[2], a[3], a[4], a[5], a[6])) 
    elif(s=='Travel'):
        conn.execute("INSERT INTO Travel (Name, Destination, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?)", 
                                                  (a[0], a[1], a[2], a[3], a[4], a[5])) 
    elif(s=='Extracurricular'):
        conn.execute("INSERT INTO Extracurricular (Name, Activity, Date, Time, Description) VALUES(?, ?, ?, ?, ?)", 
                                                  (a[0], a[1], a[2], a[3], a[4])) 
    elif(s=='Passwords'):
        conn.execute("INSERT INTO Passwords (Website, Additional_info, Username, Mail, Password) VALUES(?, ?, ?, ?, ?)", 
                                                  (a[0], a[1], a[2], a[3], a[4])) 
    elif(s=='House'):
        conn.execute("INSERT INTO House (Name, Activity, Date, Time, Description) VALUES(?, ?, ?, ?, ?)", 
                                                  (a[0], a[1], a[2], a[3], a[4])) 


conn.commit() 
