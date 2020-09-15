# TO-DO SECTION

import datetime
from tkinter import *
import tkinter as tk
import sqlite3
import Query

def read_input(main_master, master, input1, input2, input3):
    month = input1.get()
    day   = input2.get()
    year  = input3.get()
    
    isValidDate = True
    try:
        datetime.datetime(int(day), int(month), int(year))
    except ValueError :
        isValidDate = False 
        
    if(isValidDate == False):
        choose_date(main_master)
    else:
        date_notes(main_master, day, month, year)
    
# Get a date from user
def choose_date(main_master):

    # Create a new window
    master=tk.Toplevel() 

    # Create labels with descriptions for a Job section
    tk.Label(master, text="Month:").grid(row=0, column=0)
    tk.Label(master, text="Year:").grid(row=2, column=0)
    tk.Label(master, text="Day:").grid(row=1, column=0)

    # Create input boxes
    input1 = tk.Entry(master)
    input2 = tk.Entry(master)
    input3 = tk.Entry(master)

    # Set position of input boxes
    input1.grid(row=0, column=1)
    input2.grid(row=2, column=1)
    input3.grid(row=1, column=1)

    # Make buttons and setting actions
    tk.Button(master, text='Quit', command=master.destroy).grid(row=4, column=2, sticky=tk.W, pady=4)
    tk.Button(master, text='Done', command=lambda:read_input(main_master, master, input1, input2, input3)).grid(row=4, column=3, sticky=tk.W, pady=4)

def date_notes(main_master, day, month, year):
    date = ("%d/%d/%d", day, month, year)
    
    # Connect to database and getting cursor
    conn   = sqlite3.connect('Notes.db')
    cur = conn.cursor()
    
    # Get rows using cursor
    cur.execute("SELECT * FROM Job WHERE Date = ?",(date,) )
    rows_Job = cur.fetchall()
    for row in rows_Job: 
        row_J.append('Job', row)
    cur.execute("SELECT * FROM FaF WHERE Date = ?",(date,) )
    rows_FaF = cur.fetchall()
    for row in rows_FaF: 
        row_F.append('FaF', row)
    cur.execute("SELECT * FROM School WHERE Date = ?",(date,) )
    rows_School = cur.fetchall()
    for row in rows_Job: 
        row_S.append('School', row)
    cur.execute("SELECT * FROM Travel WHERE Date = ?",(date,) )
    rows_Travel = cur.fetchall()
    for row in rows_Travel: 
        row_T.append('Travel', row)
    cur.execute("SELECT * FROM Extracurricular WHERE Date = ?",(date,) )
    rows_Extracurricular = cur.fetchall()
    for row in rows_Extracurricular: 
        row_E.append('Extracurricular', row)
    cur.execute("SELECT * FROM House WHERE Date = ?",(date,) )
    rows_House = cur.fetchall()
    for row in rows_House: 
        row_J.append('House', row)
    
    rows = row_J+row_F+row_S+row_T+row_E+row_H

    # Commit your changes in the database
    conn.commit()
    # Close database
    conn.close()
    
    open_notes(main_master, rows)
    
def open_notes(main_master, rows):

     # If there is no selected items, list of indexes should be empty
     indexes_list = []
     # Make listbox
     list_box     = Listbox(main_master, height=13, width=45)
     sections     = []

     # Go through columns
     for row in rows:
           # Put name of note in the list
           list_box.insert(tk.END, row[2])
           # Put index from database in list of indexes
           indexes_list.append(row[1])
           sections.append(row[0])

     # Set position of listbox
     list_box.place(x = 150, y = 0)
     # Enable user to select multiple items
     list_box.config(selectmode = MULTIPLE)
     # Output rows on the main window when item is selected
     o.open_to_do(sections, main_master, list_box, indexes_list)
     # Set first item to be automatically selected
     list_box.select_set(first = 0, last = None)
     list_box.event_generate("<<ListboxSelect>>")
     


