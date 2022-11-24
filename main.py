from db_funcs import open_db, insert_into_db, select_from_db
from models import Employee
import bcrypt

DB_NAME="company.db"

open_db(DB_NAME)

passwd = "1234"
hashed_passwd = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())
print(hashed_passwd)

employee = Employee("John", "Smith", "user1", hashed_passwd, 20000)
insert_into_db(DB_NAME, employee)

username = input("Please enter your username: ")
password = input("Please enter your password: ") 
#hashed_password = bcrypt.hashpw(password.encode())
#print(hashed_password)
# , 

user = select_from_db(DB_NAME, username)
#print(user[4])

if bcrypt.checkpw(password.encode(), user[4]):
    print("Successfully logged in.")
else:
    print("Incorrect login credentials.")





    
