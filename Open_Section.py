from tkinter import *
import tkinter as tk
import functools
from New_Notes import*
import Delete_Update
from Delete_Update import *
from New_Job import*
import Open as o
def open_section(master,section):

     indexes_list=[]
     #make listbox
     list_box   = Listbox(master)

     conn = sqlite3.connect('Notes.db')
     cur = conn.cursor()
     cur.execute("SELECT generated_id,name FROM Job")
     #returns list of tupels
     rows = cur.fetchall()
     conn.close()

     #i is index of row

     # copy all note names from the file in window
     for row in rows:
           #put name of note in the list
           list_box.insert(tk.END,row[1])
           indexes_list.append(row[0])
           #increment index


     # set position of listbox
     list_box.place(x=160,y=0)
     list_box.config(selectmode=MULTIPLE)
     o.open(section,master,list_box,indexes_list)
     list_box.select_set(first=0,last=None)
     list_box.event_generate("<<ListboxSelect>>")
     #make buttons
     deln = tk.Button(master, text="Delete", command=lambda:deleting_Note(section,list_box,indexes_list), width='8',bg='white', fg='black')
     addn = tk.Button(master, text="New Note",command=lambda:new_note(list_box,indexes_list),width='8', bg='white', fg='black')
     edit = tk.Button(master, text="Edit",command=lambda:update_Note(master,s,a),width='8', bg='white', fg='black')

     #set places for buttons
     deln.place(x=800.0,y=20.0)
     addn.place(x=800.0,y=40.0)
     edit.place(x=800.0,y=60.0)

     #get the index of selected item
     #list_box.bind('<<ListboxSelect>>',lambda:New_Job.output_section(master,list_box))
