from file_context_manager import file_context_manager
from pickleEmployee import pickle_object, unpickle_string

# TODO - Need to merge pickle functions into get_current_logged_in_employee
def set_current_logged_in_employee(employee):

    with file_context_manager("auth_vars.pkl", "wb") as f:
        employee = pickle_object(employee)
        f.write(employee)

    return 0    


def get_current_logged_in_employee():

    with file_context_manager("auth_vars.pkl", "rb") as f:
        employee = f.read()
        employee = unpickle_string(employee)
        return employee        


