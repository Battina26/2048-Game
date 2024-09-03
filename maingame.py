from tkinter import *
from PIL import ImageTk,Image
import game
import pygame


def start(root,my_canvas):
    
    #To create buttons and its functionality
    button1 = Button(root,image = play_button,borderwidth=0,highlightthickness=0,command = lambda : change(root))
    button2 = Button(root,image = exit_button,borderwidth=0,highlightthickness=0,command = lambda : change_exit(root))
    button3 = Button(root,image = help_button,borderwidth=0,highlightthickness=0,command = lambda : instruct( ))
    button4 = Button(root,image = mute_button,borderwidth=0,highlightthickness=0,command = lambda : mute(root))
    
    #To fix the place of the buttons on the tkinter window
    button1_window = my_canvas.create_window(0,30,anchor="nw",window=button1)
    button2_window = my_canvas.create_window(0,500,anchor="nw",window=button2)
    button3_window = my_canvas.create_window(1190,20,anchor="nw",window=button3)
    button4_window = my_canvas.create_window(1195,500,anchor="nw",window=button4)


def change_exit(root):
    exit(0)
    #root.destroy()

def change(root):
    root.destroy()

def instruct():
    root1 = Toplevel()
    root1.title("Instructions")
    root1.geometry('1004x565')
    
    bg = ImageTk.PhotoImage(file="instructions.png")

    my_canvas = Canvas(root1,width=1004,height=565,highlightthickness=0)
    my_canvas.pack(fill="both",expand=True)
    my_canvas.create_image(0,0,image=bg,anchor="nw")

    root1.mainloop()

is_muted = False

def mute(root):
    global is_muted
    is_muted = not is_muted
    toggle_sound(is_muted)


def toggle_sound(mute):
    pygame.mixer.init()
    if pygame.mixer.music.get_volume() > 0 and mute:
        pygame.mixer.music.set_volume(0)
    else:
        pygame.mixer.music.set_volume(1)


def call():
    global my_canvas,play_button,exit_button,help_button,mute_button
    root = Tk()
    #root.bind('<Configure>',resizer)
    #To get a tkinter window as my fullscreen
    root.attributes("-fullscreen",True)
    root.title('Game')
    #root.geometry('900x1000')
    
    #to add background to my tkinter window
    bg = ImageTk.PhotoImage(file="idex2.png")
   
    my_canvas = Canvas(root,width=540,height=684,highlightthickness=0)
    my_canvas.pack(fill="both",expand=True)
    my_canvas.create_image(0,0,image=bg,anchor="nw")

 
    play_button = PhotoImage(file ='play.png')
    exit_button = PhotoImage(file = 'exit.png')
    help_button = PhotoImage(file = 'help.png')
    mute_button = PhotoImage(file = 'mute.png')


    img_label = Label(image = play_button)
    img_label1 = Label(image = exit_button)
    img_label2 = Label(image = help_button)
    img_label3 = Label(image = mute_button)
    #img_label.pack(pady=20)
   
    start(root,my_canvas)

    root.mainloop()

while(True):
    call()
    game.main()
