from classes import DB_context_manager

# Create table 
def open_db(DB_NAME):

    with DB_context_manager(DB_NAME) as c:
        c.execute("""

            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                FIRSTNAME TEXT,
                LASTNAME TEXT,
                USERNAME TEXT,
                PASSWORD TEXT,
                SALARY INT
            );
            
        """)

    return 0


# Insert employee into DB
def insert_into_db(DB_NAME, employee):
    
    with DB_context_manager(DB_NAME) as c:
        c.execute("INSERT INTO employee (id, FIRSTNAME, LASTNAME, USERNAME, PASSWORD, SALARY) VALUES (:id, :firstname, :lastname, :username, :password, :salary)", {'id': None, 'firstname': employee.firstname, 'lastname': employee.lastname, 'username': employee.username, 'password': employee.password, 'salary': employee.salary})
        
    return 0


# Select an employee from DB
def select_from_db(DB_NAME, username):
    
    with DB_context_manager(DB_NAME) as c:
        c.execute("SELECT * FROM employee WHERE USERNAME=:username", {'username': username})
        employee = c.fetchone()

    return employee