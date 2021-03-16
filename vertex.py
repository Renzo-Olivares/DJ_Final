import random

class Vertex:
    def __init__(self, val):
        self.predecessor = None
        self.distance = None
        self.value = val

    def __lt__(self, other):
        # Overload the less than operator. This function is called when there needs to be a tie break.
        return random.choice([self,other])