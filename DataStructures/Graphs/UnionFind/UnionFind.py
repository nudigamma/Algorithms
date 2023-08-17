'''this file implemenet UnionFind and its optimization class as in the book Algorithms 4th edition by Robert Sedgewick and Kevin Wayne
   this class is used to solve the dynamic connectivity problem
   
   this class is implemented using the eager approach   '''

from abc import ABC, abstractmethod


class UnionFind():
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
    
    def print(self):
        print(f"This network has {self._count} components")
        print("node",end=" ")
        [print(f"{i}",end=" ") for i in range(0,len(self._id))]
        print("\n")
        print("comp",end=" ")
        [print(f"{self._id[i]}",end=" ") for i in range(0,len(self._id))]

    @abstractmethod
    def find(self,p) -> int: #we postpone the implementation of this method to the different subclasses
        pass
    @abstractmethod
    def union(self,p,q): #we postpone the implementation of this method to the different subclasses
        pass
       


class QuickFind(UnionFind):
    ''' this method is called quick find because the find operation is very fast, it is O(1)'''

    def __init__(self,n):
        super().__init__(n)
 
    def find (self, p) -> int:
        '''returns the component to which p belongs'''
        return self._id[p]
    
    def connect(self,map):
        '''connects the nodes in the map'''
        for node1,node2 in map:
            if not self.connected(node1,node2):
                self.union(node1,node2)
        
    def union(self, p, q):
        pId = self.find(p) # 3
        qId = self.find(q) # 8
        if pId != qId:
            for i in range(0,len(self._id)):
                if self._id[i] == pId:
                    self._id[i] = qId
            self._count -= 1

