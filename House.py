import tkinter as tk

# Defining class for a House section
class Travel:
     def __init__(self, chore, start_date, start_time):
                  self.chore       = chore;
                  self.start_date  = start_date;
                  self.start_time  = start_time;
                  
# Main programme

def read_input():

# Reading information from the input
    chore        = input1.get()
    begin_date   = input2.get()
    begin_time   = input2.get()
    
# Opening/Closing a file and updating it
    input_file = open("House_input.txt","w");
    input_file. write(chore+" "+begin_date+" "+begin_time);
    input_file.close()
    
# Creating graphics
  # Creating a New window
    new_master = tk.Toplevel(master)
    
  # Labelling Important Points
    tk.Label(new_master, text="Who?:"+chore).grid(row=0)
    tk.Label(new_master, text="Date:"+begin_date).grid(row=1)
    tk.Label(new_master, text="Time:"+begin_time).grid(row=2)
 
    new_master.mainloop()
                  

# Creating master
master = tk.Tk()


# Making three labels for description of Travel section
tk.Label(master, text="Chore:").grid(row=0)
tk.Label(master, text="Date:").grid(row=1)
tk.Label(master, text="Time:").grid(row=2)

# Making input boxes
input1 = tk.Entry(master)
input2 = tk.Entry(master)
input3 = tk.Entry(master)

# Setting position of a box
input1.grid(row=0, column=1)
input2.grid(row=1, column=1)
input3.grid(row=2, column=1)

# Making buttons and setting actions
tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=1, sticky=tk.W,pady=4)
tk.Button(master, text='Done', command=read_input).grid(row=3, column=2, sticky=tk.W, pady=4)


master.mainloop()
