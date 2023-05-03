class MakeHashTable:
    def __init__(self, numberOfPackages):
        self.max = numberOfPackages
        self.array = [None for i in range(self.max)]

    def get_hash(self, key):
        return key % self.max

    def add(self, key, value):
        hashVar = self.get_hash(key)
        self.array[hashVar] = value

    # This method takes a key and returns the package.
    def get(self, key):
        hashVar = self.get_hash(key)
        return self.array[hashVar]

    # this method removes the package from the array and sets the value of the index to None
    def remove(self, key):
        hashVar = self.get_hash(key)
        self.array[hashVar] = None
