# Create a Backpack class
class Backpack():
    def __init__(self):
        self.items = []

    #add item to backpack
    def addItem(self, item):
        self.items.append(item)
        return self.items

    #remove item from backpack
    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
            print(item + " was removed from the backpack.")
        else:
            print(item + " was not found in your backpack.")

    # Display items in the backpack
    def displayItems(self):
        if not self.items:
            print("Your backpack is empty.")
        else:
            print("Items in backpack")
            for item in self.items:
                print(item)


    def itemList(self):
        list = []
        for item in self.items:
                list.append(item)
        return list
