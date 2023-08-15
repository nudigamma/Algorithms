'''this file implemenet UnionFind and its optimization class as in the book Algorithms 4th edition by Robert Sedgewick and Kevin Wayne
   this class is used to solve the dynamic connectivity problem
   
   this class is implemented using the eager approach   '''



class UnionFind:
    '''this class is used to solve the dynamic connectivity problem
       in this class the nodes contain the integer id of the component to which they belong, this id
       is the same for all nodes in the same component and the componenents is represented by a node'''
    def __init__(self,n):
        self._id = []
        self._count = n
        for i in range(0,n):
            self._id.append(i)
    def count(self) -> int:
        '''returns the number of components'''
        return self._count
    def connected(self,p,q)-> bool:
        '''returns true if p and q belong to the same component'''
        return self.find(p) == self.find(q)

    def find(self,p) -> int:
        '''returns an the integer id of the component to which p belong'''
        if self.validate(p):
            return self._id[p]
        return None
    

    def union(self,p,q):
        ''' merges two nodes if they belong to different components '''
        pId = self.find(p)
        qId = self.find(q)
        if not qId == pId:
            for node in range(0,n):
                if self._id[node] == pId:
                    self._id[node] = qId
                    self._count -= 1    
    def validate(self,p):
        '''validate that p is a valid index'''
        length = len(self._id)
        try:
            if (p < 0 or p >=  length):
                raise ValueError
        except ValueError:
            print("index " + p + " is not between 0 and " + (length-1))
            return False
        return True


class QuickUnion(UnionFind):
    def __init__(self,n):
        super().__init__(n)
    def print(self):
        super().print()
    def count(self):
        return super().count()
    def validate(self, p):
        super().validate(p)
    def connected(self, p, q):
        return super().connected(p, q)
    def find (self, p):
        while(p != self._id[p]):
            p  = self._id[p]
        return p
    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId != qId:
            self._id[pId] = qId
            self._count -= 1
            

