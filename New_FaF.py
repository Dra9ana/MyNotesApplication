import tkinter as tk


# Defining class for a Friends and family section

class School:
     def __init__(self, name, activity, date, time, duration, description):
                  self.name        = name;
                  self.activity    = activity;
                  self.date        = date;
                  self.time        = time;
                  self.duration    = duration;
                  self.description = description;

# Main programme

def read_input():

# Reading information from the input
    name        = input1.get()
    activity    = input2.get()
    date        = input3.get()
    time        = input4.get()
    duration    = input5.get()
    description = input6.get()

# DATABASE STUFF

# Creating graphics
  # Creating a New window
    new_master = tk.Toplevel(master)

  # Labelling Important Points
    tk.Label(new_master, text="Name:"+name).grid(row=1)
    tk.Label(new_master, text="Activity:"+activity).grid(row=2)
    tk.Label(new_master, text="Date:"+date).grid(row=3)
    tk.Label(new_master, text="Time:"+time).grid(row=4)
    tk.Label(new_master, text="Duration:"+duration).grid(row=5)
    tk.Label(new_master, text="Description:"+description).grid(row=6)
    
    new_master.mainloop()


# Creating master
master = tk.Tk()

# Making three labels for description of School section
tk.Label(master, text="Friends and family notes:").grid(row=0)
tk.Label(master, text="Name:").grid(row=1)
tk.Label(master, text="Activity:").grid(row=2)
tk.Label(master, text="Date:").grid(row=3)
tk.Label(master, text="Time:").grid(row=4)
tk.Label(master, text="Duration:").grid(row=5)
tk.Label(master, text="Description:").grid(row=6)

# Making input boxes
input1 = tk.Entry(master)
input2 = tk.Entry(master)
input3 = tk.Entry(master)
input4 = tk.Entry(master)
input5 = tk.Entry(master)
input6 = tk.Entry(master)


# Setting position of a box
input1.grid(row=1, column=1)
input2.grid(row=2, column=1)
input3.grid(row=3, column=1)
input4.grid(row=4, column=1)
input5.grid(row=5, column=1)
input6.grid(row=6, column=1)

# Making buttons and setting actions
tk.Button(master, text='Quit', command=master.quit).grid(row=7, column=1, sticky=tk.W,pady=4)
tk.Button(master, text='Done', command=read_input).grid(row=7, column=2, sticky=tk.W, pady=4)


master.mainloop()
