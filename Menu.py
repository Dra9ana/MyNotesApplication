import tkinter as tk

master = tk.Tk()

# declare the window
window = tk.Tk()
# set window title
window.title("Notes")
# set window width and height
window.configure(width=500, height=300)
# set window background color
window.configure(bg='lightblue')
window.mainloop()


#New_Note = tk.Button(master, text="New Note", command)
Job = tk.Button (master, text="Job", command = open("Job_input.txt","r"), width=20);
Job.grid(row=0, column=0)
School = tk.Button (master, text="School", command = open("School_input.txt","r"), width=20);
School.grid(row=1, column=0)
FaF = tk.Button (master, text="Family and Friends", command = open("FaF_input.txt","r"), width=20);
FaF.grid(row=2, column=0)
House = tk.Button (master, text="House", command = open("House_input.txt","r"), width=20);
House.grid(row=3, column=0)
Travel = tk.Button (master, text="Travel", command = open("Travel_input.txt","r"), width=20);
Travel.grid(row=4, column=0)
Extracurricular = tk.Button (master, text="Extracirricular", command = open("Extracurricular_input.txt","r"), width=20);
Extracurricular.grid(row=5, column=0)
Passwords = tk.Button (master, text="Passwords", command = open("Passwords_input.txt","r"), width=20);
Passwords.grid(row=5, column=0)

Job.pack()
School.pack()
FaF.pack()
House.pack()
Travel.pack()
Extracurricular.pack()
Passwords.pack()


master.mainloop()
