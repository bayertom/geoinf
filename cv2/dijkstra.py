import queue

def dijkstra(G, s, e):
    # Initialize predecessors and w-distances
    p = [-1]*(len(G)+1)    
    d = [float('Inf')]*(len(G)+1)

    # Initialization w-distance of starting node
    d[s]=0

    # Add start node to priority queue      
    Q = queue.PriorityQueue()
    Q.put((0, s))

    #Repeat until Q is empty
    while not Q.empty():
        #Get point with minimum d[u]
        du, u = Q.get()

        print(u)

        #Browse its neighbors
        for v, wuv in G[u].items():
            
            #Relaxation
            if d[u]+wuv < d[v]:
                d[v] = d[u] + wuv
                p[v] = u

                print('  ' + str(v))

                #Add to priority queue
                Q.put((d[v], v))

    return p,d

    
def pathuv(u, v, p, path):
    #Create path from predecessors
    while v != u and v != -1:
        path.append(v)
        v = p[v]
    path.append(v)

#Create graph
G={
    1 : {2:8, 3:4, 5:2},
    2 : {1:8, 3:5, 4:2, 7:6, 8:7},
    3 : {1:4, 2:5, 6:3, 7:4},
    4 : {2:2, 9:3},
    5 : {1:2, 6:5},
    6 : {3:3, 5:5, 7:5, 8:7, 9:10},
    7 : {2:6, 3:4, 6:5, 8:3},
    8 : {2:7, 6:7, 7:3, 9:1},
    9 : {4:3, 6:10, 8:1}
}

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

#Dijkstra algorithm
p, d = dijkstra(G, 1, 9)

#Reconstruct shortest path
path = []
pathuv(1, 9, p, path)

print(path)
print(d[9])
