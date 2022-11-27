from db_funcs import open_db, insert_into_db, select_from_db, insert_session_into_db, select_session_from_db
from models import Employee
import bcrypt
from getpass import getpass

DB_NAME="company.db"

def login():
    
    #user_id = 2
    username = input("Please enter your username: ")
    password = getpass("Please enter your password: ")
    #password = input("Please enter your password: ") 

    user = select_from_db(DB_NAME, username)
    if user == None:
        #print(user[4])
        print("No account with username provided.")
        return 1
    
    else:
        if bcrypt.checkpw(password.encode(), user[4]):

            ###### Need to change the 'user_id'     
            #employee = Employee(id)

            # Check if a session already exists
            session = select_session_from_db(DB_NAME, user[0])
            if session:
                print("Employee already logged in.")
                return 3
            
            else:     
                # Add user to session
                insert_session_into_db(DB_NAME, user[0])
                print("Session created for user.")     

                print("Successfully logged in.")
                return 0
        
        else:
            print("Incorrect login credentials.")
            return 2


def register():

    firstname = input("Please enter your firstname: ")
    lastname = input("Please enter your lastname: ")
    username = input("Please enter your username: ")
    password_1 = input("Please enter your password: ")
    password_2 = input("Please enter your password again: ")

    # Check username does not already exist
    user = select_from_db(DB_NAME, username)
    # If there is no user with that name
    if user:
        print("This username already exists.")
        return 1

    # Check the passwords match
    else: 
        if password_1 != password_2:
            print("Passwords do not match.")
            return 2

        else:
            hashed_password = bcrypt.hashpw(password_1.encode(), bcrypt.gensalt())
            #print(hashed_password)

            employee = Employee(firstname, lastname, username, hashed_password, 20000)     
            insert_into_db(DB_NAME, employee)
    
            # Need to run a select statement to obtain user's id and then set it in the 'employee' object
            employee_with_id = select_from_db(DB_NAME, employee.username)
            employee.set_employee_id(employee_with_id[0])

            print(f"Employee id: {employee.get_employee_id()}")

            return 0


def logout():
    pass