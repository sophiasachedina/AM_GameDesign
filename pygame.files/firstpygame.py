
#SophiaSachedina
#6/9/2022
#pygame basic functions
#creating screens, colors, shapes

from cv2 import insertChannel, sqrt
import pygame, time
pygame.init() #initialize the pygame package

#perimeter
WIDTH=700 #llike a constant, 700 is referring to pixels
HEIGHT=700
#key
colors={"white":(255,255,255), "pink":(255,0,255), "limegreen":(153,255,51)}
colors.get("limegreen")
#create display window with any name you want
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#Change the title of window
pygame.display.set_caption("My First Game") 
#Set amount of time for game to be displayed
pygame.time.delay(1000)
#creating colors - red
redColor=(255,0,0)
#blue would be (0, 0, 255)
#creating background color
screen.fill(redColor)
pygame.display.update()
pygame.time.delay(1000)
#changing colors to green
greenColor=(0,255,0)
screen.fill(greenColor)
pygame.display.update()
pygame.time.delay(1000)
#changing colors to blue
blueColor=(0,0,255)
screen.fill(blueColor)
pygame.display.update()
pygame.time.delay(1000)
#purple
purpleColor=(125, 0, 125)
hb=50
wb=50
xb=100
yb=300
square=(xb,yb,wb,hb) #create the object to draw
#to keep running, create a loop
background=greenColor
run = True
while run:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            run=False
            print('Game Over')
    #to draw a rectangle: rect(surface, color, rect) -> rect
    pygame.draw.rect(screen, redColor, square)
    #to draw a circle: circle(surface, color, center, radius) 
    pygame.draw.circle(screen, purpleColor, (350,350), 25)
    pygame.display.update()
