''' render.py '''

import state
GameStateInformation = state.state()

import draw
DrawTheNewRender = draw.draw()


class render():
	def __init__(self):
		''' initialize state '''
		return
	
	def UpdateRender():
		GameStateInformation.Run()
		DrawTheNewRender.Run()

	def Run(self):
		self.UpdateRender()

	def DisplayInitialState(self):
		''' run this outside of game loop 
		    example: GameRender.Initialize
		'''
		return 

