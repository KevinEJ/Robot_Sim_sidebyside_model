#robot
from People import *
from Object import *

class Robot(Object):
    def update(self , T ):
        r_x , r_y = transform(self.Pos_X , self.Pos_Y , self.orien , T.Pos_X , T.Pos_Y) 
        #dis = sqrt(r_x*r_x + r_y*r_y)
        self.move_to(r_x , r_y)
    def move_to(self,x,y):
        dis = sqrt(x*x+y*y)
        if(x>=0):
            if x==0:
                x += 0.1 
            arctan = atan(y/x)
            if(dis > 100):
                self.v = 20
                t = dis / self.v
                self.orien+= 2*arctan/t
            elif(dis > 50):
                self.v = 10
                t = dis / self.v
                self.orien += arctan/t
            elif(dis < 10):
                self.v = 0 
                #t = dis / self.v
                self.orien += arctan
            else:
                self.v = 6 
                t = dis / self.v
                self.orien += arctan/t
        else:
            arctan = -atan(y/x)
            if(dis > 100):
                self.v = 0
                self.orien += arctan
            elif(dis < 10):
                self.v = 0 
                self.orien += arctan
            else:
                self.v = 6 
                self.orien += arctan

    def leftKey(self,event):
        self.orien -= 0.1
    def rightKey(self,event):
        self.orien += 0.1
    def upKey(self,event):
        self.v = 5
    def downKey(self,event):
        self.v = 0 
