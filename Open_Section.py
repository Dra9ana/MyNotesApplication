from tkinter import *
import tkinter as tk
from  New_Notes import*
import Make_Changes
from Make_Changes import *
import Query
import Open as o


# Read the last selected section in listbox from database
def open_section(master, section):

     # If there is no selected items, list of indexes should be empty
     indexes_list = []
     # Make listbox
     list_box     = Listbox(master)
     # Read rows from database
     rows         = Query.select_name(section)

     # Go through columns
     for row in rows:
           # Put name of note in the list
           list_box.insert(tk.END, row[1])
           # Put index from database in list of indexes
           indexes_list.append(row[0])

     # Set position of listbox
     list_box.place(x = 160, y = 0)
     # Enable user to select multiple items
     list_box.config(selectmode = MULTIPLE)
     # Output rows on the main window when item is selected
     o.open(section, master, list_box, indexes_list)
     # Set first item to be automatically selected
     list_box.select_set(first = 0, last = None)
     list_box.event_generate("<<ListboxSelect>>")

     #make buttons
     deln = tk.Button(master, text="Delete", command=lambda:Delete_Note(section, list_box, indexes_list), width='8',bg='white', fg='black')
     addn = tk.Button(master, text="New Note",command=lambda:Add_Note(section, list_box, indexes_list),width='8', bg='white', fg='black')
     edit = tk.Button(master, text="Edit",command=lambda:Edit_Note(section, master),width='8', bg='white', fg='black')

     #set places for buttons
     deln.place(x = 800.0,y = 20.0)
     addn.place(x = 800.0,y = 40.0)
     edit.place(x = 800.0,y = 60.0)
