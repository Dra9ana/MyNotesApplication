import sqlite3

def output_table(s, i):

    # Conect to database
    conn = sqlite3.connect('Notes.db')
    # Open coursor
    cursor=conn.cursor()
    # Get section from database
    if(s == 'Job'):
       cursor.execute("SELECT * FROM  Job WHERE generated_id = ?",(i,) )
    elif(s == 'FaF'):
         cursor.execute("SELECT * FROM  FaF WHERE generated_id = ?",(i,) )
    elif(s == 'School'):
         cursor.execute("SELECT * FROM  School WHERE generated_id = ?",(i,) )
    elif(s == 'Travel'):
         cursor.execute("SELECT * FROM  Travel WHERE generated_id = ?",(i,) )
    elif(s == 'Extracurricular'):
         cursor.execute("SELECT * FROM  Extracurricular WHERE generated_id = ?",(i,) )
    elif(s == 'Passwords'):
         cursor.execute("SELECT * FROM  Passwords WHERE generated_id = ?",(i,) )
    elif(s == 'House'):
         cursor.execute("SELECT * FROM  House WHERE generated_id = ?",(i,) )
    elif(s == 'Expences'):
         cursor.execute("SELECT * FROM  Expences WHERE generated_id = ?",(i,) )
   
    # Get rows from database
    rows=cursor.fetchall()
    # Close database
    conn.close()
    # Return rows
    return rows

# Get last selected row
def get_row(section, list_box, indexes_list):
        # Get indexes of currently selected items
        index  = list_box.curselection()
        # If there are no selected items set i_prev=-1
        i_prev = -1
        # Go through indexes of database
        for i in index:
            # Convert index in database to index in listbox
            i_prev = indexes_list[i]
        # If some item is selected
        if(i_prev >= 0):
             # Get rows from database
             rows = output_table(section, i_prev)
             # Get the last selected row
             s = rows[0]
             return s
        else:
             return []

def select_name(s):

    # Connect to database
    conn = sqlite3.connect('Notes.db')
    # Open cursor
    cursor = conn.cursor()

    # Find rows of name and indes from section
    if(s == 'Job'):
        cursor.execute("SELECT generated_id,name FROM Job")
    elif(s == 'FaF'):
          cursor.execute("SELECT generated_id,name FROM FaF")
    elif(s == 'School'):
         cursor.execute("SELECT generated_id,name FROM School")
    elif(s == 'Travel'):
          cursor.execute("SELECT generated_id,name FROM Travel")
    elif(s == 'Extracurricular'):
          cursor.execute("SELECT generated_id,name FROM Extracurricular")
    elif(s == 'Passwords'):
          cursor.execute("SELECT generated_id,name FROM Passwords")
    elif(s == 'House'):
          cursor.execute("SELECT generated_id,name FROM House")
    elif(s == 'Expences'):
          cursor.execute("SELECT generated_id, date FROM Expences")
    # Get rows
    rows = cursor.fetchall()
    # Close database
    conn.close()

    # Return rows
    return rows
