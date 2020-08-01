import tkinter as tk

#section job
class Job:
     def __init__(self, start, end_time, days_off):
                  self.start_time = start;
                  self.end_time   = end_time;
                  self.days_off   = days_off;

#main programme
def check():
    print("me too");
def read_input():

    begin_time   = input1.get()
    end_time     = input2.get()
    days_off = input3.get()
    print("Usla");
    input_file = open("input.txt","w");
    input_file. write(begin_time+" "+end_time+" "+days_off);
    input_file.close()
    new_master = tk.Toplevel(master)
    tk.Label(new_master, text="Beginning time:"+begin_time).grid(row=0)
    tk.Label(new_master, text="Ending time:"+end_time).grid(row=1)
    tk.Label(new_master, text="Number of days off left:"+days_off).grid(row=2)
    new_master.mainloop()





#creates master
master = tk.Tk()


#making three labels for description of Job section
tk.Label(master, text="Beginning time:").grid(row=0)
tk.Label(master, text="Ending time:").grid(row=1)
tk.Label(master, text="Number of days-off left:").grid(row=2)
# making input boxes
input1 = tk.Entry(master)
input2 = tk.Entry(master)
input3 = tk.Entry(master)
#setting position?
input1.grid(row=0, column=1)
input2.grid(row=1, column=1)
input3.grid(row=2, column=1)
#making buttons and setting actions
tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=1, sticky=tk.W,pady=4)
tk.Button(master, text='Done', command=read_input).grid(row=3, column=2, sticky=tk.W, pady=4)



master.mainloop()
