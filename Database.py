import sqlite3

conn = sqlite3.connect('Notes.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - Job
c.execute('''CREATE TABLE Job
             ([generated_id] INTEGER PRIMARY KEY,[Topic] text, [Date] date, [Time] time, [Duration] time, [Description] text)''')
          
# Create table - School
c.execute('''CREATE TABLE School
             ([generated_id] INTEGER PRIMARY KEY,[Topic] text, [Subject] text, [activity] text, [Date] date, [Time] time, [Duration] time)''')
             
# Create table - FaF
c.execute('''CREATE TABLE FaF
             ([generated_id] INTEGER PRIMARY KEY,[Name] text, [Activity] text, [Date] date, [Time] time, [Duration] time, [Description] text)''')
             
# Create table - House
c.execute('''CREATE TABLE House
             ([generated_id] INTEGER PRIMARY KEY,[Name] text, [Activity] text, [Date] date, [Time] time, [Description] text)''')
             
# Create table - Travel
c.execute('''CREATE TABLE Travel
             ([generated_id] INTEGER PRIMARY KEY,[Name] text, [Destination] text, [Date] date, [Time] time, [Duration] time, [Description] text)''')
             
# Create table - Extracurricular
c.execute('''CREATE TABLE Extracurricular
             ([generated_id] INTEGER PRIMARY KEY,[Name] text, [Destination] text, [Date] date, [Time] time, [Duration] time, [Description] text)''')
             
# Create table - Passwords website, additional_info, username, mail, password
c.execute('''CREATE TABLE Passwords
             ([generated_id] INTEGER PRIMARY KEY,[Website] text, [Additional_info] text, [Username] text, [Mail] text, [Password] text)''')
                 
conn.commit()
