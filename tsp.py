def tsp(graph,v,currentPos,n,count,cost,path,answer,city_names):
    if count==n and graph[currentPos][0]:
        answer.append((cost+graph[currentPos][0],path+[0]))
        return
    for i in range(n):
        if not v[i] and graph[currentPos][i]:
            v[i]=True
            tsp(graph,v,i,n,count+1,cost+graph[currentPos][i],path+[i],answer,city_names)
            v[i]=False
def main():
    n=int(input("Enter the number of cities:"))
    city_names=input("Enter the city names(space seperated):").split()
    graph=[]
    for i in range(n):
        row=list(map(int,input(f"Enter the cost row for city {city_names[i]}:").split()))
        graph.append(row)
    v=[False]*n
    v[0]=True
    answer=[]
    tsp(graph,v,0,n,1,0,[0],answer,city_names)
    if answer:
        min_cost,min_path=min(answer,key=lambda x:x[0])
        print(f"Minimum cost:{min_cost}")
        print(f"Minimum path:{'->'.join(city_names[city] for city in min_path)}")
    else:
        print("NO tour found!")
main()
        