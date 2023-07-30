from tkinter import *
import time
import random

tk=Tk()
tk.tittle=('My_game')
tk.resizable(0,0)
canvas=Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()
canvas.update()

class Ball:
    def __init__(self,canvas,paddle, score,color):
        self.canvas=canvas
        self.paddle=paddle
        self.score=score
        self.id=canvas.create_oval(self.id,245,100)
        starts=[-2,-1,1,2] #возможные координаты для старта
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-2
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_buttom=False

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)

