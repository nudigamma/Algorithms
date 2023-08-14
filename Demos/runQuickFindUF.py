
import QuickFindUF as qf
import sys
import unittest



def testUF():
    validated_ids =[1, 1, 1, 8, 8, 1, 1, 1, 8, 8]
    with open('tinyUF.txt') as f:
        n = int(f.readline())
        uf = qf.QuickFindUF(n)
   
        for line in f:
            p,q = int(line.split()[0]), int(line.split()[1])
            if (uf.connected(p,q)):
                continue
            uf.union(p,q)
            uf.print()
    assert uf.ids() == validated_ids


def testQF():
    validated_ids =[1, 1, 1, 8, 8, 1, 1, 1, 8, 8]
    with open('tinyUF.txt') as f:
        n = int(f.readline())
        uf = qf.QuickUnion(n)
   
        for line in f:
            p,q = int(line.split()[0]), int(line.split()[1])
            if (uf.connected(p,q)):
                continue
            uf.union(p,q)
            uf.print()
    #assert uf.ids() == validated_ids
#testUF()
testQF()