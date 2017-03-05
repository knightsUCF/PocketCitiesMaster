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
		self.StartingCapital = StartingCapital
		self.Capital = Capital
		self.Score = Score
		self.Mana = Mana
		self.Points = Points
		self.Gold = Gold
		self.Health = Health
		self.Map = Map
		self.TileInventory = TileInventory
		
		return
	
	def UpdateState(self):
		return
	
	def Run(self):
		''' update the state '''
		self.UpdateState()
		return
