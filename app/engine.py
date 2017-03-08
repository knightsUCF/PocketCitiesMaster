''' engine.py '''
import updatestate
UpdateState.Run()

import log
io = log.log()


class engine():

	def GameLoop(self):
		running = True
		
		while running:

			io.o('Walking down the sidewalk... >>> >>> the main game loop >>> >>>')
			''' time stamp '''
			GameRender.Run()
			GameInput.Run()
			# GameState.Run()
			UpdateState.Run()
			GameSync.Run()

		for event in pygame.event.get():
		    	self.QuitGameRoutine()
		    	running = False
		    	pygame.quit()

	def QuitGameRoutine(self):
		''' Clean up 
            A) Ask player if they are sure they want to quit?
             
		'''
		return

	def Run(self):
		self.GameLoop()
