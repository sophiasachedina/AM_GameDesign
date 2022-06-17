#Sophia Sachedina
#TicTacToe Game
#Functions: 
    #grid(), 
    #zeroGrid()
    #drawMarkers()
    #checkWinner()
    #gameOver()

import pygame, time, random, math, sys, os
os.system('cls')
pygame.init()


WIDTH=700 
HEIGHT=700

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//30)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), 'red':(255, 0, 0), 'purple': (138,43,226), 'yellow':(255,215,0), 'black':(0,0,0), 'lblue':(0,206,209)}

screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Tic Tac Toe')


size = 3
player=1   
gameOver=False 
markers=[] 
winner = 0 
lineWidth=10 
Game=True 
MxMy=(0,0) 
circlecolor=colors.get("purple") 
xcolor=colors.get("white")

#function for zero array
def zero_Array(): 
    for x in range(3):
        row= [0] *3
        markers.append(row)
backgrnd=colors.get('pink')

#function for grid
def grid():
    lineClr=colors.get("black")
    for x in range(1,3):
        #horizontal line
        pygame.draw.line(screen,lineClr,(0,HEIGHT//size*x),(WIDTH,HEIGHT//size*x),lineWidth)  
        #vertical line
        pygame.draw.line(screen,lineClr,(WIDTH//size*x, 0),(WIDTH//size*x,HEIGHT),lineWidth)  
    pygame.time.delay(100)

#markers function
def draw_Markers():
    xValue=0
    for x in markers:   
        yValue=0
        for y in x:  
            if y ==1:
                pygame.draw.line(screen,xcolor,(xValue * WIDTH//size + 15, yValue * HEIGHT//size + 15), (xValue * WIDTH//size + WIDTH//size-15, yValue * WIDTH//size + WIDTH//size-15),lineWidth)
                pygame.draw.line(screen, xcolor,(xValue*WIDTH//size +WIDTH//size-15, yValue*HEIGHT//size+15),(xValue *WIDTH//size+15,yValue*HEIGHT//size+HEIGHT//size-15),lineWidth)
            if y==-1:
                pygame.draw.circle(screen,circlecolor,(xValue*WIDTH//size+WIDTH//6,yValue*HEIGHT//size +HEIGHT//6),WIDTH//6-15, lineWidth)
            yValue +=1
        xValue +=1
    pygame.display.update()

#function for is x wins
def x_winner():
    screen.fill(backgrnd)
    text=MENU_FONT.render('Player X won!', 1, (circlecolor))
    screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()
    pygame.time.delay(2000)
    gameEnd()

#function for if o wine
def o_winner():
    screen.fill(backgrnd)
    texto=MENU_FONT.render('Player O won!', 1, (circlecolor))
    screen.blit(texto, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()
    pygame.time.delay(2000)
    gameEnd() 

#function for tie
def tieGame():
    screen.fill(backgrnd)
    textTie=MENU_FONT.render("It's a tie!", 1, (circlecolor))
    screen.blit(textTie, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()
    pygame.time.delay(2000)
    gameEnd()

#function to check for winners
def checkWinner():
    global gameOver, winner
    x_position=0
    for x in markers:
        if sum(x)==3:
            winner =1
            gameOver=True
            x_winner()
        if sum(x)==-3:
            winner = -1
            gameOver = True
            o_winner()
        #check rows for winner
        if markers[0][x_position]+markers[1][x_position]+markers[2][x_position] ==3:
            winner = 1
            gameOver=True
            x_winner()
        
        if markers[0][x_position]+markers[1][x_position]+markers[2][x_position] ==-3:
            winner = -1
            gameOver=True
            o_winner()
        x_position +=1
    #check diagonals for winner
    if markers[0][0]+markers[1][1]+markers[2][2] == 3 or markers[2][0]+markers[1][1]+markers[0][2] ==3:
        winner=1
        gameOver=True
        x_winner()
    if markers[0][0]+markers[1][1]+markers[2][2] == -3 or markers[2][0]+markers[1][1]+markers[0][2] == -3:
        winner=-1
        gameOver=True
        o_winner()
    #check for tie
    if gameOver == False:
        tie = True
        for ROW in markers:
            for COL in ROW:
                if COL ==0:
                    tie = False
        #return winner 
        if tie:  
            gameOver=True
            winner=0
            print(winner)
            tieGame()

def gameEnd():
    global Game
    Game = False
    screen.fill(backgrnd)
    #question
    textagn=MENU_FONT.render('Would you like to play again?', 1, (circlecolor))
    screen.blit(textagn,(WIDTH/size, HEIGHT/size))
    #buttons yes and no
    Button_yes=pygame.Rect(WIDTH/4, HEIGHT//2, 100, 50)
    Button_no=pygame.Rect(size*WIDTH/4, HEIGHT//2, 100, 50)
    pygame.draw.rect(screen, colors.get('black'), Button_yes)
    pygame.draw.rect(screen, colors.get('black'), Button_no)
    #text yes and no
    textYes=MENU_FONT.render('Yes', 1, (colors.get("white")))
    textNo=MENU_FONT.render('No', 1, (colors.get("white")))
    screen.blit(textYes, (WIDTH//4, HEIGHT//2))
    screen.blit(textNo, (size*WIDTH//4, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(10000)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousePos=pygame.mouse.get_pos()
            mx=mousePos[0]
            my=mousePos[1]
            if Button_yes.collidepoint((mx, my)):
                Game = True
                zero_Array()
            if Button_no.collidepoint((mx, my)):
                text=MENU_FONT.render('Bye!', 1, (circlecolor))
                screen.fill(backgrnd)
                screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
                Game = False
                pygame.display.update()
                pygame.time.delay(1000)
                pygame.display.quit()
                

zero_Array()
while Game:
    screen.fill(backgrnd)
    grid()
    draw_Markers()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MxMy = pygame.mouse.get_pos()
            xcell=MxMy[0]//(WIDTH//3)
            ycell=MxMy[1]//(HEIGHT//3)
            if markers[xcell][ycell]==0:
                markers[xcell][ycell]=player
                player *=-1
                checkWinner()
                print(winner)
                if gameOver:
                    gameEnd()
