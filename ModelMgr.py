from math import *

from People import *
from Robot  import *
from Target  import *
from WallMgr import *
from Data import *
import pdb

class ModelMgr:
    def __init__ (self):
        self.P = People()
        self.R = Robot()
        self.T = Target()
        self.W = WallMgr()
        self.Laser = [ Data(0,0,10000) ] * 360
    def update(self):
        self.getLaser()
        self.P.move(self.W)
        self.T.update(self.P , self.R , self.W)
        self.T.move(self.W)
        self.R.update(self.T )
        self.R.move(self.W)
    def getLaser(self):
        # search all lines
        self.set_range()
        minList , maxList = self.dup_and_sorting()
        minCount = 0 
        maxCount = 0 
        Current_lines = []
        #print (minList)
        #print (maxList)
        #pdb.set_trace()
        for degree in range(-90,270):
            #pdb.set_trace()
            if minCount != len(minList):
                while pi/180*degree > minList[minCount][1]:
                    Current_lines.append(minList[minCount][0])
                    minCount += 1
                    if minCount == len(minList):
                        break
            if maxCount != len(maxList):
                while pi/180*degree > maxList[maxCount][1] :
                    Current_lines.remove(maxList[maxCount][0])
                    maxCount += 1
                    if maxCount == len(maxList):
                        break
            min_dis = Data( 10000*cos(pi/180*degree) , 10000 * sin(pi/180*degree),1000000)
            #min_dis = Data( 0 , 0),1000000)
            #print "===================================================="
            #print "minCount " , minCount 
            #print "maxCount " , maxCount
            #print "current degree and next degree " ,  degree , " , " , minList[minCount][1]*pi/180
            #print "cur List.len  " , len(Current_lines)
            for lines in Current_lines:
                data = self.compute_distance(lines , pi/180*degree)
                if data.d < min_dis.d :
                    min_dis = data
            #print len(Current_lines)
            self.Laser[degree+90] = min_dis
        #print minCount
        #print maxCount


    def set_range(self):
        curX , curY = self.P.Pos_X , self.P.Pos_Y
        for Walls in self.W.WallList:
            for Lines in Walls.LineList :
                r1x , r1y = Lines.v1[0] -  curX , Lines.v1[1] - curY 
                # degree - 90 ~ 270 
                if r1x >= 0 :
                    theta_1 = atan(r1y / (r1x+0.0001))
                else:
                    theta_1 = atan(r1y / (r1x+0.0001)) + pi
                r2x , r2y = Lines.v2[0] -  curX , Lines.v2[1] - curY 
                if r2x >= 0 :
                    theta_2 = atan(r2y / (r2x+0.0001))
                else:
                    theta_2 = atan(r2y / (r2x+0.0001)) + pi
                if theta_2 > theta_1 :
                    if theta_2 - theta_1 < pi: 
                        Lines.range_min = theta_1
                        Lines.range_max = theta_2
                        Lines.range_min_second = 2*pi 
                    else:
                        Lines.range_min = theta_2 - 2*pi
                        Lines.range_min_second = theta_2 
                        Lines.range_max = theta_1
                else:    
                    if theta_1 - theta_2 < pi: 
                        Lines.range_min = theta_2
                        Lines.range_max = theta_1
                        Lines.range_min_second = 2*pi 
                    else:
                        Lines.range_min = theta_1 - 2*pi
                        Lines.range_min_second = theta_1
                        Lines.range_max = theta_2
    def dup_and_sorting(self):
        Min_List = []
        Max_List = []
        for Walls in self.W.WallList:
            for Lines in Walls.LineList :
                Min_List.append([Lines , Lines.range_min] )
                Min_List.append([Lines , Lines.range_min_second] )
                Max_List.append([Lines , Lines.range_max] )
        Sorted_min_List  = sorted(Min_List , key=lambda line: line[1])
        Sorted_max_List  = sorted(Max_List , key=lambda line: line[1])
        #Sorted_max_List  = sorted(Max_List)
        return Sorted_min_List , Sorted_max_List

    def compute_distance(self , Lines , degree):
        # y = mx + b
        curX , curY = self.P.Pos_X , self.P.Pos_Y
        r1x , r1y = Lines.v1[0] -  curX , Lines.v1[1] - curY 
        #r2x , r2y = Lines.v2[0] -  curX , Lines.v2[1] - curY 
        
        x = (-r1y + Lines.m*r1x) / (Lines.m - tan(degree) + 0.0001)
        y = tan(degree) * x

        g_x = x + curX 
        g_y = y + curY
        distance = sqrt(x*x+y*y)
        data = Data(g_x , g_y , distance)
        return data

