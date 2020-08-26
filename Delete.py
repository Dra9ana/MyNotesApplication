# A function that stores new notes in a database

import sqlite3
import New_Job as nj



def delete_from_section(conn,s, i):

   
   cursor=conn.cursor()

   if(s=='Job'):
      cursor.execute("DELETE FROM Job WHERE generated_id = ?",(i,) )
   elif(s=='FaF'):
        cursor.execute("DELETE FROM FaF WHERE generated_id = ?",(i,) )
   elif(s=='School'):
        cursor.execute("DELETE FROM School WHERE generated_id = ?",(i,) )
   elif(s=='Travel'):
        cursor.execute("DELETE FROM Travel WHERE generated_id = ?",(i,) )
   elif(s=='Extracurricular'):
        cursor.execute("DELETE FROM Extracurricular WHERE generated_id = ?",(i,) )
   elif(s=='Passwords'):
        cursor.execute("DELETE FROM Passwords WHERE generated_id = ?",(i,) )
   elif(s=='House'):
        cursor.execute("DELETE FROM House WHERE generated_id = ?",(i,) )

   conn.commit()
