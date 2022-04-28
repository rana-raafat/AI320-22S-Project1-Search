
def DFS(graph, node, goal):

    stack = [node]  # frontier
    steps = {}  # A dictonary to find the steps from start to goal
    explored = []  # explored

    while stack:
        currCell = stack.pop()  # it removes/retrieves from the end of the stack
        explored.append(currCell)
        if currCell == goal:
            break
        """
            Note that:
                the order of the walls; here N->E->W->S, is what decides the order that the open cells
                are going to be entered into stack with.
                thus, it's what decides which one will be visited first (S->W->E->N).
        """
        for d in 'NEWS':
            # maze_map is a dictionary {(1,1): {'E': 0, 'W': 0, 'N': 0, 'S': 1}, ....}
            # checks if the path is open then it will find the neighbour cell
            if graph.maze_map[currCell][d] == True:
                if d=='N':
                    neighbour=(currCell[0]-1,currCell[1])          
                elif d=='E':
                    neighbour=(currCell[0],currCell[1]+1)
                elif d=='W':
                    neighbour=(currCell[0],currCell[1]-1)
                elif d=='S':
                    neighbour=(currCell[0]+1,currCell[1])
                if (neighbour in explored) or (neighbour in stack):
                    continue
                stack.append(neighbour)
                # We store the currCell as value and the neighbour as key
                steps[neighbour] = currCell

    path = {}  # to invert the path from start to goal
    cell = goal
    while cell != node:
        # We make the value of the steps as key in the path
        # and the key of the steps as the value in the path
        path[steps[cell]] = cell
        cell = steps[cell]

    return explored, steps, path
