''' pocketcities.py '''

import initialize
NewGame = initialize.initialize()

import engine
RunGameEngine = engine.engine()

import log
io = log.log()


NewGame.Start()
RunGameEngine.Run()
