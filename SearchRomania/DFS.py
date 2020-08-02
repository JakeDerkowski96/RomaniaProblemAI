def DFSearch(graph, origin, destination):
    # initialize our path list with the root node
    path_list = [[origin]]
    explored = []
    cost = 0
    # will only work if list is not empty
    while path_list:
        cost += 1
        # pop out the last on the path list
        path = path_list.pop()

        # completed
        last_node = path[-1]
        if last_node == destination:
            return path, explored, cost

        else:
            for node in graph[last_node]:
                if node not in path:
                    explored.append(node)
                    # make and add to new path
                    new_path = path + [node]
                    path_list.append(new_path)

    # then there does not exist a route
    print(f'No path exists between {origin} and {destination}')
