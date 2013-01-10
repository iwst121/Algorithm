from functools import total_ordering

@total_ordering
class Vertex:
    def __init__(self,key,value):
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self,newKey):
        self._key = newKey

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,newValue):
        self.value = newValue

    def _testConsistency(self,other):
        if type(self) != type(other):
            raise Exception("Need two vertexes here!")

    def __lt__(self,other):
        self._testConsistency(other)
        if self.index <= other.index:
            return True
        return False
    
    def __eq__(self,other):
        self._testConsistency(other)
        if self.index == other.index:
            return True
        return False
        
