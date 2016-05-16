from Wall import *
         
class WallMgr:
    def __init__(self):
        self.WallList = [] 
        self.addWall([ [100,100], [400,100] , [400,400], [100,400] , [100,100] ])
        self.addWall([ [600,600], [900,600] , [900,900], [600,900] , [600,600] ])
        self.addWall([ [100,600], [400,600] , [400,900], [100,900] , [100,600] ])
        self.addWall([ [600,100], [900,100] , [900,400], [600,400] , [600,100] ])
    def addWall(self , cornerList):
        wall = Wall(cornerList)
        self.WallList.append(wall)
        
