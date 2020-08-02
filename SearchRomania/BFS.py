# finds shortest path between 2 nodes of a graph using BFS
def BFSearch(graph, start, goal):
    # visited
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    # keep track of the cost of the search
    cost = 0

    # return path if start is goal
    if start == goal:
        return "You are already in Bucharest!"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            cost += 1
            neighbors = graph[node]
            # go through all neighbor nodes, construct a new path and
            # push it into the queue
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                # return path if neighbor is goal
                if neighbor == goal:
                    explored.append(goal)
                    return new_path, explored, cost

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "Connecting path doesn't exist"
