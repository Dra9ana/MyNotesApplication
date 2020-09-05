# DELETE A NOTE

# Save as: Delete

import sqlite3

# Delete section from database
def delete(s, i):

    # Connect to database
    conn   = sqlite3.connect('Notes.db')
    # Open coursor
    cursor = conn.cursor()

    if(s == 'Job'):
       cursor.execute("DELETE FROM Job WHERE generated_id = ?",(i,) )
    elif(s == 'FaF'):
         cursor.execute("DELETE FROM FaF WHERE generated_id = ?",(i,) )
    elif(s == 'School'):
         cursor.execute("DELETE FROM School WHERE generated_id = ?",(i,) )
    elif(s == 'Travel'):
         cursor.execute("DELETE FROM Travel WHERE generated_id = ?",(i,) )
    elif(s == 'Extracurricular'):
         cursor.execute("DELETE FROM Extracurricular WHERE generated_id = ?",(i,) )
    elif(s == 'Passwords'):
         cursor.execute("DELETE FROM Passwords WHERE generated_id = ?",(i,) )
    elif(s == 'House'):
         cursor.execute("DELETE FROM House WHERE generated_id = ?",(i,) )

    # Commit your changes in the database
    conn.commit()
    # Close database
    conn.close()
