import win32api
import threading
import time

stop_flag= False

def identify_click():
    if(win32api.GetKeyState(0x20)!=0):
    	print(win32api.GetKeyState(0x20))
    	stop_flag=True
    else:
    	stop_flag=False

while(win32api.GetKeyState(0x20)==0):
	n=None
	timer_100ms=threading.Timer(0.10,identify_click)	
	#print("Waiting for Spacebar")
	time.sleep(.15)
	#print("Spacebar Status=%d" %(win32api.GetKeyState(0x20)))
	#print("Not Entered While Case")
	#while(timer_100ms.is_alive()):
	#	print("Waiting for Timer")

#print("Spacebar input received")