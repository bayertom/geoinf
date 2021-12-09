import math
from math import *
import operator
from operator import *


#Graph definition
V = [1, 2, 3, 4, 5, 6, 7, 8, 9]

E = [
    [1, 2, 8], 
    [1, 3, 4], 
    [1, 5, 2], 
    [2, 1, 8], 
    [2, 3, 5], 
    [2, 4, 2], 
    [2, 7, 6], 
    [2, 8, 7], 
    [3, 1, 4],  
    [3, 2, 5], 
    [3, 6, 3], 
    [3, 7, 4], 
    [4, 2, 2], 
    [4, 9, 3], 
    [5, 1, 2], 
    [5, 6, 5], 
    [6, 3, 3], 
    [6, 5, 5], 
    [6, 7, 5], 
    [6, 8, 7], 
    [6, 9, 10], 
    [7, 2, 6], 
    [7, 3, 4], 
    [7, 6, 5], 
    [7, 8, 3], 
    [8, 2, 7], 
    [8, 6, 7], 
    [8, 7, 3], 
    [8, 9, 1], 
    [9, 4, 3], 
    [9, 6, 10], 
    [9, 8, 1]
    ]

#Node coordinates X, Y
C = {
    1 : [95, 322],
    2 : [272, 331],
    3 : [173, 298],
    4 : [361, 299],
    5 : [82, 242],
    6 : [163, 211],
    7 : [244, 234],
    8 : [333, 225],
    9 : [412, 196]
}

def find (u, p):
    #Find root to u using parents
    while(p[u] != u):
        p[u] = p[p[u]]
        u = p[u]
    return u

def union(u, v, p):
    # Union of two trees
    ru = find(u,p)
    rv = find(v,p)
    p[ru] = rv

def mst(V,E):
    #Minimum spanning tree by Kruskal
    T = []
    wt = 0
    p = [0] * (len(V) + 1)

    #Make-set
    for v in V:
        p[v] = v
    
    #Sort edges by w
    ES = sorted(E, key=itemgetter(2))

    #Loop through sorted edges
    for e in ES:
        #Take cuttent edge
        u, v, w = e
        
        #u, v have different roots
        if find(u, p) != find(v, p):
            
            #Union of two trees
            union(u,v,p)

            #Add edge to the spanning tree
            T.append([u, v, w])
            
            #Compute weight
            wt = wt + w

    return T, wt

#Minimum spanning tree    
T,wt = mst(V,E)
print(T)
print(wt)
