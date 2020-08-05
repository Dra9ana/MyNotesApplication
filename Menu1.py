from tkinter import *
import tkinter as tk
import Job


def open_section(file_name):
     #open file where data is written
     file = open(file_name)
     #make listbox
     list_box   = Listbox(master)
     #make dictionary
     d={}
     #read first line of code
     line = file.readline()
     #separate note name from the rest
     (key,value)=line.split(",")
     #set dictionary parameters
     d[key]=value

     #i is index of row
     i = 2
     #make first list raw
     list_box.insert(i, key)

     # copy all note names from the file in window
     while line:
           #read line
           line=file.readline()
           #increment index
           i=i+1
           #put name of note in the list
           list_box.insert(i,key)
           #seperate name from other features
           (key,value)=line.split(",")
           #set dictionary parameters
           d[key]=value
     # set position of listbox
     list_box.place(x=160,y=0)

     #make buttons
     deln = tk.Button(master, text="Delete", width='8',bg='white', fg='black')
     addn = tk.Button(master, text="New Note",width='8', bg='white', fg='black')
     edit = tk.Button(master, text="Edit",width='8', bg='white', fg='black')

     #set places for buttons
     deln.place(x=400,y=20)
     addn.place(x=400,y=40)
     edit.place(x=400,y=60)

     #get the index of selected item
     index=list_box.currselection()
     #get the selected name
     key=get(first=index,last=none)
     #find features in dictionary and split them
     list=d[key].split(";")
     #get section name from the file_name and call outpu function
     file_name[1:-10].output(master,list)



     file.close()


master = tk.Tk()
# set window title
master.title("Notes")
# set window width, height and background color
master.geometry("500x300")
master.configure(bg='lightblue')

Job = tk.Button (master, text="Job", command = lambda: open_section("Job_input.txt"), width=20, bg='white', fg='black')
Job.grid(row=0, column=0)
School = tk.Button (master, text="School", command = lambda: open_section("School_input.txt"), width=20, bg='white', fg='black')
School.grid(row=1, column=0)
FaF = tk.Button (master, text="Family and Friends", command = lambda: open_section("FaF_input.txt"), width=20, bg='white', fg='black')
FaF.grid(row=2, column=0)
House = tk.Button (master, text="House", command = lambda: open_section("House_input.txt"), width=20, bg='white', fg='black');
House.grid(row=3, column=0)
Travel = tk.Button (master, text="Travel", command = lambda: open_section("Travel_input.txt"), width=20, bg='white', fg='black');
Travel.grid(row=4, column=0)
Extracurricular = tk.Button (master, text="Extracirricular", command = lambda:open_section("Extracurricular_input.txt"), width=20, bg='white', fg='black');
Extracurricular.grid(row=5, column=0)
Passwords = tk.Button (master, text="Passwords", command = lambda: open_section("Passwords_input.txt"), width=20, bg='white', fg='black');
Passwords.grid(row=5, column=0)

#Job.pack()
#School.pack()
#FaF.pack()
#House.pack()
#Travel.pack()
#Extracurricular.pack()
#Passwords.pack()


master.mainloop()
