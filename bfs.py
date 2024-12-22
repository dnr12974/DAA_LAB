import timeit

def bfs(graph, start):
    queue = [start]
    visited = set()
    reachable = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            reachable.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return reachable

def main():
    graph = {}
    print("Enter graph as adjacency list (enter 'done' to finish):")
    
    # Collect the adjacency list from user input
    while True:
        line = input()
        if line.lower() == "done":
            break
        parts = line.split()
        node = parts[0]
        neighbor = parts[1:]
        graph[node] = neighbor

    # Prompt user for the starting node
    start_node = input("Enter the source vertex: ")

    # Get the reachable nodes from the start node
    reachable_nodes = bfs(graph, start_node)
    time_taken = timeit.timeit(lambda: bfs(graph, start_node), number=1000)
    print(f"Running time: {time_taken:.6f} seconds")
    print(f"The nodes reachable from {start_node} are: {reachable_nodes}")

# Execute the main function
main()
