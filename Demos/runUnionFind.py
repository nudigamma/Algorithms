
import sys
import unittest
import os

sys.path.append(os.path.abspath(r'D:\source\Algorithms\DataStructures\Graphs\UnionFind'))

from UnionFind import QuickFind

main_data_dir = os.path.join(r'D:\\' ,'Data')
test_validation_dir = os.path.join(main_data_dir,'TestsAndValidations')

def main():


    with open(os.path.join(main_data_dir,'tinyUF.txt')) as f:
        lines = f.readlines()
    connection_map = [(int(line[0]),int(line[2])) for line in lines[1:]]
    
    QF = QuickFind(len(connection_map))
    QF.connect(connection_map)
    QF.print()  
if __name__ == '__main__':
    main()

    