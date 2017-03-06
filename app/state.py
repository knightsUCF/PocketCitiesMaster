''' state.py '''

import tilemgr
TileManager = tilemgr.tilemgr()

class state():
	def __init__(self, PlayerName,
		           CityName,
		           PlayerCharacter, 
		           PlayerCharacters,
		           Level,
		           StartingCapital, 
		           Capital,
		           Score,
		           Mana,
		           Points,
		           Gold,
		           Health,
		           Map,
		           TileInventor,
		           Apartments,
		           Houses,
		           Hotels,
		           Buisnesses,
		           Stores
		    ):
		
		''' initialize state data '''
		self.PlayerName = PlayerName
		self.CityName = CityName
		self.PlayerCharacter = PlayerCharacter
		self.PlayerCharacters = PlayerCharacters
		self.Level = Level
		self.StartingCapital = StartingCapital
		self.Capital = Capital
		self.Score = Score
		self.Mana = Mana
		self.Points = Points
		self.Gold = Gold
		self.Health = Health
		self.Map = Map
		self.TileInventory = TileInventory
		
		self.Apartments = Apartments
		self.Houses = Houses
		self.Hotels = Hotels
		self.Motels = Motels
		self.Buisnesses = Buisnesses
		self.Stores = Stores
		
		self.PlayerName = "Bob"
		self.CityName = "San Francisco"
		self.PlayerCharacter = "Entrepreneur"
		self.PlayerCharacters = { 1 : Entrepreneur, 2 : Cook }
		self.Level = 1
		self.StartingCapital = 100000
		self.Capital = self.StartingCapital
		self.Score = 0
		self.Mana = 0
		self.Points = 0
		self.Health = 100
		''' self.map '''
		''' self.TileInventory '''
		return
	
	def BuildingsIntoCapital(self):
		''' A thousand dollars per building per turn ''' 
		self.Capital = self.Buildings * 1000 
		
	def MonopoloyIntoCapital(self):
		''' check for proximity '''
		return
	
	def CompetitionIntoCapital(self):
		''' check for competition proximity and subtract capital '''
		return 
		
	def BribesIntoCapital(self):
		return
		
	def UpdatePopulationGrowth(self):
		return
		
	def RunCivicsStats(self):
		return
		
	def CalculateCapital(self):
		return
	
	def UpdateState(self):
		if (BuildingsRevenueCycleTurnCompleted):
			self.BuildingsIntoCapital()
		if (MonopolyRevenueCycleTurnCompleted):
			self.MonopoloyIntoCapital()
		if (CompetitionRevenueCycleTurnCompleted):
			self.CompetitionIntoCapital()
		if (BribesRevenueCycleTurnCompleted):
			self.BribesIntoCapital()
		if (PopulationCycleTurnCompleted):
			self.UpdatePopulationGrowth()
		if (CivicCycleTurnCompleted):
			self.RunCivicsStats()
		''' TileManager.Run(UpdateThisState) '''
			
        def GetTileTypeAndPosition(self):
		return 
	
	def Run(self):
		''' update the state '''
		self.UpdateState()
		return
