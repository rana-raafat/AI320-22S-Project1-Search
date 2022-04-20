from queue import PriorityQueue



def h(currentCell, goalCell):
    x1, y1 = currentCell
    x2, y2 = goalCell
    h = abs(x1 - x2) + abs(y1 - y2)
    return (h)
    
def GBFS(maze, start, goal):
    
    heuristic = {cell: float("inf") for cell in maze.grid}
    heuristic[start] = h(start, goal)

    queue = PriorityQueue()
    queue.put((h(start, goal), start))

    reversedPath = {}

    searchPath = [start]

    while not queue.empty():
        currentCell = queue.get()[1]
                                   
        searchPath.append(currentCell)

        if currentCell == goal:
            break   

        for wall in 'EWNS':
            if maze.maze_map[currentCell][wall]==True:
                if wall=='E':
                    childCell=(currentCell[0],currentCell[1]+1)

                elif wall=='W':
                    childCell=(currentCell[0],currentCell[1]-1)

                elif wall=='N':
                    childCell=(currentCell[0]-1,currentCell[1])

                elif wall=='S':
                    childCell=(currentCell[0]+1,currentCell[1])

                temp_h = h(childCell, goal)

                if temp_h < heuristic[childCell]:   
                    heuristic[childCell] = temp_h
                    queue.put((h(childCell, goal), childCell))
                    reversedPath[childCell] = currentCell

    path={}

    cell=goal
    while cell!=start:
        path[reversedPath[cell]]=cell
        cell=reversedPath[cell]

    #print(heuristic)
    
    return searchPath, reversedPath, path