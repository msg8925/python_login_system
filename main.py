from db_funcs import open_db, insert_into_db, select_from_db
from models import Employee

DB_NAME="company.db"


open_db(DB_NAME)

employee = Employee("John", "Smith", 20000)
insert_into_db(DB_NAME, employee)

result = select_from_db(DB_NAME, "Smith")
print(result)
    
