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
            self.dictionary[key] = value
            self.dictionary.move_to_end(key)
        else:
            if len(self.dictionary) >= self.capacity:
                self.dictionary.popitem(last=False)
            self.dictionary[key] = value
