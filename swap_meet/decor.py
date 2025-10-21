from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, width=0, length=0, condition=0.0, age=0):
        super().__init__(id, condition)
        self.width = width
        self.length = length
        self.age = age
    
    def __str__(self):
        string = super().__str__()
        string += f" It takes up a {self.width} by {self.length} sized space."
        
        return string