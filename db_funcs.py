from classes import DB_context_manager

# Create table 
def open_db(DB_NAME):

    with DB_context_manager(DB_NAME) as c:
        c.execute("""

            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                FIRSTNAME TEXT,
                LASTNAME TEXT,
                SALARY INT
            );
            
        """)

    return 0


# Insert employee into DB
def insert_into_db(DB_NAME, employee):
    
    with DB_context_manager(DB_NAME) as c:
        c.execute("INSERT INTO employee (id, FIRSTNAME, LASTNAME, SALARY) VALUES (:id, :firstname, :lastname, :salary)", {'id': None, 'firstname': employee.firstname, 'lastname': employee.lastname, 'salary': employee.salary})
        
    return 0


# Select an employee from DB
def select_from_db(DB_NAME, lastname):
    
    with DB_context_manager(DB_NAME) as c:
        c.execute("SELECT * FROM employee WHERE LASTNAME=:lastname", {'lastname': lastname})
        employees = c.fetchall()

    return employees