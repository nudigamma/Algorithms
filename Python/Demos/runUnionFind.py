'''this demo runs the UnionFind class and prints the results'''

import sys
import unittest
import os

sys.path.append(os.path.abspath(r'D:\source\Algorithms\DataStructures\Graphs\UnionFind'))

from UnionFind import *

main_data_dir = os.path.join(r'D:\\' ,'Data')
test_validation_dir = os.path.join(main_data_dir,'TestsAndValidations')

def main():

    with open(os.path.join(main_data_dir,'tinyUF.txt')) as f:
        lines = f.readlines()
    connection_map = [(int(line[0]),int(line[2])) for line in lines[1:]]
    QF = QuickFind(len(connection_map))
    QF.connect(connection_map)
    QF.print()  


    QU = QuickUnion(len(connection_map))
    QU.connect(connection_map)
    QU.print()

    WQU = WeightedQuickUnion(len(connection_map))
    WQU.connect(connection_map)
    WQU.print()

    
if __name__ == '__main__':
    main()

    