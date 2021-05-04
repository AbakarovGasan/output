import win32api, win32con, time
def click(x,y, r=1,v=1):
#X ,Y 
    win32api.SetCursorPos((x,y))
    time.sleep(r)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(v)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

for i in range(2000000000):click( 96 , 59 ,0.03,0.005)
