# OPENS A SECTION YOU'VE CHOSEN 

import tkinter as tk
import Job
import FaF
import New_Notes
import House
import School
import Travel
import Passwords
import Extracurricular
import Expences
import To_do

# Handle event
class Handler:

      # Constructor
      def __init__(self, function, section, master, list_box, indexes):
          # Function we want to call when event occurs
          self.function = function
          # Arguments of that function
          self.master   = master
          self.section  = section
          self.list_box = list_box
          self.indexes  = indexes
      # Callback after event occurs
      def callback(self, event):
          self.function(self)

# Choose which section to output
def f(o):
      if(o.section == 'Job'):
             f = Job.output_section(o.master, o.list_box, o.indexes)
      elif(o.section == 'FaF'):
             f = FaF.output_section(o.master, o.list_box, o.indexes)
      elif(o.section == 'School'):
             f = School.output_section(o.master, o.list_box, o.indexes)
      elif(o.section == 'Travel'):
             f = Travel.output_section(o.master, o.list_box, o.indexes)
      elif(o.section == 'Extracurricular'):
             f = Extracurricular.output_section(o.master, o.list_box, o.indexes)
      elif(o.section == 'Passwords'):
             f = Passwords.output_section(o.master, o.list_box, o.indexes)
      elif(o.section == 'House'):
             f = House.output_section(o.master, o.list_box, o.indexes)
      elif(o.section == 'Expences'):
             f = Expences.output_section(o.master, o.list_box, o.indexes)
      elif(o.section == 'To_do'):
             f = To_do.output_section(o)


def open(section, master, list_box, indexes_list):
         # Create new hanler
         obj = Handler(f, section, master, list_box, indexes_list)
         # Call callback when some listbox item is selected
         list_box.bind('<<ListboxSelect>>', obj.callback)
         
def open_to_do(section, master, list_box, indexes_list):
         # Create new hanler
         obj = Handler(f, section, master, list_box, indexes_list)
         # Call callback when some listbox item is selected
         list_box.bind('<<ListboxSelect>>', obj.callback)
