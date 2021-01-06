class Hash_Map:

    # Constructor with initial capacity
    # Complexity O(1)
    def __init__(self, initial_capacity=10):
        self.table = []

    #Adds an item to the table at the key
    def add(self, key, value):
        self.table.insert(key, value)

    #Gets an item from the Hash table with the key
    def get(self, key):
        get_item = self.table.__getitem__(key)
        return get_item

    #Removes the old item at the desired location and inserts the new one
    def update(self, key, item, value):
        get_item = self.table.__getitem__(key)
        get_item.pop(item)
        get_item.insert(item, value)

