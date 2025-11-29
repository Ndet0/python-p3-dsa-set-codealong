class MySet:
    def __init__(self, items=None):
        self.dictionary = {}
        if items:
            for item in items:
                self.dictionary[item] = True

    def add(self, item):
        self.dictionary[item] = True

    def delete(self, item):
        if item in self.dictionary:
            del self.dictionary[item]

    def has(self, item):
        return item in self.dictionary

    def size(self):
        return len(self.dictionary)
