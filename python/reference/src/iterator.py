class SimpleIterator():
    def __init__(self, data):
        self._data = data
        self._index = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index > 0:
            self._index -= 1
            return self._data[self._index]
        raise StopIteration