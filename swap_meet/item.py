import uuid

class Item:
    def __init__(self, id=None, condition=0.0, age=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition
        self.age = age
    
    # returns a string holding the name of the class
    def get_category(self):
        return "Item"
    
    # overriding the str() representation of an object
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    # returns a condition description based on value range from 0 to 5
    def condition_description(self):
        match self.condition:
            case 0:
                return "Heavily used"
            case 1:
                return "Somewhat used"
            case 2:
                return "Mildly used"
            case 3:
                return "Gently used"
            case 4:
                return "Great condition"
            case 5:
                return "Brand new"
            case _:
                return "Invalid condition"
