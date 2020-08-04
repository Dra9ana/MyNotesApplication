import tkinter as tk

# Defining class for a Travel section
class Travel:
     def __init__(self, destination, start_date, start_time, end_date, end_time):
                  self.destination = destination;
                  self.start_date  = start_date;
                  self.start_time  = start_time;
                  self.end_date    = end_date;
                  self.end_time    = end_time;
                  
# Main programme

def read_input():

# Reading information from the input
    destination  = input1.get()
    begin_date   = input2.get()
    begin_time   = input3.get()
    end_date     = input4.get()
    end_time     = input5.get()
    
# Opening/Closing a file and updating it
    input_file = open("travel_input.txt","w");
    input_file. write(destination+" "+begin_date+" "+begin_time+" "+end_date+" "+end_time);
    input_file.close()
    
# Creating graphics
  # Creating a New window
    new_master = tk.Toplevel(master)
    
  # Labelling Important Points
    tk.Label(new_master, text="Destination:"+destination).grid(row=0)
    tk.Label(new_master, text="Beginning date:"+begin_date).grid(row=1)
    tk.Label(new_master, text="Beginning time:"+begin_time).grid(row=2)
    tk.Label(new_master, text="Ending date:"+end_date).grid(row=3)
    tk.Label(new_master, text="Ending time:"+end_time).grid(row=4)
    new_master.mainloop()
                  

# Creating master
master = tk.Tk()


# Making three labels for description of Travel section
tk.Label(master, text="Destination:").grid(row=0)
tk.Label(master, text="Beginning date:").grid(row=1)
tk.Label(master, text="Beginning time:").grid(row=2)
tk.Label(master, text="Ending date:").grid(row=3)
tk.Label(master, text="Ending time:").grid(row=4)

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
