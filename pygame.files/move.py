#SophiaSachedina
#6/9/2022
#pygame basic functions
#creating screens, colors, shapes, move

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

hb=50
wb=50
xb=100
yb=300
square=pygame.Rect(xb,yb,wb,hb) #create the object to draw
squareColor=colors.get("pink")
#to keep running, create a loop
circleColor=colors.get("pink")
background=colors.get("limegreen")
run = True
#create a variable to move
speed=5
cx=350
cy=350
rad=25
while run:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            run=False
            print('Game Over')
    keys= pygame.key.get_pressed() #this is a list
    if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb+speed):
        square.x += speed
    if keys[pygame.K_LEFT] and square.x > speed:
        square.x += speed
    if keys[pygame.K_DOWN] and square.y > speed:
        square.y += speed
    if keys[pygame.K_UP] and square.y < HEIGHT -(hb):
        square.y += speed

    #to draw a rectangle: rect(surface, color, rect) -> rect
    pygame.draw.rect(screen, squareColor, square)
    #to draw a circle: circle(surface, color, center, radius) 
    pygame.draw.circle(screen, circleColor, (cx,cy), rad)
    pygame.display.update()

    keys= pygame.key.get_pressed() #this is a list
    if keys[pygame.K_d] and cx < WIDTH -(cx+speed):
        cx += speed
    if keys[pygame.K_a] and cx > speed:
        cx += speed
    if keys[pygame.K_s] and cy > speed:
        cy += speed
    if keys[pygame.K_w] and cy < HEIGHT -(cy):
        cy += speed