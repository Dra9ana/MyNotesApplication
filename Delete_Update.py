import sqlite3

def deleting_Note(section, note_id):

    #Connecting to sqlite database
    conn = sqlite3.connect('Notes.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Deleting records
    cursor.execute('''DELETE FROM section WHERE ID==note_id''')


    #Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()


# ok ovo treba da se zavrsi, nisam imala inspiraciju 
def update_Note(section, note_id, a):
    conn = sqlite3.connect('Notes.db')
    #conn.cursor().execute('''UPDATE section  FROM section WHERE ID==note_id''')
    conn.commit()
    conn.cursor().close()
    
    
    
    
    
