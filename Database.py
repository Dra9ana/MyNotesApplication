# CREATE A DATABASE

import sqlite3

# Create database
conn = sqlite3.connect('Notes.db')
# Create cursor
c = conn.cursor()

# Create table - Job
c.execute('''CREATE TABLE Job
             ([generated_id] INTEGER PRIMARY KEY, [Name] text, [Date] date, [Time] time, [Duration] time, [Description] text)''')

# Create table - School
c.execute('''CREATE TABLE School
             ([generated_id] INTEGER PRIMARY KEY, [Name] text, [Subject] text, [activity] text, [Date] date, [Time] time, [Duration] time, [Description] text )''')

# Create table - FaF
c.execute('''CREATE TABLE FaF
             ([generated_id] INTEGER PRIMARY KEY, [Name] text, [Activity] text, [Date] date, [Time] time, [Duration] time, [Description] text)''')

# Create table - House
c.execute('''CREATE TABLE House
             ([generated_id] INTEGER PRIMARY KEY, [Name] text, [Activity] text, [Date] date, [Time] time, [Description] text)''')

# Create table - Travel
c.execute('''CREATE TABLE Travel
             ([generated_id] INTEGER PRIMARY KEY, [Name] text, [Destination] text, [Date] date, [Time] time, [Duration] time, [Description] text)''')

# Create table - Extracurricular
c.execute('''CREATE TABLE Extracurricular
             ([generated_id] INTEGER PRIMARY KEY, [Name] text, [Destination] text, [Date] date, [Time] time, [Duration] time, [Description] text)''')

# Create table - Passwords website, additional_info, username, mail, password
c.execute('''CREATE TABLE Passwords
             ([generated_id] INTEGER PRIMARY KEY, [Name] text, [Website] text, [Additional_info] text, [Username] text, [Mail] text, [Password] text)''')

# Commit changes
conn.commit()
# Close Database
conn.close()
