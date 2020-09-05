# JOB SECTION

from tkinter import *
import tkinter as tk
import New_Notes
import sqlite3
import Query

# Read input
def read_input(master, input1, input2, input3, input4, input5, list_box, indexes_list):
    # Get attributes from input boxes and storing them
    topic       = input1.get()
    date        = input2.get()
    time        = input3.get()
    duration    = input4.get()
    description = input5.get()


    # Store data in a Database
    id = New_Notes.new_notes('Job', [topic, date, time, duration, description])
    # Output new note on listbox
    list_box.insert(tk.END, topic)
    # Store id from database of added note
    indexes_list.append(id)

# Output section after clicking on button
def output_section(master, list_box, indexes_list):

     s = Query.get_row("Job",list_box,indexes_list)
     if(s != []):
       # Set column index and its relative weight to distributeadditional space between
       master.grid_columnconfigure(2, weight=1)
       # Make labels and position them
       l1 = tk.Label(master, text="Topic:"+s[1], width=20, height=2).grid(row=1, column=2)
       l2 = tk.Label(master, text="Date:"+s[2], width=20, height=2).grid(row=2, column=2)
       l3 = tk.Label(master, text="Time:"+s[3], width=20, height=2).grid(row=3, column=2)
       l4 = tk.Label(master, text="Duration:"+s[4], width=20, height=2).grid(row=4, column=2)
       l5 = tk.Label(master, text="Description:"+s[5], width=20, height=2).grid(row=5, column=2)

# Make window for input
def new_note (list_box, indexes_list):

    # Create new window
    master=tk.Toplevel()

    # Create labels with descriptions for a Job section
    tk.Label(master, text="Job notes:").grid(row=0)
    tk.Label(master, text="Topic:").grid(row=1)
    tk.Label(master, text="Date:").grid(row=2)
    tk.Label(master, text="Time:").grid(row=3)
    tk.Label(master, text="Duration:").grid(row=4)
    tk.Label(master, text="Description:").grid(row=5)

    # Create input boxes
    input1 = tk.Entry(master)
    input2 = tk.Entry(master)
    input3 = tk.Entry(master)
    input4 = tk.Entry(master)
    input5 = tk.Entry(master)


    # Set position of input boxes
    input1.grid(row=1, column=1)
    input2.grid(row=2, column=1)
    input3.grid(row=3, column=1)
    input4.grid(row=4, column=1)
    input5.grid(row=5, column=1)


    # Make buttons and setting actions
    tk.Button(master, text='Quit', command=master.quit).grid(row=7, column=2, sticky=tk.W, pady=4)
    tk.Button(master, text='Done', command=lambda:read_input(master, input1, input2, input3, input4, input5, list_box, indexes_list)).grid(row=7, column=3, sticky=tk.W, pady=4)
