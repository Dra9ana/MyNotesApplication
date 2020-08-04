import tkinter as tk

def open_section(file_name)
    #open file where data is written
    file   = open(file_name)
    #make a window
    master = tk.Toplevel()
    #set position of window(we shoudl see where we should set it)
    #read first line in file
    line   = file.readline()
    #i is index of row
    i      = 1
    #make first label
    tk.Label(master, text=line).grid(row=0)

    # copy all lines from the file in window
    while line:
          line=file.readline()
          i=i+1;
          tk.Label(master, text=line).grid(row=i)
    file.close()
    
master = tk.Tk()
# set window title
master.title("Notes")
# set window width and height
master.configure(width=500, height=300)
# set window background color
master.configure(bg='lightblue')
master.mainloop()


#New_Note = tk.Button(master, text="New Note", command)
Job = tk.Button (master, text="Job", command = open_section("Job_input.txt"), width=20);
Job.grid(row=0, column=1)
School = tk.Button (master, text="School", command = open_section("School_input.txt"), width=20);
School.grid(row=1, column=0)
FaF = tk.Button (master, text="Family and Friends", command = open_section("FaF_input.txt"), width=20);
FaF.grid(row=2, column=0)
House = tk.Button (master, text="House", command = open_section("House_input.txt"), width=20);
House.grid(row=3, column=0)
Travel = tk.Button (master, text="Travel", command = open_section("Travel_input.txt"), width=20);
Travel.grid(row=4, column=0)
Extracurricular = tk.Button (master, text="Extracirricular", command = open_section("Extracurricular_input.txt"), width=20);
Extracurricular.grid(row=5, column=0)
Passwords = tk.Button (master, text="Passwords", command = open_section("Passwords_input.txt"), width=20);
Passwords.grid(row=5, column=0)

Job.pack()
School.pack()
FaF.pack()
House.pack()
Travel.pack()
Extracurricular.pack()
Passwords.pack()


master.mainloop()
