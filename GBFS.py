from queue import PriorityQueue


#--- Heurtistic values are calculated using Manhattan distance ---#
def h(currentCell, goalCell):
    x1, y1 = currentCell
    x2, y2 = goalCell
    h = abs(x1 - x2) + abs(y1 - y2)
    return (h)
    
def GBFS(maze, start, goal):
    
    #--- initialize h(n) as infinity for all maze cells, ---#
    #--- until calculated when getting added to priority queue ---#
    heuristic = {cell: float("inf") for cell in maze.grid}
    heuristic[start] = h(start, goal)

    queue = PriorityQueue()
    queue.put((heuristic[start], start))

    explored = []

    steps = {}

    while not queue.empty():
        currentCell = queue.get()[1]    #--- removes/returns cell in start of priority queue; ---#
                                        #--- which is the one with the least heuristic value ---#
                                   
        explored.append(currentCell)

        if currentCell == goal:
            break   

        for wall in 'NEWS':
            """
                Note that:
                    maze.maze_map is dictionary provided by the pyamaze module which has the
                    information of each maze cell walls as following...
                        (2, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 1}
                        
                    value of 1 means wall is open, and 0 closed
                    E: East, W: West, N: North, S: South
            """
            if maze.maze_map[currentCell][wall]==True:
                if wall=='N':
                    childCell=(currentCell[0]-1,currentCell[1])
                    
                elif wall=='E':
                    childCell=(currentCell[0],currentCell[1]+1)

                elif wall=='W':
                    childCell=(currentCell[0],currentCell[1]-1)

                elif wall=='S':
                    childCell=(currentCell[0]+1,currentCell[1])

                if childCell not in explored:   
                    heuristic[childCell] = h(childCell, goal)
                    queue.put((heuristic[childCell], childCell))
                    #--- went to key [childCell] cell from value [currentCell] ---# 
                    steps[childCell] = currentCell

    #--- backtrack steps to find path ---#

    path={}

    cell=goal
    while cell!=start:
        #--- went from key [parentCell] cell to value [cell] ---# 
        path[steps[cell]]=cell
        #--- parent cell next to be iterated ---#
        cell=steps[cell]



    return explored, steps, path