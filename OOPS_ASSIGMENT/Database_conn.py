class Database:
    def __init__(self, host):
        self.host = host
        print(f"Connected to database at {self.host}")


class MySQLDatabase(Database):
    def __init__(self, host, user):
        super().__init__(host)
        self.user = user
        print(f"MySQL User: {self.user}")


db = MySQLDatabase("localhost", "admin")