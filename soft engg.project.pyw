from tkinter import *
import time
import random

tk=Tk()
tk.title("amit")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.config(bg="black")
canvas.pack()
tk.update()
canvas.create_line(250,0,250,400,fill="orange")
counter=0
counter1=0

class Ball:  
     def __init__(self,canvas,color,paddle,paddle1):
          self.canvas=canvas
          self.paddle=paddle
          self.paddle1=paddle1
          canvas.create_text(125,130,text="player 2",font=('arial',30),fill="purple")
          canvas.create_text(355,130,text="player 1",font=('arial',30),fill="purple")
          canvas.create_text(125,350,text="created by:",font=('arial',15),fill="white")
          canvas.create_text(235,375,text="Amit,Ayush,Hardik ,himanshu",font=('arial',10),fill="silver")
          
          self.id=canvas.create_oval(10,10,25,25,fill=color)
          self.canvas.move(self.id,235,260)
          start=[-3,3]
          random.shuffle(start)
          self.x=start[0]
          self.y=-3
          self.canvas_height=self.canvas.winfo_height() 
          self.canvas_width=500
         
          
     def draw(self):
          """canvas.create_text(125,130,text="player 2",font=('arial',30),fill="purple")
          canvas.create_text(355,130,text="player 1",font=('arial',30),fill="purple")
          canvas.create_text(125,350,text="created by:",font=('arial',15),fill="white")
          canvas.create_text(235,375,text="Amit,Ayush,Hardik",font=('arial',10),fill="silver")"""
          self.canvas.move(self.id,self.x,self.y)
          pos=self.canvas.coords(self.id)
          if pos[1]<=0:
               self.y=3
          if pos[3]>=self.canvas_height:
               self.y=-3
          if pos[0]<=0:
               self.x=3
               self.score(True)
          if pos[2]>=self.canvas_width:
               self.x=-3
               self.score(False)
          if self.hit_paddle(pos)==True:
               self.x=3
          if self.hit_paddle1(pos)==True:
               self.x=-3

     def score(self,val):
          global counter
          global counter1
          if val==True:
               a=self.canvas.create_text(125,40,text=counter,font=("arial",60),fill="white")
               canvas.itemconfig(a,fill="black")
               counter+=1
               a=self.canvas.create_text(125,40,text=counter,font=("arial",60),fill="white")

          if val== False:
               a=self.canvas.create_text(375,40,text=counter1,font=("arial",60),fill="white")
               canvas.itemconfig(a,fill="black")
               counter1+=1
               a=self.canvas.create_text(375,40,text=counter1,font=("arial",60),fill="white")
                                                                  

     def hit_paddle(self,pos):
          paddle_pos=self.canvas.coords(self.paddle.id)
          if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
               if pos[0]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                    return True
               return False

     def hit_paddle1(self,pos): 
          paddle_pos=self.canvas.coords(self.paddle1.id)
          if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
               if pos[2]>=paddle_pos[0] and pos[2]<=paddle_pos[2]:
                    return True
               return False
class Paddle:
     def __init__(self,canvas,color):
          self.canvas=canvas
          self.id=canvas.create_rectangle(0,150,30,250,fill=color)
          self.y=0
          self.canvas_height=self.canvas.winfo_height()
          self.canvas_width=self.canvas.winfo_width()
          self.canvas.bind_all("w",self.turn_left)
          self.canvas.bind_all("s",self.turn_right)
          
     def draw(self):
          self.canvas.move(self.id,0,self.y)
          pos=self.canvas.coords(self.id)
          if pos[1]<=0:
               self.y=0
          if pos[3]>=400:
               self.y=0

     def turn_left(self,evt):
          self.y=-3
          
     def turn_right(self,evt):
          self.y=3


          
class Paddle1:
     def __init__(self,canvas,color):
          self.canvas=canvas
          self.id=canvas.create_rectangle(470,150,500,249,fill=color)
          self.y=0
          self.canvas_height=self.canvas.winfo_height()
          self.canvas_width=self.canvas.winfo_width()
          self.canvas.bind_all("<KeyPress-Down>",self.turn_left)
          self.canvas.bind_all('<KeyPress-Up>',self.turn_right)
          
     def draw(self):
          self.canvas.move(self.id,0,self.y)
          pos=self.canvas.coords(self.id)
          if pos[1]<=0:
               self.y=0
          if pos[3]>=300:
               self.y=0
     def turn_left(self,evt):
          self.y=3
          
     def turn_right(self,evt):
          self.y=-3

          
paddle=Paddle(canvas,"silver")
paddle1=Paddle1(canvas,"red")
          
ball=Ball(canvas,"gold",paddle,paddle1)

 


while 1: 
     ball.draw()
     paddle.draw()
     paddle1.draw()
      
     if counter==10:
          ball.x=0
          ball.y=0
          paddle.y=0
          paddle1.y=0
          canvas.create_text(250,200,text="congrats player 1! you won!",font=60,fill="aqua")
          canvas.create_text(250,230,text='score:'+str(counter)+"-"+str(counter1),font=32,fill="red")
               
     if counter1==10:
          ball.x=0
          ball.y=0
          paddle.y=0
          paddle1.y=0
          canvas.create_text(250,200,text="congrats player 2! you won!",font=60,fill="aqua")
          canvas.create_text(250,230,text='score:'+str(counter)+"-"+str(counter1),font=32,fill="red")

     tk.update_idletasks()
     tk.update()
     time.sleep(0.00001)
     if counter==10 or counter1==10:
          time.sleep(10000)
