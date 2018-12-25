from Tkinter import *


def callbackKey(event):
    k=event.keysym.lower()
    if k=='up':
        print 'up start'
        print 'up on'
    if k=='down':
        print 'down start'
        print 'down on'
    
    
def callbackKeyr(event):
    k=event.keysym.lower()
    if k=='up':
        print 'up end'
    if k=='down':
        print 'down end'
    
                

root=Tk()
root.bind("<Key-Up>", callbackKey)
root.bind("<KeyRelease-Up>",callbackKeyr)
root.bind("<KeyPress-Down>", callbackKey)
root.bind("<KeyRelease-Down>",callbackKeyr)




root.mainloop()
