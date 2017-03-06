import draw
DrawGrid = draw.draw()

class grid():
    def __init__(self, StartingGridSize, VerticalNumberOfLines, HorizontalNumberOfLines, HideGrid):
        self.StartingGridSize = StartingGridSize
        self.VerticalNumberOfLines = VerticalNumberOfLines
        self.HorizontalNumberOfLines = HorizontalNumberOfLines
        self.HideGrid = HideGrid
        return
    
    def DrawVerticalLine(self):
        return 
    
    def DrawHorizontalLine(self):
        return 
    
    def DrawAGrid(self, width, height):
        DrawGrid.FromDrawModuleDrawGrid(widgth, height)
        
    def StartDrawingRow(self):
        return
        
    def StartDrawingColumn(self):
        return 
    
    def EndDrawingRow(self):
        return 
    
    def EndDrawingColumn(self):
        return 
    
    def TurnOffGrid(self):
        return self.HideGrid = true
    
    
    
    
    def CreateAGrid(self, width, height):
        # width and height are in boxes
        self.DrawGrid(width, height)
        return 
    
    
        
      
