# TREBA UPDATE DA SE URADI
# NECE DA OTVORI NEW NOTE



# EXPENCES_ALLOWANCE SECTION 

from tkinter import *
import tkinter as tk
import New_Notes
import sqlite3
import Query

# Read input
def read_input(master, input1, input2, input3, input4, input5, list_box, indexes_list):
    # Get attributes from input boxes and storing them
    food         = input1.get()
    clothes      = input2.get()
    bills        = input3.get()
    direct_debts = input4.get()
    other        = input5.get()
    total        = food + clothes + bills + direct_debts + other 


    # Store data in a Database
    # OVDE TREBA DA SE POZOVE UPDATE FUNKCIJA

# Output section after clicking on button
#def output_section(master, list_box, indexes_list):
#
 #    s = Query.get_row("New Expences",list_box,indexes_list)
  #   if(s != []):
   #    # Set column index and its relative weight to distributeadditional space between
    #   master.grid_columnconfigure(2, weight=1)
     #  # Make labels and position them
      # l1 = tk.Label(master, text="Food:"+s[1], width=20, height=2).grid(row=1, column=2)
       #l2 = tk.Label(master, text="Clothes:"+s[2], width=20, height=2).grid(row=2, column=2)
       #l3 = tk.Label(master, text="Bills:"+s[3], width=20, height=2).grid(row=3, column=2)
       #l4 = tk.Label(master, text="Direct Debts:"+s[4], width=20, height=2).grid(row=4, column=2)
       #l5 = tk.Label(master, text="Other:"+s[5], width=20, height=2).grid(row=5, column=2)
       #l6 = tk.Label(master, text="Total:"+s[5], width=20, height=2).grid(row=6, column=2)

# Make window for input
def new_note (list_box, indexes_list):

    # Create new window
    master=tk.Toplevel() 

    # Create labels with descriptions for a Job section
    tk.Label(master, text="Setting Allowance:").grid(row=0)
    tk.Label(master, text="Food:").grid(row=1)
    tk.Label(master, text="Clothes:").grid(row=2)
    tk.Label(master, text="Bills:").grid(row=3)
    tk.Label(master, text="Direct debts:").grid(row=4)
    tk.Label(master, text="Other:").grid(row=5)
    tk.Label(master, text="Total:").grid(row=6)

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
    tk.Button(master, text='Quit', command=master.destroy).grid(row=8, column=2, sticky=tk.W, pady=4)
    tk.Button(master, text='Done', command=lambda:read_input(master, input1, input2, input3, input4, input5, list_box, indexes_list)).grid(row=8, column=3, sticky=tk.W, pady=4)
