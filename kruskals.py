def find(parent,i):
    if parent[i]!=i:
        parent[i]=find(parent,parent[i])
    return parent[i]
def kruskals(graph,V):
    mst=[]
    cost=0
    parent=list(range(V))
    graph.sort(key=lambda x:x[2])
    for u,v,weight in graph:
        x,y=find(parent,u-1),find(parent,v-1)
        if x!=y:
            mst.append((u,v,weight))
            parent[y]=x
            cost=cost+weight
            if len(mst)==V-1:
                break
    print("The minimum spanning tree is:",mst)
    print("The minimum cost of minimum spanning tree is:",cost)
V=int(input("Enter the number of vertices:"))
E=int(input("Enter the number of edges:"))
graph=[]
for i in range(E):
    u,v,weight=map(int,input(f"Enter the edge {i+1}(format: u v weight):").split())
    graph.append((u,v,weight))
kruskals(graph,V)