class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dictionary.keys():
            self.dictionary.move_to_end(key)
            return self.dictionary[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.dictionary.move_to_end(key)
        self.dictionary[key] = value
        if len(self.dictionary) > self.capacity:
            self.dictionary.popitem(last=False)
        
