from pico2d import *
import math

open_canvas()

# 사진 불러오기
grass = load_image('grass.png')
character = load_image('character.png')

#grass.draw_now(400, 30)
#character.draw_now(400, 90)

#delay(5)

x = 0
y=90

#게임 루프
while (True):
 #게임 렌더링
 clear_canvas_now()
 grass.draw_now(400, 30)
 character.draw_now(x, y)
 #게임 로직(상호작용을 계산하는 것)
 if(x!=770 and y==90):
  x = x + 2 
 elif(x==770 and y!=540):
  y= y+2
 elif(x!=0 and y==540):
  x=x-2
 elif(x==0 and y!=90):
  y=y-2
 delay(0.01)
close_canvas()
