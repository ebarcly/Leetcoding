class RandomizedSet:

    def __init__(self):
        self.valueIndexMap = {}
        self.valuesList = []

    def insert(self, val: int) -> bool:
        if val in self.valueIndexMap:
            return False

        self.valueIndexMap[val] = len(self.valuesList)
        self.valuesList.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueIndexMap:
            return False
        
        index = self.valueIndexMap[val]
        lastElement = self.valuesList[-1]

        self.valuesList[index] = lastElement
        self.valueIndexMap[lastElement] = index

        self.valuesList.pop()
        del self.valueIndexMap[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.valuesList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()