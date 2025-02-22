class RandomizedSet:
    def __init__(self):
        self.map = {}
        self.values = []
        self.index = -1

    def getRandom(self):
        return random.choice(self.values) if self.values else None
    
    def insert(self, val):
        if self.map.get(val) is None:
            self.index += 1
            self.map[val] = self.index
            self.values.append(val)
            return True
        else:
            return False
    
    def remove(self, val):
        if self.map.get(val) is None:
            return False
        else:
            i = self.map[val]
            j = len(self.values) - 1

            temp = self.values[j]
            self.values[j] = self.values[i]
            self.values[i] = temp

            self.values.pop()
            self.index -= 1
            self.map.pop(val)

            if len(self.values) > 0 and i != j:
                self.map[temp] = i
            return True

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()