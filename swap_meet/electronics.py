from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id = None, type= "Unknown",condition = 0):
        super().__init__(id)
        self.type= type
        self.condition = condition
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
