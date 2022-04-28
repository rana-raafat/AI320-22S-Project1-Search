from tkinter import *
import tkinter.ttk as ttk
from turtle import color

from pyamaze import *

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
    end = (1, 1)

    if button_id == 'bfsButton':
        searched, reversedPath, path = BFS(mazeWorld, start, end)
        algorithm = 'BFS'
    elif button_id == 'dfsButton':
        searched, reversedPath, path = DFS(mazeWorld, start, end)
        algorithm = 'DFS'
    elif button_id == 'ucsButton':
        searched, reversedPath, path = ucs(mazeWorld, start, end)
        algorithm = 'UCS'
    elif button_id == 'gbfsButton':
        searched, reversedPath, path = GBFS(mazeWorld, start, end)
        algorithm = 'GBFS'       
    elif button_id == 'aStarButton':
        searched, reversedPath, path = aStar(mazeWorld, start, end)
        algorithm = 'A*'       

    l = textLabel(mazeWorld, 'Path Length', len(path)+1)
    # we added the +1 because 'path' is a dictionary
    # of the moves taken from start to goal, so
    # the starting point itself is not counted
    l = textLabel(mazeWorld, 'Search Time', len(searched))

    style = ttk.Style(mazeWorld._win)
    style.theme_use('clam')

    label = Label(text=algorithm)
    label.place(x=mazeWorld._win.winfo_screenwidth() - 800, y=mazeWorld._win.winfo_screenheight() - 100)

    back = ttk.Button(mazeWorld._win, text="Back", command=lambda: MenuWindow(mazeWorld))
    back.place(x=mazeWorld._win.winfo_screenwidth() - 100, y=mazeWorld._win.winfo_screenheight() - 100)

    a = agent(mazeWorld, x=start[0], y=start[1],
                footprints=True, color=COLOR.blue, goal=end)
    b = agent(mazeWorld, x=end[0], y=end[1], 
                footprints=True, color=COLOR.blue, goal=start, filled=True)
    c = agent(mazeWorld, x=start[0], y=start[1],
                footprints=True, color=COLOR.light, goal=end)

    mazeWorld.tracePath({a: searched}, delay=333)
    mazeWorld.tracePath({b: reversedPath}, delay=111)
    mazeWorld.tracePath({c: path}, delay=111)

    mazeWorld.run()



def MenuWindow(mazeWorld=None):
    if(mazeWorld):
        #del mazeWorld
        mazeWorld._win.destroy()
        mazeWorld._tracePathList.clear()

    window = Tk()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    window.geometry("%dx%d" % (screenWidth, screenHeight))
    window.configure(background='#1C1C1C')

    style = ttk.Style(window)
    style.theme_use('clam')

    label = Label(text='Choose an Algorithm to apply on maze')
    label.configure(background='#1C1C1C', font=30, fg='white')
    label.pack(pady=15)

    bfsButton = ttk.Button(window,
                           text='BFS',
                           command=lambda: applyAlgorithm("bfsButton", window))
    bfsButton.pack(pady=15)

    dfsButton = ttk.Button(window,
                           text='DFS',
                           command=lambda: applyAlgorithm("dfsButton", window))
    dfsButton.pack(pady=15)

    ucsButton = ttk.Button(window,
                           text='UCS',
                           command=lambda: applyAlgorithm("ucsButton", window))
    ucsButton.pack(pady=15)

    gbfsButton = ttk.Button(window,
                           text='GBFS',
                           command=lambda: applyAlgorithm("gbfsButton", window))
    gbfsButton.pack(pady=15)

    aStarButton = ttk.Button(window,
                           text='A*',
                           command=lambda: applyAlgorithm("aStarButton", window))
    aStarButton.pack(pady=15)

    window.mainloop()



MenuWindow()
