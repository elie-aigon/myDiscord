from Settings import *

class User:
    def __init__(self, username, password, is_online, status):
        self.username = username
        self.password = password
        self.is_online = is_online
        self.status = status
