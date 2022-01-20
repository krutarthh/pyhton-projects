from tkinter import *
from pygame import mixer
import os
def playsong():
    activesong=musiclist.get(ACTIVE)
    print(activesong)
    mixer.music.load(activesong)
    mixer.music.play()
def pausesong():
    mixer.music.pause()
def resumesong():
    mixer.music.unpause()
def stopsong():
    mixer.music.stop()

root=Tk()
root.title("music player")
mixer.init()
musiclist=Listbox(root,selectmode=SINGLE,bg="white")
musiclist.grid(columnspan=5)
os.chdir=('')
song1=os.listdir()
for p in song1:
    musiclist.insert(END,p)

Button(root,text= 'play', command = playsong).grid(row =1 , column = 0)
Button(root,text= 'pause', command = pausesong).grid(row =1 , column = 1)
Button(root,text= 'stop', command = stopsong).grid(row =1 , column = 2)
Button(root,text= 'resume', command = resumesong).grid(row =1 , column = 3)
mainloop()


