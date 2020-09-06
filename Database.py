# CREATE A DATABASE

import sqlite3

global id_allowance 
global id_balance 

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

# Create table - Passwords
c.execute('''CREATE TABLE Passwords
             ([generated_id] INTEGER PRIMARY KEY, [Name] text, [Website] text, [Additional_info] text, [Username] text, [Mail] text, [Password] text)''')

# Create table - Allowance
c.execute('''CREATE TABLE Allowance
             ([generated_id] INTEGER PRIMARY KEY, [Food] float, [Clothes] float, [Bills] float, [Direct_debts] float, [Other] float, [Total] float)''')

# Create table - Expenes
c.execute('''CREATE TABLE Expences
             ([generated_id] INTEGER PRIMARY KEY, [Date] date, [Incomes] float, [Food] float, [Clothes] float, [Bills] float, [Direct_debts] float, [Other] float, [Total] float)''')

# Create table - Balance
c.execute('''CREATE TABLE Balance
             ([generated_id] INTEGER PRIMARY KEY, [Incomes] float, [Food] float, [Food_left] float, [Clothes] float, [Clothes_left] float, [Bills] float, [Bills_left] float, [Direct_debts] float, [Direct_debts_left] float, [Other] float, [Other_left] float, [Total] float, [Left] float)''')

c.execute("INSERT INTO Allowance (Food, Clothes, Bills, Direct_debts, Other, Total) VALUES(?, ?, ?, ?, ?, ?)",
                               (0, 0, 0, 0, 0, 0))
id_allowance=c.lastrowid
c.execute("INSERT INTO Balance (Incomes, Food, Food_left, Clothes, Clothes_left, Bills, Bills_left, Direct_debts, Direct_debts_left, Other, Other_left, Total, Left) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
id_balance=c.lastrowid

def expences_ids():
    return [id_allowance, id_balance]

# Commit changes
conn.commit()
# Close Database
conn.close()
