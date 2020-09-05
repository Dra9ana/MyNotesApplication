# CREATE A NEW NOTE

import sqlite3

# Store note in database
def new_notes(s, a):
   # Create database
   conn = sqlite3.connect('Notes.db')
   # Open cursor
   cursor=conn.cursor()

   # Choose section
   if(s == 'Job'):
    cursor.execute("INSERT INTO Job (Name, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4]))
   elif(s == 'FaF'):
        cursor.execute("INSERT INTO FaF (Name, Activity, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4], a[5]))
   elif(s == 'School'):
        cursor.execute("INSERT INTO School (Name, Subject, Activity, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?, ?)",
                                                 (a[0], a[1], a[2], a[3], a[4], a[5], a[6]))
   elif(s == 'Travel'):
        cursor.execute("INSERT INTO Travel (Name, Destination, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4], a[5]))
   elif(s == 'Extracurricular'):
        cursor.execute("INSERT INTO Extracurricular (Name, Activity, Date, Time, Description) VALUES(?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4]))
   elif(s == 'Passwords'):
        cursor.execute("INSERT INTO Passwords (Name, Website, Additional_info, Username, Mail, Password) VALUES(?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4], a[5]))
   elif(s == 'House'):
        cursor.execute("INSERT INTO House (Name, Activity, Date, Time, Description) VALUES(?, ?, ?, ?, ?)",
                                                  (a[0], a[1], a[2], a[3], a[4]))


   # Get id of last row inserted into database
   id=cursor.lastrowid
   # Commit the changes
   conn.commit()
   # Close the database
   conn.close()
   # Return id in database
   return id
