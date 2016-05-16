from math import *

def init_canvas( Mgr , canvas):
    for line_num in Mgr.W.WallList:
        canvas.create_polygon(line_num.cornerList)

def display_Laset (Mgr , canvas):
    #print len(Mgr.W.WallList[0].LineList)
    #print len(Mgr.Laser)
    for Data in Mgr.Laser:
        canvas.create_line([Data.x , Data.y] , [Mgr.P.Pos_X , Mgr.P.Pos_Y] )


def update_canvas( Mgr , canvas):
        p_sine = sin(Mgr.P.orien)
        p_coss = cos(Mgr.P.orien)
        pv_x = 15 * p_coss
        pv_y = 15 * p_sine
        r_sine = sin(Mgr.R.orien)
        r_coss = cos(Mgr.R.orien)
        rv_x = 15 * r_coss
        rv_y = 15 * r_sine
        canvas.delete("all") 
        init_canvas( Mgr , canvas)
        display_Laset (Mgr , canvas)
        canvas.create_oval(Mgr.P.Pos_X-10, Mgr.P.Pos_Y-10, Mgr.P.Pos_X + 10 , Mgr.P.Pos_Y+10, fill="blue")
        canvas.create_oval(Mgr.P.Pos_X+pv_x-5, Mgr.P.Pos_Y+pv_y-5, Mgr.P.Pos_X +pv_x+ 5 , Mgr.P.Pos_Y+ pv_y+5, fill="blue")
        canvas.create_oval(Mgr.R.Pos_X-10, Mgr.R.Pos_Y-10, Mgr.R.Pos_X + 10 , Mgr.R.Pos_Y+10, fill="red")
        canvas.create_oval(Mgr.R.Pos_X+rv_x-5, Mgr.R.Pos_Y+rv_y-5, Mgr.R.Pos_X +rv_x+ 5 , Mgr.R.Pos_Y+ rv_y+5, fill="red")
        canvas.create_oval(Mgr.T.Pos_X-5, Mgr.T.Pos_Y-5, Mgr.T.Pos_X+ 5 , Mgr.T.Pos_Y+5, fill="red")
        
