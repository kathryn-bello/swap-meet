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
    
    ## 6
    def get_by_category(self,category):
        ans = []
        for item in self.inventory:
            if item.get_category() == category:
                ans.append(item)
        return ans
    
    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        info = [None, -1000] # for item and its condition 
        for item in category_list:
            if item.condition > info[1]:
                info = [item, item.condition ]
        return info[0]
    

    def swap_best_by_category(self, other_vendor,my_priority,their_priority):
        if not self.get_best_by_category(their_priority) or not other_vendor.get_best_by_category(my_priority): 
            return False
        else:
            my_trade = self.get_best_by_category(their_priority)
            their_trade = other_vendor.get_best_by_category(my_priority)
            self.swap_items(other_vendor, my_trade, their_trade)
            return True
