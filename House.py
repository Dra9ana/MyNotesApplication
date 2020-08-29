# House section
from tkinter import *
import tkinter as tk
import New_Notes
import sqlite3
import Query
import tkinter as tk

# Read input
def read_input(master, input1, input2, input3, input4, input5, list_box, indexes_list):

    # Read information from the input
    name        = input1.get()
    activity    = input2.get()
    date        = input3.get()
    time        = input4.get()
    description = input5.get()

    # Store data in a Database
    id = New_Notes.new_notes('House', [name, activity, date, time, description])

    # Output new note on listbox
    list_box.insert(tk.END, topic)
    # Store id from database of added note
    indexes_list.append(id)

# Output section after clicking on button
def output_section(master, list_box, indexes_list):

     s = Query.get_row("House",list_box,indexes_list)
     if(s != []):
        # Set column index and its relative weight to distributeadditional space between
        master.grid_columnconfigure(2, weight=1)

        # Labelling Important Points
        tk.Label(new_master, text="Name:"+s[1], width=20, height=2).grid(row=1, column=2)
        tk.Label(new_master, text="Activity:"+s[2], width=20, height=2).grid(row=2, column=2)
        tk.Label(new_master, text="Date:"+s[3], width=20, height=2).grid(row=3, column=2)
        tk.Label(new_master, text="Time:"+s[4], width=20, height=2).grid(row=4, column=2)
        tk.Label(new_master, text="Description:"+s[5], width=20, height=2).grid(row=5, column=2)

def new_note (list_box, indexes_list):
    # Creating master
    master = tk.Tk()

    # Making three labels for description of School section
    tk.Label(master, text="House notes:").grid(row=0)
    tk.Label(master, text="Name:").grid(row=1)
    tk.Label(master, text="Activity:").grid(row=2)
    tk.Label(master, text="Date:").grid(row=3)
    tk.Label(master, text="Time:").grid(row=4)
    tk.Label(master, text="Description:").grid(row=5)

    # Making input boxes
    input1 = tk.Entry(master)
    input2 = tk.Entry(master)
    input3 = tk.Entry(master)
    input4 = tk.Entry(master)
    input5 = tk.Entry(master)

    # Setting position of a box
    input1.grid(row=1, column=1)
    input2.grid(row=2, column=1)
    input3.grid(row=3, column=1)
    input4.grid(row=4, column=1)
    input5.grid(row=5, column=1)

    # Making buttons and setting actions
    tk.Button(master, text='Quit', command=master.quit).grid(row=7, column=1, sticky=tk.W,pady=4)
    tk.Button(master, text='Done', command=lambda:read_input(master, input1, input2, input3, input4, input5, list_box, indexes_list)).grid(row=7, column=2, sticky=tk.W, pady=4)
