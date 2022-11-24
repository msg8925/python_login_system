class Employee:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary 

    def __repr__(self):
        return f"Employee({self.firstname}, {self.lastname}, {self.salary})"  