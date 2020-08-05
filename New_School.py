import tkinter as tk


# Defining class for a School section

class School:
     def __init__(self, topic, subject, activity, date, time, duration, description):
                  self.topic       = topic;
                  self.subject     = subject;
                  self.activity        = activity;
                  self.date        = date;
                  self.time        = time;
                  self.duration    = duration;
                  self.description = description;

# Main programme

def read_input():

# Reading information from the input
    topic       = input1.get()
    subject     = input2.get()
    activity    = input3.get()
    date        = input4.get()
    time        = input5.get()
    duration    = input6.get()
    description = input7.get()

# DATABASE STUFF

# Creating graphics
  # Creating a New window
    new_master = tk.Toplevel(master)

  # Labelling Important Points
    tk.Label(new_master, text="Topic:"+topic).grid(row=1)
    tk.Label(new_master, text="Subject:"+topic).grid(row=2)
    tk.Label(new_master, text="Activity:"+activity).grid(row=3)
    tk.Label(new_master, text="Date:"+date).grid(row=4)
    tk.Label(new_master, text="Time:"+time).grid(row=5)
    tk.Label(new_master, text="Duration:"+duration).grid(row=6)
    tk.Label(new_master, text="description:"+description).grid(row=7)
    
    new_master.mainloop()


# Creating master
master = tk.Tk()

# Making three labels for description of School section
tk.Label(master, text="School notes:").grid(row=0)
tk.Label(master, text="Topic:").grid(row=1)
tk.Label(master, text="Subject:").grid(row=2)
tk.Label(master, text="Type:").grid(row=3)
tk.Label(master, text="Date:").grid(row=4)
tk.Label(master, text="Time:").grid(row=5)
tk.Label(master, text="Duration:").grid(row=6)
tk.Label(master, text="Description:").grid(row=7)

# Making input boxes
input1 = tk.Entry(master)
input2 = tk.Entry(master)
input3 = tk.Entry(master)
input4 = tk.Entry(master)
input5 = tk.Entry(master)
input6 = tk.Entry(master)
input7 = tk.Entry(master)


# Setting position of a box
input1.grid(row=1, column=1)
input2.grid(row=2, column=1)
input3.grid(row=3, column=1)
input4.grid(row=4, column=1)
input5.grid(row=5, column=1)
input6.grid(row=6, column=1)
input7.grid(row=7, column=1)

# Making buttons and setting actions
tk.Button(master, text='Quit', command=master.quit).grid(row=8, column=1, sticky=tk.W,pady=4)
tk.Button(master, text='Done', command=read_input).grid(row=8, column=2, sticky=tk.W, pady=4)


master.mainloop()
