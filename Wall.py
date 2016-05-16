from math import pi


class Wall:
    def __init__(self , cornerList):
        self.cornerList = cornerList
        self.LineList = []
        self.setLine()
    def setLine(self):
        for vex in range(len(self.cornerList)-1):
            self.LineList.append(Line(self.cornerList[vex] , self.cornerList[vex+1])) 


class Line:
    def __init__(self , v1  , v2):
        self.v1 = v1 
        self.v2 = v2
        if v2[0] != v1[0] :
            self.m  = (v2[1]-v1[1]) / (v2[0]-v1[0])
        else:
            self.m = 999
        self.range_min = 0 
        self.range_min_second = 3*pi
        self.range_max = 0 
        self.range_sort = 0 

