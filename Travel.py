# Travel section
from tkinter import *
import tkinter as tk
import New_Notes
import sqlite3
import Query

# Read input
def read_input(master, input1, input2, input3, input4, input5, input6, list_box, indexes_list):

# Reading information from the input
    name        = input1.get()
    destination = input2.get()
    date        = input3.get()
    time        = input4.get()
    duration    = input5.get()
    description = input6.get()

    # Storing data in a Database
    id = New_Notes.new_notes('Travel', [name, destination, date, time, duration, description])
    # Output new note on listbox
    list_box.insert(tk.END, name)
    # Store id from database of added note
    indexes_list.append(id)

# Output section after clicking on button
def output_section(master, list_box, indexes_list):

     s = Query.get_row("Travel",list_box,indexes_list)
     if(s != []):
        # Set column index and its relative weight to distributeadditional space between
        master.grid_columnconfigure(2, weight=1)

        # Labelling Important Points
        tk.Label(master, text="Name:"+s[1], width=20, height=2).grid(row=1, column=2)
        tk.Label(master, text="Destination:"+s[2], width=20, height=2).grid(row=2, column=2)
        tk.Label(master, text="Date:"+s[3], width=20, height=2).grid(row=3, column=2)
        tk.Label(master, text="Time:"+s[4], width=20, height=2).grid(row=4, column=2)
        tk.Label(master, text="Duration:"+s[5], width=20, height=2).grid(row=5, column=2)
        tk.Label(master, text="Description:"+s[6], width=20, height=2).grid(row=6, column=2)

# Make window for input
def new_note (list_box, indexes_list):

    # Creating master
    master = tk.Tk()

    # Making three labels for description of School section
    tk.Label(master, text="Travel notes:").grid(row=0)
    tk.Label(master, text="Name:").grid(row=1)
    tk.Label(master, text="Destination:").grid(row=2)
    tk.Label(master, text="Date:").grid(row=3)
    tk.Label(master, text="Time:").grid(row=4)
    tk.Label(master, text="Duration:").grid(row=5)
    tk.Label(master, text="Description:").grid(row=6)

    # Making input boxes
    input1 = tk.Entry(master)
    input2 = tk.Entry(master)
    input3 = tk.Entry(master)
    input4 = tk.Entry(master)
    input5 = tk.Entry(master)
    input6 = tk.Entry(master)

    # Setting position of a box
    input1.grid(row=1, column=1)
    input2.grid(row=2, column=1)
    input3.grid(row=3, column=1)
    input4.grid(row=4, column=1)
    input5.grid(row=5, column=1)
    input6.grid(row=6, column=1)

    # Making buttons and setting actions
    tk.Button(master, text='Quit', command=master.quit).grid(row=8, column=1, sticky=tk.W,pady=4)
    tk.Button(master, text='Done', command=lambda:read_input(master, input1, input2, input3, input4, input5, input6, list_box, indexes_list)).grid(row=8, column=2, sticky=tk.W, pady=4)
