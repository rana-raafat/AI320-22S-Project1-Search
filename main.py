from tkinter import *

from pyamaze import maze, agent, COLOR, textLabel

from BFS import BFS
from DFS import DFS
from UCS import ucs
from aStar import aStar
from GBFS import GBFS



def applyAlgorithm():  
    mazeWorld = maze()
    mazeWorld.CreateMaze(loadMaze='maze.csv')
    
    start = (mazeWorld.rows, mazeWorld.cols)
    #start = (6,1)
    end = (1,1)

    #searchPath, reversedPath, path = BFS(mazeWorld, start, end)
    #searchPath, reversedPath, path = DFS(mazeWorld, start, end)
    searchPath, reversedPath, path = ucs(mazeWorld, start, end)
    #searchPath, reversedPath, path = aStar(mazeWorld, start, end)
    #searchPath, reversedPath, path = GBFS(mazeWorld, start, end)

    a=agent(mazeWorld, x=start[0], y=start[1], footprints=True, color=COLOR.blue, goal=end)
    b=agent(mazeWorld, x=end[0], y=end[1], footprints=True, color=COLOR.blue, goal=start, filled=True)
    c=agent(mazeWorld, x=start[0], y=start[1], footprints=True, color=COLOR.light, goal=end)

    mazeWorld.tracePath({a:searchPath}, delay=333)
    mazeWorld.tracePath({b:reversedPath}, delay=111)
    mazeWorld.tracePath({c:path}, delay=111)

    l=textLabel(mazeWorld,'Path Length',len(path)+1)    # we add the +1 because 'path' is a 
                                                        # dictionary of the moves done, so  
                                                        # the starting point is not counted
    l=textLabel(mazeWorld,'Search Length',len(searchPath))

    #print(searchPath)
    #print(reversedPath)
    #print(path)

    mazeWorld.run()


# window = Tk()  
# width= window.winfo_screenwidth()               
# height= window.winfo_screenheight()               
# window.geometry("%dx%d" % (width, height))

# button = Button(window,
# 	text = 'aStar',
# 	command = applyAlgorithm)  
# button.pack()  

# window.mainloop()

applyAlgorithm()