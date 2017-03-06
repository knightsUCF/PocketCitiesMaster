import state
TileState = state.state()



class tile():
    
    def __init__(self, type, ID, position):
        self.type = type
        self.ID = ID
        self.position = position

    def CreateTileDatabase(self):
        return 
    
    def UpdateTileMap():
        TileState.GetTileTypeAndPosition()
        return 
        
    def UpdateTileState(self):
        self.UpdateTileMap()
        return 
    
    def DrawTiles(self):
        return
    
    def TileLibrary(self):
        return
    
    def GenerateStartingTiles(self):
        return 
    
    def Run(self):
        self.UpdateTileState()
        self.DrawTiles()
        return
        
        
        
    
