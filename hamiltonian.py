# Python Code to check whether the given graph
# contains Hamiltonian Cycle using backtracking

# Check if it's valid to place vertex at current position
def isSafe(vertex, graph, path, pos):
    
    # The vertex must be adjacent to the previous vertex
    if not graph[path[pos - 1]][vertex]:
        return False

    # The vertex must not already be in the path
    for i in range(pos):
        if path[i] == vertex:
            return False

    return True

# Recursive backtracking to construct Hamiltonian Cycle
def hamCycleUtil(graph, path, pos, n):
    
    # Base case: all vertices are in the path
    if pos == n:
        
        # Check if there's an edge from 
        # last to first vertex
        return graph[path[pos - 1]][path[0]]

    # Try all possible vertices as next candidate
    for v in range(1, n):
        if isSafe(v, graph, path, pos):
            path[pos] = v

            if hamCycleUtil(graph, path, pos + 1, n):
                return True

            # Backtrack if v doesn't lead to a solution
            path[pos] = -1

    return False

# Initialize path and invoke backtracking function
def hamCycle(graph):
    n = len(graph)
    path = [-1] * n

    # Start path with vertex 0
    path[0] = 0

    if not hamCycleUtil(graph, path, 1, n):
        return [-1]

    return path

# Driver Code
if __name__ == "__main__":
    
    # Representation of the given graph
    #    (0)-(1)-(2) 
    #     |  / \  | 
    #     | /   \ | 
    #     |/     \| 
    #    (3)-----(4)
    graph = [
        [0, 1, 0, 1, 0], 
        [1, 0, 1, 1, 1], 
        [0, 1, 0, 0, 1], 
        [1, 1, 0, 0, 1], 
        [0, 1, 1, 1, 0]
    ]

    path = hamCycle(graph)

    if path[0] == -1:
        print("Solution does not Exist")
    else:
        for i in range(len(path)):
            print(path[i], end=" ")

        # Print the first vertex again 
        # to complete the cycle
        print(path[0])
