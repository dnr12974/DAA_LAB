import timeit
def dfs(graph,start,visited=None):
    if visited is None:
        visited=[]
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)
    return visited
def main():
    graph={}
    print("Enter the graph as adjacency list(enter 'done' to finish):")
    while True:
        line=input()
        if line.lower()=="done":
            break
        parts=line.split()
        node=parts[0]
        neighbor=parts[1:]
        graph[node]=neighbor
    start_node=input("Enter the source vertex:")
    reachable_nodes=dfs(graph,start_node)
    print(f"The nodes reachable from {start_node} are:{reachable_nodes}")
    time_taken=timeit.timeit(lambda:dfs(graph,start_node),number=1000)
    print(f"The running time={time_taken}")
main()
