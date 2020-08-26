# Job section
from tkinter import *
import tkinter as tk
import New_Notes
import sqlite3

# Defining a class for the Job section
class Job:
     def __init__(self, topic, date, time, duration, description):
                  self.topic       = topic;
                  self.date        = date;
                  self.time        = time;
                  self.duration    = duration;
                  self.description = description;

# Main programme
def read_input(master,input1,input2,input3,input4,input5,list_box, indexes_list ):
    # Getting topic, date, time, duration and discription from input boes and storing them
    topic       = input1.get()
    date        = input2.get()
    time        = input3.get()
    duration    = input4.get()
    description = input5.get()


    # Storing data in a Database
    id=New_Notes.new_notes('Job', [topic, date, time, duration, description])
    list_box.insert(tk.END,topic)
    indexes_list.append(id)
    #master.quit





# Creating graphics

def output_section(master1,list_box1,indexes_list):

    conn = sqlite3.connect('Notes.db')

    #Creating a cursor object using the cursor() method
    cur = conn.cursor()

    index=list_box1.curselection()
    i_prev=-1
    for i in index:
        i_prev=indexes_list[i]
    if(i_prev>=0):
       cur.execute("SELECT * FROM  Job WHERE generated_id = ?",(i_prev,) )
       rows=cur.fetchall()
       #print(rows)
       conn.commit()
       conn.close()
       # Creating labels and positioning them
       s = rows[0]
       #print(s)
       #print(s[0],s[1])
       master1.grid_columnconfigure(2, weight=1)
       l1=tk.Label(master1, text="Topic:"+s[1],width=20,height=2).grid(row=1,column=2)

       l2=tk.Label(master1, text="Date:"+s[2],width=20,height=2).grid(row=2,column=2)

       l3=tk.Label(master1, text="Time:"+s[3],width=20,height=2).grid(row=3, column=2)

       l4=tk.Label(master1, text="Duration:"+s[4],width=20,height=2).grid(row=4,column=2)

       l5=tk.Label(master1, text="Description:"+s[5],width=20,height=2).grid(row=5,column=2)







def new_note (list_box,indexes_list):

    master=tk.Toplevel()
    # Creating labels with descriptions for a Job section
    tk.Label(master, text="Job notes:").grid(row=0)
    tk.Label(master, text="Topic:").grid(row=1)
    tk.Label(master, text="Date:").grid(row=2)
    tk.Label(master, text="Time:").grid(row=3)
    tk.Label(master, text="Duration:").grid(row=4)
    tk.Label(master, text="Description:").grid(row=5)

    # Creating input boxes

    input1 = tk.Entry(master)
    input2 = tk.Entry(master)
    input3 = tk.Entry(master)
    input4 = tk.Entry(master)
    input5 = tk.Entry(master)


    # Setting position of input boxes
    input1.grid(row=1, column=1)
    input2.grid(row=2, column=1)
    input3.grid(row=3, column=1)
    input4.grid(row=4, column=1)
    input5.grid(row=5, column=1)


    # Making buttons and setting actions
    tk.Button(master, text='Quit', command=master.quit).grid(row=7, column=1, sticky=tk.W,pady=4)
    tk.Button(master, text='Done', command=lambda:read_input(master,input1,input2,input3,input4,input5,list_box,indexes_list)).grid(row=7, column=2, sticky=tk.W, pady=4)
