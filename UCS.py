def ucs(graph, start, goal):

    # n is the key and the value is (inf)
    # to set the cost of each cell by setting the value of each key(cell) to values from 1 to infinity
    queue = {n: float('inf') for n in graph.grid}
    queue[start] = 0  # we make the start cell's cost = 0
    visited = {}
    ucsPath = {}
    searchPath = [start]
    while queue:
        # We get the cell with the minimum cost
        currCell = min(queue, key=queue.get)
        visited[currCell] = queue[currCell]
        searchPath.append(currCell)
        if currCell == goal:
            break
        for d in 'ESNW':
            if graph.maze_map[currCell][d] == True:
                if d == 'E':
                    neighbour = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    neighbour = (currCell[0], currCell[1]-1)
                elif d == 'S':
                    neighbour = (currCell[0]+1, currCell[1])
                elif d == 'N':
                    neighbour = (currCell[0]-1, currCell[1])
                if neighbour in visited:
                    continue
                cost = queue[currCell]+1  # we calculate the new cost

                if cost < queue[neighbour]:
                    queue[neighbour] = cost
                    ucsPath[neighbour] = currCell

        queue.pop(currCell)

    revPath = {}
    cell = goal
    while cell != start:
        revPath[ucsPath[cell]] = cell
        cell = ucsPath[cell]

    return searchPath, ucsPath, revPath  # return the path and the total cost
