# NE RADI NEW NOTE


# EXPENCES_SPENT SECTION 

from tkinter import *
import tkinter as tk
import New_Notes
import sqlite3
import Query

# Read input
def read_input(master, input1, input2, input3, input4, input5, input6, input7, list_box, indexes_list):
    # Get attributes from input boxes and storing them
    date         = input1.get()
    incomes      = input2.get()
    food         = input3.get()
    clothes      = input4.get()
    bills        = input5.get()
    direct_debts = input6.get()
    other        = input7.get()
    total_spent  = food + clothes + bills + direct_debts + other 


    # Store data in a Database
    id = New_Notes.new_notes('Expences', [date, incomes, food, clothes, bills, direct_debts, other, total_spent])
    # Output new note on listbox
    list_box.insert(tk.END, topic)
    # Store id from database of added note
    indexes_list.append(id)
    
    #UPDATE NOTE WITH id_total ID IN THE DATABASE 
    

# Output section after clicking on button
def output_section(master, list_box, indexes_list):

     s = Query.get_row("Expences",list_box,indexes_list)
     if(s != []):
       # Set column index and its relative weight to distributeadditional space between
       master.grid_columnconfigure(2, weight=1)
       # Make labels and position them
       l1 = tk.Label(master, text="Date:"+s[1], width=20, height=2).grid(row=1, column=2)
       l2 = tk.Label(master, text="Incomes:"+s[2], width=20, height=2).grid(row=2, column=2)
       l3 = tk.Label(master, text="Food:"+s[3], width=20, height=2).grid(row=3, column=2)
       l4 = tk.Label(master, text="Clothes:"+s[4], width=20, height=2).grid(row=4, column=2)
       l5 = tk.Label(master, text="Bills:"+s[5], width=20, height=2).grid(row=5, column=2)
       l6 = tk.Label(master, text="Direct Debts:"+s[6], width=20, height=2).grid(row=6, column=2)
       l7 = tk.Label(master, text="Other:"+s[7], width=20, height=2).grid(row=7, column=2)
       l8 = tk.Label(master, text="Total Spent:"+s[8], width=20, height=2).grid(row=8, column=2)

# Make window for input
def new_note (list_box, indexes_list):

    # Create new window
    master=tk.Toplevel() 

    # Create labels with descriptions for a Job section
    tk.Label(master, text="Expences notes:").grid(row=0)
    tk.Label(master, text="Date:").grid(row=1)
    tk.Label(master, text="Incomes:").grid(row=2)
    tk.Label(master, text="Food:").grid(row=2)
    tk.Label(master, text="Clothes:").grid(row=4)
    tk.Label(master, text="Bills:").grid(row=5)
    tk.Label(master, text="Direct debts:").grid(row=6)
    tk.Label(master, text="Other:").grid(row=7)

    # Create input boxes
    input1 = tk.Entry(master)
    input2 = tk.Entry(master)
    input3 = tk.Entry(master)
    input4 = tk.Entry(master)
    input5 = tk.Entry(master)
    input6 = tk.Entry(master)
    input7 = tk.Entry(master)


    # Set position of input boxes
    input1.grid(row=1, column=1)
    input2.grid(row=2, column=1)
    input3.grid(row=3, column=1)
    input4.grid(row=4, column=1)
    input5.grid(row=5, column=1)
    input6.grid(row=6, column=1)
    input7.grid(row=7, column=1)
    


    # Make buttons and setting actions
    tk.Button(master, text='Quit', command=master.destroy).grid(row=10, column=2, sticky=tk.W, pady=4)
    tk.Button(master, text='Done', command=lambda:read_input(master, input1, input2, input3, input4, input5, input6, input7, list_box, indexes_list)).grid(row=10, column=3, sticky=tk.W, pady=4)
    
    
