

class event():
    
    def OnTileSelect(self):
        ''' Show graphic and play sound ''' 
        return 
    
    def OnStartGame(self):
        ''' Play intro song, roll credits '''
        return 
        
    def OnWinGame(self):
        ''' Show You Won Congratulations screen '''
        return 
        
    def Run(self):
        self.OnTileSelect()
        self.OnStartGame()
        self.OnWinGame()
