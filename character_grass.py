from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

count =0

while(True):
 x = 2
 y = 90
 while (count!=1):

  clear_canvas_now()
  grass.draw_now(400, 30)
  character.draw_now(x, y)
  if(x!=770 and y==90):
   x = x + 2 
  elif(x==770 and y!=540):
   y= y+2
  elif(x!=0 and y==540):
   x=x-2
  elif(x==0 and y!=90):
   y=y-2
   if(y==90):
    count = 1
  delay(0.01)
 count = count+1

 x2 = 400
 y2 = 300
 a = 90
 r = 150
 
 #게임 루프
 while (count!=0):

  x2=r*math.cos(math.radians(a))+400
  y2=r*math.sin(math.radians(a))+300
  a=a-5
  delay(0.1)
  clear_canvas_now()
  grass.draw_now(400, 30)
  character.draw_now(x2, y2)
  if(a==-270):
    count = 0
close_canvas()
