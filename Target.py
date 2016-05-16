from Object import *


class Target(Object):
    def update(self ,  P , R , W):
        r_x , r_y , r_vx , r_vy , r_o = self.get_related_parameter(P,R)
        d = 100 
        goal_l_x = r_x + d * sin(r_o)
        goal_l_y = r_y - d * cos(r_o)
        goal_r_x = r_x - d * sin(r_o)
        goal_r_y = r_y + d * cos(r_o)
       
        goal_x = goal_l_x 
        goal_y = goal_l_y 

        self.Pos_X , self.Pos_Y = re_transform(-R.Pos_X , -R.Pos_Y , -R.orien , goal_x ,goal_y)

    def get_related_parameter(self , P , R):
        r_x , r_y = transform(R.Pos_X , R.Pos_Y , R.orien , P.Pos_X , P.Pos_Y)
        pv_y , pv_x = P.v * sin(P.orien) , P.v *  cos(P.orien)
        r_vx , r_vy = transform(0 ,0 , self.orien , pv_x , pv_y)
        r_o = P.orien - R.orien
        return r_x , r_y , r_vx , r_vy , r_o


