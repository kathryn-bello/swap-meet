from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, id = None, fabric = "Unknown", condition = 0):
        super().__init__(id)
        self.fabric = fabric
        self.condition = condition

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
