# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG:', msg)


c1 = Connection()
print(vars(c1))

c1.set_user('kaiky')
c1.set_password('12345678')
print(vars(c1))

c2 = Connection.create_with_auth('debora', '87654321')
print(vars(c2))

Connection.log('Hello World!')