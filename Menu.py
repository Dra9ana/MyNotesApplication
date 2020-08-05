from tkinter import *
import tkinter as tk

def open_section(file_name):
     #open file where data is written
     file = open(file_name)
     #make a window

     list_box   = Listbox(master)
     #set position of window(we shoudl see where we should set it)
     #read first line in file
     line = file.readline()
     #i is index of row
     i = 2
     #make first label
     list_box.insert(i, line)

     # copy all lines from the file in window
     while line:
           line=file.readline()
           i=i+1;
           list_box.insert(i, line)

     list_box.place(x=160,y=0)

     deln = tk.Button(master, text="Delete", width='5',bg='blue', fg='white')
     addn = tk.Button(master, text="New Note",width='5', bg='blue', fg='white')
     edit = tk.Button(master, text="Edit",width='5', bg='blue', fg='white')

     deln.place(x=300,y=20)
     addn.place(x=300,y=40)
     edit.place(x=300,y=60)



     file.close()





master = tk.Tk()
# set window title
master.title("Notes")
# set window width, height and background color
master.geometry("500x300")
master.configure(bg='lightblue')

#New_Note = tk.Button(master, text="New Note", command)
Job = tk.Button (master, text="Job", command = lambda: open_section("Job_input.txt"), width=20, bg='blue',fg='white')
Job.grid(row=0, column=0)
School = tk.Button (master, text="School", command = lambda: open_section("School_input.txt"),width=20, bg='blue',fg='white')
School.grid(row=1, column=0)
FaF = tk.Button (master, text="Family and Friends", command = lambda: open_section("FaF_input.txt"),width=20, bg='blue',fg='white')
FaF.grid(row=2, column=0)
House = tk.Button (master, text="House", command = lambda: open_section("House_input.txt"), width=20, bg='blue',fg='white');
House.grid(row=3, column=0)
Travel = tk.Button (master, text="Travel", command = lambda: open_section("Travel_input.txt"), width=20, bg='blue',fg='white');
Travel.grid(row=4, column=0)
Extracurricular = tk.Button (master, text="Extracirricular", command = lambda:open_section("Extracurricular_input.txt"), width=20, bg='blue', fg='white');
Extracurricular.grid(row=5, column=0)
Passwords = tk.Button (master, text="Passwords", command = lambda: open_section("Passwords_input.txt"), width=20, bg='blue',fg='white');
Passwords.grid(row=5, column=0)

#Job.pack()
#School.pack()
#FaF.pack()
#House.pack()
#Travel.pack()
#Extracurricular.pack()
#Passwords.pack()


master.mainloop()
