#Import The needed Libraries
import sqlite3

# Connect to the SQL API
conn = sqlite3.connect("info.db")
#Cursor
cursor = conn.cursor()

def main():
   #SQL Code to be executed
   cursor.execute('''
               CREATE TABLE IF NOT EXISTS information(
                  TITLE TEXT,
                  USER TEXT,
                  PASSWORD TEXT
                  )    
   ''')

   print("Database Succesfully Created")
   conn.commit()
   conn.close()



if __name__ == "__main__":
   main()
else:
   print("Error")