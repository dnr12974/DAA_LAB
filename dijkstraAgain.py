import heapq
class Graph:
    def __init__(self,V):
        self.V=V
        self.adj=[[] for i in range(self.V)]
    def addEdge(self,u,v,w):
        self.adj[u].append((v,w))
        self.adj[v].append((u,w))
    def dijkstra(self,src):
        pq=[]
        dist=[float('inf')]*self.V
        dist[src]=0
        heapq.heappush(pq,(0,src))
        while pq:
            d,u=heapq.heappop(pq)
            for v,w in self.adj[u]:
                if dist[v]>dist[u]+w:
                    dist[v]=dist[u]+w
                    heapq.heappush(pq,(dist[v],v))
        print("The distance of vertex from source:")
        for i in range(self.V):
            print(i,"\t",dist[i])
v=int(input("Enter the number of vertices:"))
g=Graph(v)
ch=1
while ch:
    u,v,w=map(int,input("Enter the edge(format:u v w):").split())
    g.addEdge(u,v,w)
    ch=int(input("Do you want to continue? 1-YES,0-NO:"))
g.dijkstra(0)
        