

class UnionFind:
    '''Union Find class'''
    def __init__(self,n): # Initialize N 
        self.n = n
        self._count = 0
        self._id = []
        for i in range(0,n):
            self._id.append(i)    

    def union(self, p, q) :  # add connection between p and q 
        pass

    def  find(self,p) -> int : # components ieden
        pass    
    
    def connected(self,p,q ) -> bool: #return true if p and q are in the same component number of c
        return self.find(p) == self.find(q)

    def count(self) -> int: #number of componenets
        return self._count
    

    def print(self):
        print(self._id)

    
uf = UnionFind(10)
uf.print()