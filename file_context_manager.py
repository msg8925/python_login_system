####################################################
#
#   Desc: 
#
#
####################################################
class file_context_manager():

    # init method runs when object is created
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        print("__init__")

    # enter method runs when an operation such as a write is performed
    def __enter__(self):
        self.f = open(self.filename, self.mode)
        print("__enter__")
        return self.f

    # exit method runs when an operation has finshed
    def __exit__(self, exc_type, exc_cal, traceback):
        print("__exit__")
        self.f.close()