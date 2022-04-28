from queue import PriorityQueue



"""
    Remember:
        g(n) is the real cost from current cell to goal
        h(n) is the heuristic value of current cell; 
                which is the shortest straight line distance from current cell to goal
        f(n) = g(n) + h(n)
"""

#--- Calculating Heuristic Cost ---#
def h(currentCell, goalCell):
    x1, y1 = currentCell
    x2, y2 = goalCell
    #--- Manhattan distance ---#
    h = abs(x2 - x1) + abs(y2 - y1)
    return (h)
    
def aStar(maze, start, goal):
    """
        Note that:
            maze.grid is an array provided by the pyamaze module with all maze cells
    """
    #--- initialize g(n) as infinity for all maze cells ---#
    g = {cell: float("inf") for cell in maze.grid}
    g[start] = 0

    #--- initialize g(n) as infinity for all maze cells ---#
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

    #--- List of cells explored ---#
    explored = []

    #--- Dictionary of moves taken to create path from start cell to goal cell ---# 
    steps = {}


    while not queue.empty():
        currentCell = queue.get()[2]    #--- get() retrieves the first queue element ---#
                                        #--- as mentioned before, index 2 of tuple is the cell itself ---#
        #--- adding cell currently being explored into 'explored' list ---#        
        explored.append(currentCell)

        if currentCell == goal:
            break   

        #--- loops on all four walls of current cells and adds to queue if open ---#
        for wall in 'NEWS':
            """
                Note that:
                    maze.maze_map is dictionary provided by the pyamaze module which has the
                    information of each maze cell walls as following...
                        (2, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 1}
                        
                    value of 1 means wall is open, and 0 closed
                    E: East, W: West, N: North, S: South
            """
            #--- checks if the iteration's 'wall' is open ---#  
            if maze.maze_map[currentCell][wall]==True:
                #--- then checks which one of the four was it, and decides child location accordingly---#
                if wall=='N':
                    childCell=(currentCell[0]-1,currentCell[1])

                elif wall=='E':
                    childCell=(currentCell[0],currentCell[1]+1)

                elif wall=='W':
                    childCell=(currentCell[0],currentCell[1]-1)

                elif wall=='S':
                    childCell=(currentCell[0]+1,currentCell[1])

                #--- g() of child cell would cost one more step ahead of current cell's g() ---# 
                temp_g = g[currentCell] + 1
                temp_f = temp_g + h(childCell, goal)
                #--- but note that it's just a temporary cost that may or may not be stored ---#
                #--- in the dictionaries 'g'/'f'; as we don't store it right away but rather ---#
                #--- check first if it has been visited before or not... ---#
                if childCell not in explored:   
                    #--- if lower, update in dictionary and add to queue ---# 
                    g[childCell] = temp_g
                    f[childCell] = temp_g + h(childCell, goal)
                    queue.put((f[childCell], h(childCell, goal), childCell))
                    #--- store move; went to key [childCell] cell from value [currentCell] ---# 
                    """
                        Note that:
                            Dictionaries' keys must be unique. 
                            So we can't store the currentCell as key to the step, as it possibly can open 
                            more than one child (will not be unique).
                            We must instead store the child cell as key to the step, as it will only 
                            have one parent. 
                    """ 
                    steps[childCell] = currentCell
                    

    #--- we'll find that the stored 'steps' are actually not tracable unless backwards ---# 
    #--- so to get a proper path, we must backtrack those 'steps' taken/stored above ---#
    #--- and store as we go a swapped version of the keys/values---# 
    path={}

    #--- we start iterating on them starting from the goal cell; ---# 
    #--- as it will be the last cell entered as dictionary key ---# 
    cell=goal
    #--- and until the starting cell is reached ---# 
    while cell!=start:
        #--- store move; went from key [parentCell] cell to value [cell] ---# 
        path[steps[cell]]=cell
        #--- next cell to be iterated would be the one we treaded that step from; the parent cell; ---#
        #--- which is as mentioned before is the dictionary value of a cell as key ---# 
        cell=steps[cell]
        

        
    return explored, steps, path