#SophiaSachedina
#TicTacToe game

from turtle import bgcolor
import pygame, time,os,random, math, sys,datetime, math
pygame.init()
os.system('cls')
WIDTH=600 
HEIGHT=600

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)


#list for colors
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),
"RED" : (255, 0, 0), "GREEN" : (0, 255, 0), "BLUE" : (0, 0,255), "BLACK" : (0, 0, 0), "GREY" : (190, 190, 190),
"WHITE" : (255, 255,255), "BROWN" : (166, 42, 42), "GREEN_1" : (0, 255, 0), "ORANGE" : (255, 165, 0),"PINK" : (205, 96, 144),}

screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Menu HW Game")  

#Functions:
    #draw_grid()
    #zero_grid()
    #draw_marker() - to draw x's and o's
    #checkforwin()
    #gameover
    #score

SIZE = 3  
gameover = False
markers = []
winner = 0
MxMy = (0,0)
linewidth = 10
Game = True
cellx = 0
celly = 0
player = 1
circlecolor = colors.get("BLACK")
xColor = colors.get("BlUE")


def zero_array():
    for x in range(3):
        row = [0]*3 #to create 3 rows of zeroes
        markers.append(row)
bgColor = colors.get("PINK")

def draw_grid():
    lineColor = colors.get("BLACK")
    for x in range(SIZE):
        #horizontal line:
        pygame.draw.line(screen, lineColor, (0, HEIGHT//SIZE*x), (WIDTH, HEIGHT//SIZE*x), linewidth) 
        #vertical line
        pygame.draw.line(screen, lineColor, (WIDTH//SIZE*x, 0), (WIDTH//SIZE*x, HEIGHT), linewidth)
        pygame.time.delay(100)


def draw_markers():
    xValue=0
    for x in markers:   # getting a rw
        yValue=0
        for y in x:  #each elem fthe rw
            if y ==1:
                pygame.draw.line(screen,xColor,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),linewidth)
                pygame.draw.line(screen, xColor,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),linewidth)
            if y==-1:
                pygame.draw.circle(screen,circlecolor,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, linewidth)
            yValue +=1
        xValue +=1
    pygame.display.update()
    
def x_winner():
    screen.fill(bgColor)
    text=MENU_FONT.render('Player X won!', 1, (circlecolor))
    screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()
    pygame.time.delay(2000)
    gameEnd()
def o_winner():
    screen.fill(bgColor)
    texto=MENU_FONT.render('Player O won!', 1, (circlecolor))
    screen.blit(texto, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()
    pygame.time.delay(2000)
    gameEnd() 
def tieGame():
    screen.fill(bgColor)
    textTie=MENU_FONT.render("It's a tie!", 1, (circlecolor))
    screen.blit(textTie, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()
    pygame.time.delay(2000)
    gameEnd()
def checkWinner():
    global gameover, winner
    x_position=0
    for x in markers:
        if sum(x)==3:
            winner =1
            gameover=True
            x_winner()
        if sum(x)==-3:
            winner = -1
            gameover = True
            o_winner()
        #check rows
        if markers[0][x_position]+markers[1][x_position]+markers[2][x_position] ==3:
            winner = 1
            gameover=True
            x_winner()
        
        if markers[0][x_position]+markers[1][x_position]+markers[2][x_position] ==-3:
            winner = -1
            gameover=True
            o_winner()
        x_position +=1
    #check diagonals
    if markers[0][0]+markers[1][1]+markers[2][2] == 3 or markers[2][0]+markers[1][1]+markers[0][2] ==3:
        winner=1
        gameover=True
        x_winner()
    if markers[0][0]+markers[1][1]+markers[2][2] == -3 or markers[2][0]+markers[1][1]+markers[0][2] == -3:
        winner=-1
        gameover=True
        o_winner()
    #check tie
    if gameover == False:
        tie = True
        for ROW in markers:
            for COL in ROW:
                if COL ==0:
                    tie = False
        #return winner 
        if tie:  #in a boolean variable you dotn need ==
            gameover=True
            winner=0
            print(winner)
            tieGame()

def gameEnd():
    global Game
    Game = False
    screen.fill(bgColor)
    #question
    textagn=MENU_FONT.render('Would you like to play again?', 1, (circlecolor))
    screen.blit(textagn,(WIDTH/2.8, HEIGHT/2.8))
    #yes or no buttons
    Button_yes=pygame.Rect(WIDTH/4, HEIGHT//2, 100, 50)
    Button_no=pygame.Rect(3*WIDTH/4, HEIGHT//2, 100, 50)
    pygame.draw.rect(screen, colors.get('pink'), Button_yes)
    pygame.draw.rect(screen, colors.get('pink'), Button_no)
    #yes no text
    textYes=MENU_FONT.render('Yes', 1, (circlecolor))
    textNo=MENU_FONT.render('No', 1, (circlecolor))
    screen.blit(textYes, (WIDTH//4, HEIGHT//2))
    screen.blit(textNo, (3*WIDTH//4, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(10000)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousePos=pygame.mouse.get_pos()
            mx=mousePos[0]
            my=mousePos[1]
            if Button_yes.collidepoint((mx, my)):
                Game = True
                zero_array()
            if Button_no.collidepoint((mx, my)):
                text=MENU_FONT.render('Bye!', 1, (circlecolor))
                screen.fill(bgColor)
                screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
                Game = False
                pygame.display.update()
                pygame.time.delay(1000)
                pygame.display.quit()
                

zero_array()

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
            if markers [cellx][celly] == 0:
                markers [cellx][celly] == player
                player *= -1
                checkWinner()
                if gameover:
                    gameEnd()

    #pygame.time.delay(50)
    #pygame.display.update()


            
