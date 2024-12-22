def prims(V,graph,src):
    cost=0
    edge=0
    dist=[False for _ in range(V)]
    dist[src]=True
    while edge<V-1:
        minimum,x,y=float('inf'),0,0
        for i in range(V):
            if dist[i]:
                for j in range(V):
                    if (not dist[j]) and graph[i][j]:
                        if graph[i][j]<minimum:
                            minimum,x,y=graph[i][j],i,j
        print(x,"-",y,"=",minimum)
        dist[y]=True
        cost=cost+minimum
        edge=edge+1
    print("Minimum Spanning tree cost:",cost)
V=int(input("Enter the number of vertices:"))
graph=[]
print("Enter adjacency matric row by row:")
for i in range(V):
    row=list(map(int,input(f"Enter the row {i+1}:").split()))
    graph.append(row)
src=int(input("Enter the source vertex:(0 indexed):"))
prims(V,graph,src)

