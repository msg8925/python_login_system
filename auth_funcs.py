from file_context_manager import file_context_manager

def set_current_logged_in_employee(employee):

    with file_context_manager("auth_vars.pkl", "wb") as f:
        f.write(employee)

    return 0    


def get_current_logged_in_employee():

    with file_context_manager("auth_var.pkl", "rb") as f:
        employee = f.read()
        return employee        


