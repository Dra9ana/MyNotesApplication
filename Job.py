import tkinter as tk

#section job
class Job:
     def __init__(self, start_time, end_time, days_off):
                  self.start_time = start_time;
                  self.end_time   = end_time;
                  self.days_off   = days_off;

#main programme

def read_input():
    #gets begin and end from input boxes ad store them in begin_time, end_time, daysoff
    name         = input1.get()
    begin_time   = input2.get()
    end_time     = input3.get()
    days_off     = input4.get()

     #writes data in file input.txt
    input_file = open("Job_input.txt","w");
    input_file. write(name+" "+begin_time+","+end_time+","+days_off);
    input_file.close()

def output_section(new_master, list):

    #label=what is written on the window, and sets position
    tk.Label(new_master, text="Beginning time:"+list[0]).grid(row=0)
    tk.Label(new_master, text="Ending time:"+list[1]).grid(row=1)
    tk.Label(new_master, text="Number of days off left:"+[list[2]]).grid(row=2)

def new_note(master):
    #making three labels for description of Job section
    tk.Label(master, text="Note name:").grid(row=0)
    tk.Label(master, text="Beginning time:").grid(row=1)
    tk.Label(master, text="Ending time:").grid(row=2)
    tk.Label(master, text="Number of days-off left:").grid(row=3)

    # making input boxes
    input1 = tk.Entry(master)
    input2 = tk.Entry(master)
    input3 = tk.Entry(master)
    input4 = tk.Entry(master)

    #setting position
    input1.grid(row=0, column=1)
    input2.grid(row=1, column=1)
    input3.grid(row=2, column=1)
    input4.grid(row=3, column=1)

    #making buttons and setting actions, command=what will happen when you click the button,sticky, pady not sure
    tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=1, sticky=tk.W,pady=4)
    tk.Button(master, text='Done', command=read_input ).grid(row=4, column=2, sticky=tk.W, pady=4)

#creates master
master = tk.Tk()
new_note(master)
master.mainloop()
