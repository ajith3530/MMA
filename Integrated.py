import win32api
import threading
import time
import random

x_limit=500
y_limit=500
stop_flag= False

def movemouse():
	set_x_pos=random.randint(0,x_limit)
	set_y_pos=random.randint(0,y_limit)
	win32api.SetCursorPos((set_x_pos,set_y_pos))

def application():
	prev_pos=win32api.GetCursorPos()
	time.sleep(5)
	cur_pos =win32api.GetCursorPos()
	if(prev_pos==cur_pos ):
		movemouse()
	else:
		print("Move position changed")

def identify_click():
	while(win32api.GetKeyState(0x20)==0):
		timer_100ms=threading.Timer(0.10,identify_click)	
		#print("Waiting for Spacebar")
		time.sleep(.15)
		application()
		#print("Spacebar Status=%d" %(win32api.GetKeyState(0x20)))
		#print("Not Entered While Case")
		#while(timer_100ms.is_alive()):
		print("Waiting for Timer")


identify_click()