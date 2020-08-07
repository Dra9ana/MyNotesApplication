import sqlite3

def New_Notes(s): 
  conn = sqlite3.connect('Notes.db')
  
  if(s=='Job'):
    conn.execute("INSERT INTO Job (Topic, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?)", 
                                                  (topic, date, time, duration, description))     
    elif(s=='FaF'):
        conn.execute("INSERT INTO FaF (Name, Activity, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?)", 
                                                  (name, activity, date, time, duration, description)) 
    elif(s=='School'):
        conn.execute("INSERT INTO School (Topic, Subject, Activity, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?, ?)", 
                                                 (topic, subject, activity, date, time, duration, description)) 
    elif(s=='Travel'):
        conn.execute("INSERT INTO Travel (Name, Destination, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?, ?)", 
                                                  (name, destination, date, time, duration, description)) 
    elif(s=='Extracurricular'):
        conn.execute("INSERT INTO Extracurricular (Name, Activity, Date, Time, Description) VALUES(?, ?, ?, ?, ?)", 
                                                  (name, activity, date, time, description)) 
    elif(s=='Passwords'):
        conn.execute("INSERT INTO Passwords (Website, Additional_info, Username, Mail, Password) VALUES(?, ?, ?, ?, ?)", 
                                                  (website, additional_info, username, mail, password)) 
    elif(s=='House'):
        conn.execute("INSERT INTO House (Name, Activity, Date, Time, Description) VALUES(?, ?, ?, ?, ?)", 
                                                  (name, activity, date, time, description)) 


conn.commit() 
