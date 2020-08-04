import tkinter as tk

# Defining class for a Extracurricular section
class Travel:
     def __init__(self, activity, location, start_date, start_time, duration):
                  self.activity       = activity;
                  self.location       = location
                  self.start_date     = start_date;
                  self.start_time     = start_time;
                  self.duration       = duration;
                  
# Main programme

def read_input():

# Reading information from the input
    activity     = input1.get()
    location     = input2.get()
    begin_date   = input3.get()
    begin_time   = input4.get()
    duration     = input5.get()
    
# Opening/Closing a file and updating it
    input_file = open("Extracurricular_input.txt","w");
    input_file. write(activity+" "+location+" "+begin_date+" "+begin_time+" "+duration);
    input_file.close()
    
# Creating graphics
  # Creating a New window
    new_master = tk.Toplevel(master)
    
  # Labelling Important Points
    tk.Label(new_master, text="Activity:"+activity).grid(row=0)
    tk.Label(new_master, text="Location:"+location).grid(row=1)
    tk.Label(new_master, text="Date:"+begin_date).grid(row=2)
    tk.Label(new_master, text="Time:"+begin_time).grid(row=3)
    tk.Label(new_master, text="Duration:"+duration).grid(row=4)
 
    new_master.mainloop()
                  

# Creating master
master = tk.Tk()


# Making three labels for description of Travel section
tk.Label(master, text="Activity:").grid(row=0)
tk.Label(master, text="Location:").grid(row=1)
tk.Label(master, text="Date:").grid(row=2)
tk.Label(master, text="Time:").grid(row=3)
tk.Label(master, text="Duration:").grid(row=4)

# Making input boxes
input1 = tk.Entry(master)
input2 = tk.Entry(master)
input3 = tk.Entry(master)
input4 = tk.Entry(master)
input5 = tk.Entry(master)

# Setting position of a box
input1.grid(row=0, column=1)
input2.grid(row=1, column=1)
input3.grid(row=2, column=1)
input4.grid(row=3, column=1)
input5.grid(row=4, column=1)

# Making buttons and setting actions
tk.Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=tk.W,pady=4)
tk.Button(master, text='Done', command=read_input).grid(row=5, column=2, sticky=tk.W, pady=4)


master.mainloop()
