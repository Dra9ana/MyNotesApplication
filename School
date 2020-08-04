import tkinter as tk


# Defining class for a School section

class School:
     def __init__(self, subject, type, start_time, end_time):
                  self.subject    = subject;
                  self.type       = type;
                  self.start_time = start_time;
                  self.end_time   = end_time;

# Main programme

def read_input():

# Reading information from the input
    subject    = input1.get()
    type       = input2.get()
    begin_time = input3.get()
    end_time   = input4.get()

# Opening/Closing a file and updating it
    input_file = open("school_input.txt","w");
    input_file. write(subject+" "+type+" "+begin_time+" "+end_time);
    input_file.close()

# Creating graphics
  # Creating a New window
    new_master = tk.Toplevel(master)

  # Labelling Important Points
    tk.Label(new_master, text="Subject:"+subject).grid(row=0)
    tk.Label(new_master, text="Type of activity:"+type).grid(row=1)
    tk.Label(new_master, text="Beginning time:"+begin_time).grid(row=2)
    tk.Label(new_master, text="Ending time:"+end_time).grid(row=3)
    new_master.mainloop()


# Creating master
master = tk.Tk()

# Making three labels for description of School section
tk.Label(master, text="Subject:").grid(row=0)
tk.Label(master, text="Type:").grid(row=1)
tk.Label(master, text="Beginning time:").grid(row=2)
tk.Label(master, text="Ending time:").grid(row=3)

# Making input boxes
input1 = tk.Entry(master)
input2 = tk.Entry(master)
input3 = tk.Entry(master)
input4 = tk.Entry(master)


# Setting position of a box
input1.grid(row=0, column=1)
input2.grid(row=1, column=1)
input3.grid(row=2, column=1)
input4.grid(row=3, column=1)

# Making buttons and setting actions
tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=1, sticky=tk.W,pady=4)
tk.Button(master, text='Done', command=read_input).grid(row=4, column=2, sticky=tk.W, pady=4)


master.mainloop()
