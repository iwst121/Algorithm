from functools import total_ordering

@total_ordering
class Vertex:
    def __init__(self,key,value = None):
        self.key = key
        self.value = value

    def __str__(self):
        return "(Key: "+str(self.key)+",Value: "+str(self.value)+")"
    
    def __repr__(self):
        return str(self)

    def _testConsistency(self,other):
        if type(self) != type(other):
            raise Exception("Need two vertexes here!")

    def __hash__(self):
        return self.key

    def __lt__(self,other):
        self._testConsistency(other)
        if self.key <= other.key:
            return True
        return False
    
    def __eq__(self,other):
        self._testConsistency(other)
        if self.key == other.key:
            return True
        return False
        
