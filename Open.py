import tkinter
import New_Job
import New_FaF
import New_Notes
import New_House
import New_School
import New_Travel
#import New_Passwords
import New_Extracurricular

class Handler:

      def __init__(self,function,section,master,list_box,indexes):
          self.function=function
          self.master=master
          self.section=section
          self.list_box=list_box
          self.indexes=indexes
      def callback(self,event):
          self.function(self)
def f(o):
      if(o.section=='Job'):
            New_Job.output_section(o.master,o.list_box,o.indexes)
      elif(o.section=='FaF'):
              f=New_FaF.output_section(o.master,o.list_box,o.indexes)
      elif(o.section=='School'):
             f=New_School.output_section(o.master,o.list_box,o.indexes)
      elif(o.section=='Travel'):
             f=New_Travel.output_section(o.master,o.list_box,o.indexes)
      elif(o.section=='Extracurricular'):
             f=New_Extracurricular.output_section(o.master,o.list_box,o.indexes)
         #elif(section=='Passwords'):
             #f=New_Passwords.output_section(master,list_box)
      elif(o.section=='House'):
             f=New_House.output_section(o.master,o.list_box,o.indexes)

def open(section,master,list_box,indexes_list):
         obj=Handler(f,section,master,list_box,indexes_list)
         list_box.bind('<<ListboxSelect>>',obj.callback)
