class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.edges=[]
    def add_edges(self,u,v,w):
        self.edges.append((u,v,w))
    def bellman_ford(self,source):
        distances={v:float('inf') for v in self.vertices}
        distances[source]=0
        n=len(self.vertices)
        for _ in range(n-1):
            for u,v,w in self.edges:
                if distances[u]+w<distances[v]:
                    distances[v]=distances[u]+w
        for u,v,w in self.edges:
            if distances[u]+w<distances[v]:
                return -1
        return distances
vertices=input("Enter the vertices(space seprated):").split()
g=Graph(vertices)
edge_count=int(input("Enter the number of edges:"))
for _ in range(edge_count):
    u,v,w=input("Enter the edge(format: u v w):").split()
    g.add_edges(u,v,int(w))
source_vertex=input("Enter the source vertex:")
result=g.bellman_ford(source_vertex)
if result==-1:
    print("Negetive cycle found!!!")
else:
    print("Vertex distsnce from source:")
    for vertex,distance in result.items():
        print(f"{vertex} \t\t {distance}")