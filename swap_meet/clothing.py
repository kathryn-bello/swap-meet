from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0.0, age=0):
        super().__init__(id)
        self.fabric = fabric
        self.condition = condition
        self.age = age
    
    def __str__(self):
        string = super().__str__()
        string += f" It is made from {self.fabric} fabric."
        return string