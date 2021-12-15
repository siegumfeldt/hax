class Button:
    def __init__(self, is_pushed=False):
        self.is_pushed = is_pushed
    
    def push(self):
        self.is_pushed = True

    def __repr__(self):
        if self.is_pushed:
            return "<Button (pushed)>"
        else:
            return "<Button (not pushed)>"
