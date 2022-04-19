# pyamaze is the library that has everything related to the maze
from pyamaze import maze, agent, COLOR


def DFS(graph):
    node = (graph.rows, graph.cols)  # start cell
    explored = [node]  # visited
    frontier = [node]  # stack
    dfsPath = {}  # A dictonary to find the path from start to goal
    dSearch = []
    while len(frontier) > 0:
        currCell = frontier.pop()
        dSearch.append(currCell)  # to show the searching
        if currCell == graph._goal:
            break
        poss = 0
        for d in 'ESNW':
            # maze_map is a dictionary {(1,1): {'E': 0, 'W': 0, 'N': 0, 'S': 1}, ....}
            # checks if the path is open then it will find the neighbour cell
            if graph.maze_map[currCell][d] == True:
                if d == 'E':
                    neighbour = (currCell[0], currCell[1]+1)
                if d == 'W':
                    neighbour = (currCell[0], currCell[1]-1)
                if d == 'N':
                    neighbour = (currCell[0]-1, currCell[1])
                if d == 'S':
                    neighbour = (currCell[0]+1, currCell[1])
                if neighbour in explored:
                    continue
                poss += 1
                explored.append(neighbour)
                frontier.append(neighbour)
                # We store the currCell as value and the neigbour as key
                dfsPath[neighbour] = currCell
        if poss > 1:
            graph.markCells.append(currCell)
    revPath = {}  # to invert the path from start to goal
    cell = graph._goal
    while cell != node:
        # We make the value of the dfsPath as key in the revPath
        revPath[dfsPath[cell]] = cell
        # and the key of the dfsPath as the value in the revPath
        cell = dfsPath[cell]
    return dSearch, dfsPath, revPath
