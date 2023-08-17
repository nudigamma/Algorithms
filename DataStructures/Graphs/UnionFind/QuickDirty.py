
import numpy as np

array1 = np.random.randint(0,10,10)
array2 = np.random.randint(0,10,10)

connection = zip(array1 , array2)

def fill(connection):
    for node1,node2 in connection:
        print(node1,node2)
