class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        
        return False
    
    def get_by_id(self, search_id):
        if isinstance(search_id, int):
            for item in self.inventory:
                if item.id == search_id:
                    return item
            return None
        else:
            return "Invalid input. Id must be a number."
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        
        return True
        
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True
    
    def get_by_category(self, category):
        items_in_category = []
        
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
            else:
                continue
        
        return items_in_category

    def get_best_by_category(self, category):
        best_item_condition = 0
        best_item = None
        
        if not self.get_by_category(category):
            return None
        else:
            for item in self.get_by_category(category):
                if item.condition > best_item_condition:
                    best_item_condition = item.condition
                    best_item = item
        
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.get_best_by_category(their_priority) or not other_vendor.get_best_by_category(my_priority):
            return False
        
        self.swap_items(other_vendor, self.get_best_by_category(their_priority), other_vendor.get_best_by_category(my_priority))
        
        return True
        
    def get_newest_item(self):
        newest_age = 1000
        newest_item = None
        
        if not self.inventory:
            return None
        else:
            for item in self.inventory:
                if item.age < newest_age:
                    newest_age = item.age
                    newest_item = item
                
            return newest_item
        
    def swap_by_newest(self, other_vendor):
        if not other_vendor.inventory or not self.inventory:
            return False
        else:
            self.swap_items(other_vendor, self.get_newest_item(), other_vendor.get_newest_item())
            return True
