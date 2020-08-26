import sqlite3
import Delete
def deleting_Note(section, list_box, indexes_list):



    #Creating a cursor object using the cursor() method
    conn = sqlite3.connect('Notes.db')
    cursor = conn.cursor()

    #Deleting records
    index=list_box.curselection()
    for i in index[::-1]:
        #write for whole programme
        Delete.delete_from_section(conn,section,indexes_list[i])
        list_box.delete(first=i,last=None)

    #Commit your changes in the database
    conn.commit()
    conn.close()




# ok ovo treba da se zavrsi, nisam imala inspiraciju
def update_Note(section, note_id, a):
    conn = sqlite3.connect('Notes.db')
    print("Usla u update")
    #conn.cursor().execute('''UPDATE section s SET s=new_notes(section,a) WHERE ID==note_id''')
    conn.commit()
    conn.close()
