from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0.0, age=0):
        super().__init__(id, condition)
        self.type= type
        self.condition = condition
        self.age = age
    
    def __str__(self):
        string = super().__str__()
        string += f" This is a {self.type} device."
        return string