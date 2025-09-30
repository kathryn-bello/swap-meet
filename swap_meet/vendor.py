class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory else []

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_id(self, id = None):
        for items in self.inventory:
            if id == items.id:
                return items
        return None

    def swap_items(self,other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False
        
    def swap_first_item(self,other_vendor):
        if self.inventory and other_vendor.inventory:
            self.swap_items(other_vendor, self.inventory[0],other_vendor.inventory[0])
            return True

        return False