from sense_hat import SenseHat
import time
import random
sense = SenseHat()
batcolor = (255,255,255)
ballcolor = (0,0,255)
backcolor = (0,0,0)
bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]
lost = False
obat_y=4
t=0.5
shame=False
a=0.1
times_hit=0
#---Functions-------------------
def drawbat():
  sense.set_pixel(0,bat_y,batcolor)
  sense.set_pixel(0,bat_y+1,batcolor)
  sense.set_pixel(0,bat_y-1,batcolor)

def opbat():
  global obat_y
  sense.set_pixel(7,obat_y,batcolor)
  sense.set_pixel(7,obat_y+1,batcolor)
  sense.set_pixel(7,obat_y-1,batcolor)
  if ball_velocity[0]==1:
    if ball_position[1]-obat_y>0 and obat_y<6:
      obat_y += 1
    elif ball_position[1]-obat_y<0 and obat_y>1:
      obat_y -= 1

def drawball():
  global times_hit
  ball_position[0]+=ball_velocity[0]
  ball_position[1]+=ball_velocity[1]
  sense.set_pixel(ball_position[0],ball_position[1],ballcolor)
  if ball_position[0] == 7 or ball_position[0]==0:
    ball_velocity[0] = -ball_velocity[0]
  if ball_position[1] == 7 or ball_position[1]==0:
    ball_velocity[1] = -ball_velocity[1]
  if ball_position[0] == 1 and (bat_y-1)<=ball_position[1]<=(bat_y+1):
    ball_velocity[0] = -ball_velocity[0]
    times_hit+=1
  if ball_position[0] == 6 and (obat_y-1)<=ball_position[1]<=(obat_y+1):
    ball_velocity[0] = -ball_velocity[0]
  if ball_position[0]==0:
    lose()
  if ball_position[0]==7:
    win()
  #if ball_position[0]==1:
    #if ball_position[1]- bat_y==2 or ball_position[1]- bat_y== -2:
      #ball_velocity[0]*=-1
      #ball_velocity[0]*=-1
  #if ball_position[0]==6:
    #if ball_position[1]-obat_y==2 or ball_position[1]-obat_y== -2:
      #ball_velocity[0]*=-1
      #ball_velocity[0]*=-1
  
def win():
  global lost
  lost = True

def lose():
  global lost
  global shame
  lost = True
  shame = True

def move_up(event):
  global bat_y
  if event.action == "pressed" and bat_y>1:
    bat_y-=1

def move_down(event):
  global bat_y
  if event.action == "pressed" and bat_y<6:
    bat_y+=1

#---------------------------------
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

while True:
  bat_y = 4
  obay_y =4
  t=0.5
  a=0.1
  lost = False
  ball_position = [random.randint(2,5), random.randint(1,5)]
  ball_velocity = [1, 1]
  shame=False
  while not lost:
    sense.clear(backcolor)
    drawbat()
    opbat()
    drawball()
    time.sleep(t)
    a/=1.5
    t-=a
  time.sleep(2)
  for x in range(25):
    sense.clear(0,0,0)
    sense.set_pixel(ball_position[0],ball_position[1],(255,255,255))
    time.sleep(0.001)
    sense.clear(255,255,255)
    sense.set_pixel(ball_position[0],ball_position[1],(0,0,0))
    time.sleep(0.001)
  if shame:    
    sense.show_message("You Lost: "+str(times_hit))
  else:
    sense.show_message("You Won: "+str(times_hit))
