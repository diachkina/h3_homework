import uuid
from simple_logger import logger

class User:
    def __init__(self, username, userpass, email):
        self.id = uuid.uuid4()
        self._username = username
        self._userpass = userpass
        self.email = email
        self.log = logger
        self.log.info(f'User ok')

    @property
    def username(self):
        return self._username

    @property
    def userpass(self):
        return '*' * len(self._userpass)


user1 = User("qwerty", "12345", "qwewqe@qew.q")
