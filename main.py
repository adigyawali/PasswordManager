'''
This program is a storage that stores data
Author:ME
'''
#Import The needed Libraries
import sqlite3
import os

# Connect to the SQL API
conn = sqlite3.connect("info.db")
#Cursor
cursor = conn.cursor()


# Insert information into the table
def insertInto(title, user, passW):
    cursor.execute("INSERT INTO information (TITLE, USER, PASSWORD) VALUES (?, ?, ?)", (title, user, passW))
    #Commit
    conn.commit()


# Print all the usernames/Emails
def printAlltitles():
    #Print the information from the table
    cursor.execute('''
                    SELECT TITLE FROM information            
    ''')

    rows = cursor.fetchall()
    print("+-+-+-+-+-+-+-+-+")
    print(f"| {'TITLE':<14}|")
    print("+-+-+-+-+-+-+-+-+")

    for i in range(len(rows)):
        print(f"| {rows[i][0]:<14}|")
        print("+---------------+")


def printPass(title):
    cursor.execute("SELECT * FROM information WHERE TITLE = ?", (title,))
    rows = cursor.fetchall()

    #Too lazy to consider same email for multiple things, print all passwords for one username/email
    print("+---------------+---------------+---------------+")
    print(f"{'TITLE':<15} | {'USERNAME/EMAIL':<15}| {'PASSWORD':<15}")
    print("+---------------+---------------+---------------+")

    for i in range(len(rows)):
        print(f"{rows[i][0]:<15} | {rows[i][1]:<15}| {rows[i][2]:<15}")
        print("+---------------+---------------+---------------+")


#Clear the terminal while quitting
def clear():
    if os.name == "nt":  # If running on Windows
        os.system("cls")
    else:  # If running on macOS/Linux
        os.system("clear")
        

#Main program
def main():
    #Loop
    programLoop = True

    while programLoop == True:
        userInput = input().strip().lower()
        

        #Main commands that the user can do
        if userInput == "help":
            print(" Press 'I' to insert information\n",
                "Press 'D' for list\n",
                "Press 'V' to view specific information\n",
                "Press 'Q' to quit\n")
        

        #Inser Information
        elif userInput == "i":
            title = input("Enter Title: ")
            userName = input("Enter Username/Email: ")
            passW = input("Enter your password: ")

            insertInto(title, userName, passW)

        #Show users
        elif userInput == "d":
            clear()
            printAlltitles()


        elif userInput == "v":
            clear()
            title = input("Enter Title: ")
            clear()
            printPass(title)



        elif userInput == "q":
            clear()
            programLoop = False
            break

        else:
            print("Not a valid input, Try again\n")

    conn.commit()
    conn.close()


#Run the program
if __name__ == "__main__":
    main()