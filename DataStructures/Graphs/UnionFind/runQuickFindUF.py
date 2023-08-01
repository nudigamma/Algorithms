
import QuickFindUF as qf
import sys

def main():
    with open('tinyUF.txt') as f:
        n = int(f.readline())
        pairs = []
        for line in f:
            pairs.append([int(x) for x in line.split()])
    
    uf = qf.QuickFindUF(n)
    print("Initial List")
    uf.print()
    print("initial count of connected components")
    print(uf.count())
    for p,q in pairs:
        if (uf.find(p) == uf.find(q)):
            continue
        uf.union(p,q)
    print("Final List")
    print(uf.print())
    print("Final count of connected components")
    print(uf.count())
if __name__ == '__main__':
    main()