from Tkinter import *
import time

from update import *
from ModelMgr import *
main = Tk()
Mgr = ModelMgr()

time1 = ''
clock = Label(main, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)

canvas = Canvas(main , width = 1000 , height = 1000)
canvas.pack()

main.bind('<Left>', Mgr.P.leftKey)
main.bind('<Right>', Mgr.P.rightKey)
main.bind('<Up>', Mgr.P.upKey)
main.bind('<Down>', Mgr.P.downKey)
'''
main.bind('<A>', R.leftKey)
main.bind('<D>', R.rightKey)
main.bind('<W>', R.upKey)
main.bind('<S>', R.downKey)
'''

init_canvas( Mgr , canvas)

def update_clock():
    now = time.strftime("%H:%M:%S")
    clock.configure(text=now)
    Mgr.update()
    update_canvas(Mgr,canvas)
    main.after(100, update_clock)

update_clock()

main.mainloop()




