import uuid
class Item:
    def __init__(self, id = None, condition = 0):

        self.id = uuid.uuid4().int if not id else id 
        self.condition = condition 

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        condition_dict = {
        0: "Mint",
        1: "Excellent",
        2: "Good",
        3: "Fair",
        4: "Poor",
        5: "Heavily Used"   
        }
        return condition_dict[self.condition]
        