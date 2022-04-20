from tkinter import *
import tkinter.ttk as ttk
from turtle import color 

from pyamaze import maze, agent, COLOR, textLabel

from BFS import BFS
from DFS import DFS
from UCS import ucs
from aStar import aStar
from GBFS import GBFS



def applyAlgorithm(button_id, buttonsWindow):  
    buttonsWindow.destroy()

    mazeWorld = maze()
    mazeWorld.CreateMaze(loadMaze='maze.csv')
    
    start = (mazeWorld.rows, mazeWorld.cols)
    #start = (6,1)
    end = (1,1)

    if button_id == 'bfsButton':
        searchPath, reversedPath, path = BFS(mazeWorld, start, end)
    elif button_id == 'dfsButton':
        searchPath, reversedPath, path = DFS(mazeWorld, start, end)
    elif button_id == 'ucsButton':
        searchPath, reversedPath, path = ucs(mazeWorld, start, end)
    elif button_id == 'gbfsButton': 
        searchPath, reversedPath, path = GBFS(mazeWorld, start, end)
    elif button_id == 'aStarButton':
        searchPath, reversedPath, path = aStar(mazeWorld, start, end)

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


window = Tk()  
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("%dx%d" % (width, height))
window.configure(background='#111')

style = ttk.Style(window)
style.theme_use('clam')

label=Label(text='Choose an Algorithm to apply on maze')
label.configure(background='#111', font=30, fg='white')
label.pack(pady=15)  

bfsButton = ttk.Button(window,
	text = 'BFS',
	command=lambda: applyAlgorithm("bfsButton", window) )
bfsButton.pack(pady=15)  

bfsButton = ttk.Button(window,
	text = 'DFS',
	command=lambda: applyAlgorithm("dfsButton", window) )
bfsButton.pack(pady=15)  

bfsButton = ttk.Button(window,
	text = 'UCS',
	command=lambda: applyAlgorithm("ucsButton", window) )
bfsButton.pack(pady=15)  

bfsButton = ttk.Button(window,
	text = 'GBFS',
	command=lambda: applyAlgorithm("gbfsButton", window) )
bfsButton.pack(pady=15)  

bfsButton = ttk.Button(window,
	text = 'A*',
	command=lambda: applyAlgorithm("aStarButton", window) )
bfsButton.pack(pady=15)  

window.mainloop()

#applyAlgorithm()