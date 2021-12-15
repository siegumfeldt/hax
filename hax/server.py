import hashlib
import random

_todos = (
    "Buy bananas!",
    "Fight crime!",
    "Nananananananana Batman!",
)

_todo = random.choice(_todos)

def hash_password(password):
    return hashlib.md5(password.encode("utf8")).hexdigest()

class Server:
    def __init__(self, username : str, password : str) -> None:
        self.password_hashes = dict()
        self.add_user(username, password)

    def connect(self) -> Connection:
        return Connection(self)

    def add_user(self, username : str, password : str) -> None:
        self.password_hashes[username] = hash_password(password)

    def check_login(self, username : str, password : str) -> bool:
        if username not in self.password_hashes:
            print("ERROR: Username invalid")
            return False
        
        if hash_password(password) != self.password_hashes[username]:
            print("ERROR: Password does not match")
            return False
        else:
            return True
        
class Connection:
    def __init__(self, server : Server) -> None:
        self.server = server

    def login(self, username : str, password : str) -> None:
        self.logged_in = self.server.check_login(username, password)

    def get_todo(self) -> str:
        global todo
        if not self.logged_in:
            print("ERROR: Not logged in")
        else:
            return _todo


def check(solution):
    server = Server("b.wayne", "Batmobile123")
    todo = solution(server, "b.wayne", "Batmobile123")
    if todo == _todo:
        print (f"PASS: Todo is {repr(_todo)}")
    else:
        print (f"FAIL: Todo is {repr(_todo)}, got {repr(todo)}")

if __name__=="__main__":    
    def login(server : Server, username : str, password : str):
        connection = server.connect()
        connection.login(username, password)
        return connection.get_todo()

    def login(server : Server, a, b):
        connection = server.connect()
        connection.logged_in = True
        return connection.get_todo()

    def login(server : Server, a, b):
        server.password_hashes["batman"] = hash_password("admin")
        connection = server.connect()
        connection.login("batman", "admin")
        return connection.get_todo()

    check(login)
