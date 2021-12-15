class Switch:
    def __init__(self, is_flipped):
        self.is_flipped = is_flipped

    def flip(self):
        self.is_flipped = not self.is_flipped

    def __repr__(self):
        if self.is_flipped:
            return "<A flipped switch>"
        else:
            return "<An unflipped switch>"
