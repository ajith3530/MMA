import random
import win32api

x_limit=500
y_limit=500

def movemouse():
	set_x_pos=random.randint(0,x_limit)
	set_y_pos=random.randint(0,y_limit)
	win32api.SetCursorPos((set_x_pos,set_y_pos))


movemouse()
