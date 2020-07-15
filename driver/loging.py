import datetime

class Loging:

    def __init__(self):
        self.log_list = []

    def add_log(self, type_message=None, message=None):
        self.log_list.append(str(datetime.datetime.now()) + ' --- ' + str(type_message) + ' --- ' + str(message))
