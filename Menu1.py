from tkinter import *
import tkinter as tk
import New_Job as nj
from New_Job import *
import Open_Section as os

master = tk.Tk()


# set window title
master.title("Notes")
# set window width, height and background color
master.geometry("2500x3000")
master.configure(bg='lightblue')

Job = tk.Button (master, text="Job", command = lambda:os.open_section(master,"Job"), width=20, bg='white', fg='black')
Job.grid(row=0, column=0)
School = tk.Button (master, text="School", command = lambda:os.open_section(master,"School"), width=20, bg='white', fg='black')
School.grid(row=1, column=0)
FaF = tk.Button (master, text="Family and Friends", command = lambda:os.open_section(master,"FaF"), width=20, bg='white', fg='black')
FaF.grid(row=2, column=0)
House = tk.Button (master, text="House", command = lambda:os.open_section(master,"House"), width=20, bg='white', fg='black');
House.grid(row=3, column=0)
Travel = tk.Button (master, text="Travel", command = lambda:os.open_section(master,"Travel"), width=20, bg='white', fg='black');
Travel.grid(row=4, column=0)
Extracurricular = tk.Button (master, text="Extracirricular", command = lambda:os.open_section(master,"Extracurricular"), width=20, bg='white', fg='black');
Extracurricular.grid(row=5, column=0)
Passwords = tk.Button (master, text="Passwords", command = lambda:os.open_section(master,"Passwords"), width=20, bg='white', fg='black');
Passwords.grid(row=5, column=0)

#Job.pack()
#School.pack()
#FaF.pack()
#House.pack()
#Travel.pack()
#Extracurricular.pack()
#Passwords.pack()


master.mainloop()
