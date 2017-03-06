

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
    
    def OnCreateNewCharacter(self):
        return 
    
    def OnKillCharacter(self):
        return
    
    def OnTradeCharacter(self):
        return 
    
    def OnBuyNewCharacter(self):
        return 
    
    def OnBirthNewCharacter(self):
        return 
    
    def OnPopulationGrowth(self):
        return
    
    def OnBankruptcy(self):
        return 
        
    def Run(self):
        self.OnTileSelect()
        self.OnStartGame()
        self.OnWinGame()
