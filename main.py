from db_funcs import open_db, insert_into_db, select_from_db
from models import Employee

DB_NAME="company.db"

open_db(DB_NAME)

employee = Employee("John", "Smith", "user1", "1234", 20000)
insert_into_db(DB_NAME, employee)

username = input("Please enter your username: ")
password = input("Please enter your password: ") 


user = select_from_db(DB_NAME, username)
#print(user[4])

if user[4] == password:
    print("Successfully logged in.")
else:
    print("Incorrect login credentials.")





    
