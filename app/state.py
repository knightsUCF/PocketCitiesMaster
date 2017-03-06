''' state.py '''

class state():
	def __init__(self, PlayerName,
		           CityName,
		           PlayerCharacter, 
		           PlayerCharacters,
		           StartingCapital, 
		           Capital,
		           Score,
		           Mana,
		           Points,
		           Gold,
		           Health,
		           Map,
		           TileInventor
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
		
		self.InitializeState()
		
		return
	
	def InitializeState(self):
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
	
	def BuildingsIntoTurnCapital(self):
		
	def CalculateCapital(self):
		
		return self.Capital
	
	def UpdateState(self):
		if (BuildingsRevenueCycleTurnCompleted):
			self.BuildingsIntoCapital()
		if (MonopolyRevenueCycleTurnCompleted):
			self.MonopoloyIntoCapital()
		if (BribesRevenueCycleTurnCompleted):
			self.BribesIntoCapital()
		if (PopulationCycleTurnCompleted):
			self.UpdatePopulationGrowthOrDecline()
		if (CivicCycleTurnCompleted):
			self.RunCivicsStats()
			
		
		return
	
	def Run(self):
		''' update the state '''
		self.UpdateState()
		return
