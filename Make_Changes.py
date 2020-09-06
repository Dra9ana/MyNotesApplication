# MAKE CHANGES 
# "Main code" for Deleting, Editing and Creating new notes 

import sqlite3
import Delete
import Job
import FaF
import New_Notes
import House
import School
import Travel
import Passwords
import Extracurricular
import Expences

# DELETE
def Delete_Note(section, list_box, indexes_list):

    # Get selected rows from listbox
    index = list_box.curselection()
    # Go through all of indexes
    for i in index[::-1]:
        # Delete all selected indexes from database
        Delete.delete(section,indexes_list[i])
        # Delete all selected indexes from listbox
        list_box.delete(first=i,last=None)

# EDIT
def Edit_Note(section, note_id, a):

    #Connect to database
    conn = sqlite3.connect('Notes.db')
    # Update note
    print("Usla u update")
    #conn.cursor().execute('''UPDATE section s SET s=new_notes(section,a) WHERE ID==note_id''')
    conn.commit()
    conn.close()

# ADD
def Add_Note(section, list_box, indexes):

    if(section == 'Job'):
           f = Job.new_note(list_box, indexes)
    elif(section == 'FaF'):
           f = FaF.new_note(list_box, indexes)
    elif(section == 'School'):
           f = School.new_note(list_box, indexes)
    elif(section == 'Travel'):
           f = Travel.new_note(list_box, indexes)
    elif(section == 'Extracurricular'):
           f = Extracurricular.new_note(list_box, indexes)
    elif(section == 'Passwords'):
           f = Passwords.new_note(list_box, indexes)
    elif(section == 'House'):
           f = House.new_note(list_box, indexes)
    elif(section == 'Expenes'):
           f = Expences.new_note(list_box, indexes)
    elif(section == 'Allowance'):
           f = Expences.new_note(list_box, indexes)
