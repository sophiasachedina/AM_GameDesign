#SophiaSachedina
#TicTacToe game

import pygame, time,os,random, math, sys,datetime
pygame.init()
os.system('cls')
WIDTH=600 
HEIGHT=600
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Menu HW Game")  

#list for colors
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),
"RED" : (255, 0, 0), "GREEN" : (0, 255, 0), "BLUE" : (0, 0,255), "BLACK" : (0, 0, 0), "GREY" : (190, 190, 190),
"WHITE" : (255, 255,255), "BROWN" : (166, 42, 42), "GREEN_1" : (0, 255, 0), "ORANGE" : (255, 165, 0),"PINK" : (205, 96, 144),}

#Functions:
    #draw_grid()
    #zero_grid()
    #draw_marker() - to draw x's and o's
    #checkforwin()
    #gameover
    #score

SIZE = 3  
markers = []
MxMy = (0,0)
linewidth = 10
cellx = 0
celly = 0
player = 1
circlecolor = colors.get("BLACK")
xColor = colors.get("BlUE")
bgColor = colors.get("PINK")

def zero_grid():
    for x in range(3):
        row = [0]*SIZE #to create 3 rows of zeroes
        markers.append(row)

#zero_grid()
#print(markers)
#markers[1][1] = -1 #first index is the row, second index is the column
#print(markers)
#print(markers[1][1])

def checkforwinner():
    print(markers[0][0])

def draw_grid():

    lineColor = colors.get("BLACK")
    for x in range(SIZE):
        #horizontal line:
        pygame.draw.line(screen, lineColor, (0, HEIGHT//SIZE*x), (WIDTH, HEIGHT//SIZE*x), linewidth) 
        #vertical line
        pygame.draw.line(screen, lineColor, (WIDTH//SIZE*x, 0), (WIDTH//SIZE*x, HEIGHT), linewidth)
        pygame.display.update()

draw_grid()

def draw_markers():
    xValue = 0
    for x in markers: #gives each row
        yValue = 0
        for y in x: #each element in the row
            if y == 1:
                print(y)
                #pygame.draw.line(screen, xColor,(xValue*WIDTH//3+15, yValue*HEIGHT//3-15), (xValue*WIDTH//3+WIDTH//3-15 , yValue*HEIGHT+15) linewidth)
            if y == -1:
                #draw o
                pygame.draw.circle(screen, circlecolor, (xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3+HEIGHT//6), WIDTH//6-25, linewidth)
            yValue += 1
            xValue += 1

zero_grid()

Game = True
while Game:
    screen.fill(bgColor)
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(titleMain,messageMenu,True)
            pygame.quit
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MxMy = pygame.mouse.get_pos()
            cellx = MxMy[0]//(WIDTH//SIZE)
            celly = MxMy[1]//(HEIGHT//SIZE)
            print(markers)
            if markers [cellx][celly] == 0:
                markers [cellx][celly] == player
                player *= -1

    pygame.time.delay(50)
    pygame.display.update()


            
