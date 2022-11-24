class Employee:

    def __init__(self, firstname, lastname, username, password, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.salary = salary 


    def __repr__(self):
        return f"Employee({self.firstname}, {self.lastname}, {self.username}, {self.salary})"  