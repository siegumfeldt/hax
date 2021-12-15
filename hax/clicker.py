
class Clicker:
    def __init__(self, color):
        self.number = 0
    
    def push(self):
        self.number += 1

    def __repr__(self):
        if self.is_pushed:
            return f"<CLicker (pushed {self.number} times)>"
