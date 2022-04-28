def ucs(graph, start, goal):

    # n is the key and the value is (inf)
    # to set the cost of each cell by setting the value of each key(cell) to values from 1 to infinity
    queue = {n: float('inf') for n in graph.grid}
    queue[start] = 0  # we make the start cell's cost = 0
    steps = {}
    explored = []
    while queue:
        # We get the cell key with the minimum cost value
        currCell = min(queue, key=queue.get)
        explored.append(currCell)
        if currCell == goal:
            break
        for d in 'NEWS':
            if graph.maze_map[currCell][d] == True:
                if d=='N':
                    neighbour=(currCell[0]-1,currCell[1])          
                elif d=='E':
                    neighbour=(currCell[0],currCell[1]+1)
                elif d=='W':
                    neighbour=(currCell[0],currCell[1]-1)
                elif d=='S':
                    neighbour=(currCell[0]+1,currCell[1])

                if neighbour in explored:
                    continue

                cost = queue[currCell]+1  # we calculate the new cost

                #-- overwritten every time a shorter cost path is found --#
                if cost < queue[neighbour]:
                    queue[neighbour] = cost
                    steps[neighbour] = currCell
        #--- we must pop it at the end as we use it's cost to get neighbour's costs ---#
        queue.pop(currCell)

    path = {}
    cell = goal
    while cell != start:
        path[steps[cell]] = cell
        cell = steps[cell]

    return explored, steps, path  # return the path and the total cost
