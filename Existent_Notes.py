import sqlite3

def Existent_Notes(s): 
  conn = sqlite3.connect('Notes.db')
  
  if(s=='Job'):
      conn.cursor().execute('SELECT * FROM Job')
      data = conn.cursor().fetchall()
      print(data)
      for row in data:
          print(row)
        
    elif(s=='FaF'):
        conn.cursor().execute('SELECT * FROM FaF')
        data = conn.cursor().fetchall()
        print(data)
        for row in data:
            print(row)
    elif(s=='School'):
        conn.cursor().execute('SELECT * FROM School')
        data = conn.cursor().fetchall()
        print(data)
        for row in data:
            print(row)
    elif(s=='Travel'):
        conn.cursor().execute('SELECT * FROM Travel')
        data = conn.cursor().fetchall()
        print(data)
        for row in data:
            print(row)
    elif(s=='Extracurricular'):
        conn.cursor().execute('SELECT * FROM Extracurricular')
        data = conn.cursor().fetchall()
        print(data)
        for row in data:
            print(row)
    elif(s=='Passwords'):
        conn.cursor().execute('SELECT * FROM Passwords')
        data = conn.cursor().fetchall()
        print(data)
        for row in data:
            print(row)
    elif(s=='School'):
        conn.cursor().execute('SELECT * FROM School')
        data = conn.cursor().fetchall()
        print(data)
        for row in data:
            print(row)
    elif(s=='House'):
        conn.cursor().execute('SELECT * FROM House')
        data = conn.cursor().fetchall()
        print(data)
        for row in data:
            print(row)

    
read_from_db()
conn.cursor().close
conn.close()
