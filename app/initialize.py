''' initialize.py '''
import window
StartingWindow = window.window()

import grid
InitialGrid = grid.grid()

class initialize():
	def __init__(self):
		''' game initialization state variable data '''

	def Start(self):
		InitialGrid.InitializeGrid()
		StartWindow.InitializeWindow()
