from db_funcs import open_db, insert_into_db, select_from_db
from auth import login, register, logout 
from decorators import login_required

DB_NAME="company.db"

open_db(DB_NAME)

@login_required
def some_secure_function():
    print("This function will run and shows results after the decorator has run.")


user_input = input("Please enter your option: ")
if user_input == '1':
    logout()
else: 
    # This function will prompt user for login information before running
    some_secure_function()

