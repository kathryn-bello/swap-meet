import uuid

class Item:
    def __init__(self, id=None, condition=0.0, age=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition
        self.age = age
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        category = self.get_category()
        return "An object of type "+category+f" with id {self.id}."
    
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
