from Tkinter import *
from math import *
from Object import *

class People(Object):
    '''
    def __init__(self):
        self.Pos_X  = 500 
        self.Pos_Y  = 500 
        self.orien  = 0  # in radiens
        self.v      = 0
    '''
    def leftKey(self,event):
        self.orien -= 0.1
    def rightKey(self,event):
        self.orien += 0.1
    def upKey(self,event):
        self.v = 5
    def downKey(self,event):
        self.v = 0 

