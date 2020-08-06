# Job section

import tkinter as tk


# Defining a class for the Job section
class Job:
     def __init__(self, topic, date, time, duration, description):
                  self.topic       = topic;
                  self.date        = date;
                  self.time        = time;
                  self.duration    = duration;
                  self.description = description;

# Main programme

def read_input():
    # Getting topic, date, time, duration and discription from input boes and storing them
    topic       = input1.get()
    date        = input2.get()
    time        = input3.get()
    duration    = input4.get()
    description = input5.get()


    # Storing data in a Database
    conn = open.database("Notes.db")
    conn.execute("INSERT INTO Job (Topic, Date, Time, Duration, Description) VALUES(?, ?, ?, ?, ?)", 
                                                  (topic, date, time, duration, description)) 
  
    conn.commit() 
     
# Creating graphics
    # Creating a window
    new_master = tk.Toplevel(master)
    # Creating labels and positioning them
    tk.Label(new_master, text="Topic:"+topic).grid(row=1)
    tk.Label(new_master, text="Date:"+date).grid(row=2)
    tk.Label(new_master, text="Time:"+time).grid(row=3)
    tk.Label(new_master, text="Duration:"+duration).grid(row=4)
    tk.Label(new_master, text="description:"+description).grid(row=5)
    
    
    new_master.mainloop()


# Creating master
master = tk.Tk()


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
tk.Button(master, text='Done', command=read_input).grid(row=7, column=2, sticky=tk.W, pady=4)



master.mainloop()
