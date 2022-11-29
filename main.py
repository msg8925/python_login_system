from db_funcs import open_db
from auth import login, register, logout 
from tasks import some_secure_function 
import os

if __name__=="__main__":

    # Get DB info from dotenv file 
    #DB_NAME=os.getenv("DB_NAME")
    DB_NAME="company.db"
    print(DB_NAME)
    
    # Setup DB
    open_db(DB_NAME)

    while True:

        # Clear terminal
        os.system("cls")

        print("""

            1. Login
            2. Logout
            3. Register
            4. Execute task
            5. Exit

        Please enter your option:

        """)
        user_input = input(">>: ")

        if user_input == '1':
            login()
            user_input = input("Press any key to continue... ")

        elif user_input == '2':
            logout()
            user_input = input("Press any key to continue... ")

        elif user_input == '3':
            register()
            user_input = input("Press any key to continue... ")

        elif user_input == '4': 
            # This function will prompt user for login information before running
            some_secure_function()
            user_input = input("Press any key to continue... ")

        elif user_input == '5':
            print("Exiting...")
            exit()

        else:
            print("Invalid option selected.")
            user_input = input("Press any key to continue... ")
