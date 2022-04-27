def BFS(graph, node, goal):

    l = [node]
    queue = [node]  # frontier
    bfsPath = {}  # A dictonary to find the path from start to goal
    bSearch = [node]  # explored

    while queue:
        currCell = queue.pop(0)  # it removes/retrieves from the start
        bSearch.append(currCell)
        if currCell == goal:
            break
        for d in 'ESNW':
            # maze_map is a dictionary {(1,1): {'E': 0, 'W': 0, 'N': 0, 'S': 1}, ....}
            # checks if the path is open then it will find the neighbour cell
            if graph.maze_map[currCell][d] == True:
                if d == 'E':
                    neighbour = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    neighbour = (currCell[0], currCell[1]-1)
                elif d == 'S':
                    neighbour = (currCell[0]+1, currCell[1])
                elif d == 'N':
                    neighbour = (currCell[0]-1, currCell[1])
                if neighbour in l:
                    continue
                l.append(neighbour)
                queue.append(neighbour)
                # We store the currCell as value and the neighbour as key
                bfsPath[neighbour] = currCell

    revPath = {}  # to invert the path from start to goal
    cell = goal
    while cell != node:
        # We make the value of the bfsPath as key in the revPath
        revPath[bfsPath[cell]] = cell
        # and the key of the bfsPath as the value in the revPath
        cell = bfsPath[cell]
    return bSearch, bfsPath, revPath
