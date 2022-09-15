import tkinter as tk
import random
import keyboard
import time
from PIL import Image, ImageTk
import playsound 


def make_mouse():
    global x_mouse,y_mouse,mouse

    x_mouse = random.randrange(18,1270,50)
    y_mouse = random.randrange(7,620,50)
    canvas.delete(mouse)  
    canvas.config(bg="DarkOliveGreen1")
    mouse = canvas.create_rectangle(x_mouse,y_mouse,x_mouse+50,y_mouse+50,fill='purple')

def make_snake():
    global x_snake

    for i in range(3):
        x_snake+=50
        listsq.append(canvas.create_rectangle(x_snake,y_snake,x_snake+50,y_snake+50,fill='orange'))

def crash():
    global x_snake,y_snake

    for i in range(0,len(listpos)-1):
        if (x_snake+25) in range(listpos[i][0],listpos[i][0]+51) and (y_snake+25) in range(listpos[i][1],listpos[i][1]+51):
            canvas.delete("all")
            playsound('8bit.mp3')
            img = ImageTk.PhotoImage(Image.open("1.png").resize((1536,864)))  
            canvas.create_image(752, 400, image=img)
            canvas.update()
            time.sleep(5)
            root.destroy() 
            break
            
def screenEnd():
    global mouse,x_snake,y_snake

    x_snake = 1468 if x_snake<18 else x_snake
    x_snake = 18 if x_snake>1468 else x_snake
    y_snake = 807 if y_snake<7 else y_snake
    y_snake = 7 if y_snake>807 else y_snake

    update(x_snake,y_snake)

def update(x1,y1):
    global x_mouse,y_mouse,x_snake,y_snake

    listpos.append([x_snake,y_snake])

    if (x1+25) in range(x_mouse,x_mouse+51) and (y1+25) in range(y_mouse,y_mouse+51):        
            listsq.append(canvas.create_rectangle(x1,y1,x1+50,y1+50,fill='black'))
            make_mouse()
    else:
        canvas.delete(listsq[0])
        listsq.pop(0)
        listsq.append(canvas.create_rectangle(x1,y1,x1+50,y1+50,fill='black'))
        listpos.pop(0)

    crash()

def leftcheck():
    global x_snake,y_snake,direction

    if keyboard.is_pressed('left'):
        x_snake-=50
        direction='left'

    elif direction=='left':
        x_snake-=50
        direction='left'

def rightcheck():
    global x_snake,y_snake,direction

    if keyboard.is_pressed('right'):
        x_snake+=50
        direction='right'
    
    elif direction=='right':
        x_snake+=50
        direction='right'

def upcheck():
    global x_snake,y_snake,direction

    if keyboard.is_pressed('up'):
        y_snake-=50
        direction='up'

    elif direction=='up':
        y_snake-=50
        direction='up'

def downcheck():
    global x_snake,y_snake,direction

    if keyboard.is_pressed('down'):
        y_snake+=50
        direction='down'

    elif direction=='down':
        y_snake+=50
        direction='down'

def structure():
    global direction

    if keyboard.is_pressed('esc'):
        img = ImageTk.PhotoImage(Image.open("1.png").resize((1536,864)))  
        canvas.create_image(752, 400, image=img)
        canvas.update()
        time.sleep(2)
        root.destroy()

    if direction=='up':
        leftcheck()
        rightcheck()
        upcheck()

    elif direction=='down':
        leftcheck()
        rightcheck()
        downcheck()

    elif direction=='left':
        upcheck()
        downcheck()
        leftcheck()

    elif direction=='right':
        upcheck()
        downcheck()
        rightcheck()
    
    screenEnd()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1300x650")
    root.resizable(0,0)

    # root.attributes("-fullscreen",True)
    canvas = tk.Canvas(root,width=1290,height=640)
    canvas.pack()
    x_mouse = random.randrange(18,1290)
    y_mouse = random.randrange(7,640,50)    
    mouse=canvas.create_rectangle(x_mouse,y_mouse,x_mouse+50,y_mouse+50)
    x_snake = random.randrange(18,1290,50)
    y_snake = random.randrange(7,640,50)
    direction='right'
    listsq = []
    listpos = []
    listpos.append([x_snake,y_snake])
    make_mouse()
    make_snake()
    while(True):
        structure()
        canvas.update()
        time.sleep(0.05)
    root.mainloop()