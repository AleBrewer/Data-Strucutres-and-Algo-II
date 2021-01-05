class Hash_Map:

    # Constructor with initial capacity
    # Makes all buckets in table empty
    def __init__(self, initial_capacity=41):

        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def add(self, key, value):
        self.table.insert(key, value)

    def get(self, key):
        get_item = self.table.__getitem__(key)
        return get_item

    def update(self, key, item, value):
        get_item = self.table.__getitem__(key)
        get_item.pop(item)
        get_item.insert(item, value)



        #if self.table[key_hash] is not None:
        #    for pair in self.table[key_hash]:
        #        if pair[0] == key:
        #            pair[1] = value
        #            print(pair[1])
        #            return True
        #else:
        #    print ("Error")



        #get_item = self.table.__getitem__(key)
        #get_item.append(value)

        print("sadness")
        #update_item = self.table.__setitem__(key)
        #self.table.append(value)




