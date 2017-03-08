# START at Run()
# Here we are going to import state, where we actually keep all the data

import state
WhatIsState = state.state()

# to get values we are going to get them through methods 
 
# to get input and use to update state

import processinputintogamelogic # this contains the button class, also gets input through linking the button class
ObjectProcessInputIntoGameLogic = processinputintogamelogic.processinputintogamelogic()

class updatestate():
    def UpdateAllStates(self):
         # do all the updating
         return
    
    def Run(self):
        UpdateAllStates()
        
       
       
# to get values we are going to get them through methods
# Here are all the methods to access player metrics
# The methods below live in state

'''

def GetInitialGold(self):
    return self.InitialGold
def GetInitialScore(self):
		  return self.InitialScore
def GetCurrentGold(self):
		  return

'''
