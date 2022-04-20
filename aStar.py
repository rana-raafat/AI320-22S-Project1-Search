from queue import PriorityQueue



"""
    Remember:
        g(n) is the real cost from current cell to goal
        h(n) is the heuristic value; shortest straight line distance from current cell to goal
        f(n) = g(n) + h(n)
"""

#--- Calculating Heuristic Cost ---#
def h(currentCell, goalCell):
    x1, y1 = currentCell
    x2, y2 = goalCell
    #--- Manhattan distance ---#
    h = abs(x1 - x2) + abs(y1 - y2)
    return (h)
    
def aStar(maze, start, goal):
    """
        Note that:
            maze.grid is an array provided by the pyamaze module with all maze cells
    """
    #--- initialize g(n) as infinty for all maze cells ---#
    g = {cell: float("inf") for cell in maze.grid}
    g[start] = 0

    #--- initialize g(n) as infinty for all maze cells ---#
    f = {cell: float("inf") for cell in maze.grid}
    #--- no need to add g(start) here, as it is 0 ---#
    f[start] = h(start, goal)
    
    queue = PriorityQueue()
    #--- stored in queue tuple are: f(n), h(n), n ---#
    queue.put((h(start, goal), h(start, goal), start))
    """
        Remember:
            Priority queue will arranges itself according to tuple instances in order...
            So the cell with the lowest f(n) will be in front; and if two cells have the same f(n) value,
            the one with lower h(n) will be in front of the other.
    """

    #--- ??? ---# 
    reversedPath = {}

    #--- ??? ---#
    searchPath = [start]

    while not queue.empty():
        currentCell = queue.get()[2]    #--- get() retrieves the first queue element ---#
                                        #--- as mentioned before, tuple of index 2 is the cell itself ---#
        #--- ??? ---#        
        searchPath.append(currentCell)

        if currentCell == goal:
            break   

        for wall in 'EWNS':
            """
                Note that:
                    maze.maze_map is dictionary provided by the pyamaze module which has the
                    information of each maze cell walls as following...
                        (2, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 1}
                        
                    value of 1 means wall is open, and 0 closed
                    E: East, W: West, N: North, S: South
            """
            if maze.maze_map[currentCell][wall]==True:
                if wall=='E':
                    childCell=(currentCell[0],currentCell[1]+1)

                elif wall=='W':
                    childCell=(currentCell[0],currentCell[1]-1)

                elif wall=='N':
                    childCell=(currentCell[0]-1,currentCell[1])

                elif wall=='S':
                    childCell=(currentCell[0]+1,currentCell[1])

                #--- g() of child cell is one step ahead of current cell's g() ---# 
                temp_g = g[currentCell] + 1
                temp_f = temp_g + h(childCell, goal)

                #--- if lower f() than stored, update ??? ---# 
                if temp_f < f[childCell]:   
                    g[childCell] = temp_g
                    f[childCell] = temp_g + h(childCell, goal)
                    queue.put((f[childCell], h(childCell, goal), childCell))

                    #--- dictionary; went to [key] cell from [value] cell??? ---# 
                    reversedPath[childCell] = currentCell

    #--- to get actual path, we must reverse the stored reversed path from above ---# 
    path={}

    #--- we start looping on the reversed path starting from its initial point; the goal cell ---# 
    cell=goal
    #--- and until the start cell is reached ---# 
    while cell!=start:
        #--- went from [key] cell to [value] cell ??? ---# 
        path[reversedPath[cell]]=cell
        #--- iterate to next cell ??? ---# 
        cell=reversedPath[cell]

    return searchPath, reversedPath, path