
from math import *

def transform(s_x,s_y,s_theta,x,y):
    xx = x - s_x 
    yy = y - s_y 
    xxx = xx * cos(-s_theta) - yy*sin(-s_theta)
    yyy = xx * sin(-s_theta) + yy*cos(-s_theta) 
    return xxx,yyy

def re_transform(s_x,s_y,s_theta,x,y):
    xx = x * cos(-s_theta) - y*sin(-s_theta)
    yy = x * sin(-s_theta) + y*cos(-s_theta) 
    xxx = xx - s_x 
    yyy = yy - s_y 
    return xxx,yyy
    
    
class Object:
    def __init__(self):
        self.Pos_X  = 500 
        self.Pos_Y  = 500 
        self.orien  = 0  # in radiens
        self.v      = 0
    def move(self , W):
        sine = sin(self.orien)
        coss = cos(self.orien)
        self.Pos_X += self.v * coss
        self.Pos_Y += self.v * sine
        self.check_collision(W)
        if self.Pos_X > 1000:
            self.Pos_X = 1000
        elif self.Pos_X < 0:
            self.Pos_X = 0 
        
        if self.Pos_Y > 1000:
            self.Pos_Y = 1000
        elif self.Pos_Y < 0:
            self.Pos_Y = 0 

    def check_collision( self , walllist ):
        if self.Pos_X > 100 and self.Pos_X < 400 and self.Pos_Y > 100 and self.Pos_Y < 400:
            a = abs (self.Pos_X - 100)
            b = abs (self.Pos_X - 400)
            c = abs (self.Pos_Y - 100)
            d = abs (self.Pos_Y - 400)
       
            L = [a,b,c,d]
            num = L.index(min(L))
            if num == 0:
                self.Pos_X = 100
            elif num == 1:
                self.Pos_X = 400
            elif num == 2:
                self.Pos_Y = 100
            elif num == 3:
                self.Pos_Y = 400
 
