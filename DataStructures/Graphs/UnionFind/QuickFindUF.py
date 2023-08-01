'''this file implemenet QuickFindUF class as in the book Algorithms 4th edition by Robert Sedgewick and Kevin Wayne
   this class is used to solve the dynamic connectivity problem
   
   this class is implemented using the eager approach   '''

class QuickFindUF:

    def __init__(self, n):
        '''Initializes an empty union-find data structure with 
        n elements through n-1
        @param n the number f elements'''
        try:
         if n < 0:
            raise ValueError
        except ValueError:
                print("n cannot be negative")

        self._id = []
        self._count =  n
        for i in range(0,self._count):
            self._id.append(i)

    def print(self):
        print(self._id)

    def count(self):
        return self._count
    
    def validate(self, p):
        length = len(self._id)
        try:
            if (p < 0 or p >=  length):
                raise ValueError
        except ValueError:
            print("index " + p + " is not between 0 and " + (length-1))

    def find(self, p):
        self.validate(p)
        return self._id[p]
    
    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return self._id[p] == self._id[q]
    
    def union(self, p, q):
        self.validate(p)
        self.validate(q)
        pId = self._id[p]
        qId = self._id[q]
        if pId  !=  qId:
            for i in range(0,len(self._id)):
                if self._id[i] == pId:
                    self._id[i] = qId     
                    self._count -= self._count
               

