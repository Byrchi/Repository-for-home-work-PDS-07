

class Custom_type_error(Exception):

    def __init__(self, message):
        self.message = message


    def __str__(self):
        return self.message


raise Custom_type_error ('Somebody wrong')
