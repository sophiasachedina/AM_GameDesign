#SophiaSachedina

import pygame, time,os,random, math, sys,datetime
pygame.init()
os.system('cls')
WIDTH=700 
HEIGHT=700
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)

#list for colors
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),
"RED" : (255, 0, 0), "GREEN" : (0, 255, 0), "BLUE" : (0, 0,255), "BLACK" : (0, 0, 0), "GREY" : (190, 190, 190),
"WHITE" : (255, 255,255), "BROWN" : (166, 42, 42), "GREEN_1" : (0, 255, 0), "ORANGE" : (255, 165, 0),"PINK" : (205, 96, 144),}

#Message Lists
messageMenu=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
messageSettings=["Background Color", "Screen Size", "Sound"]
titleMain="Main Menu"
clock = pygame.time.Clock()

#Creating New Window
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Menu HW Game")  

#boxes for menu
boxsize=WIDTH//3
Button_Menu=pygame.Rect(boxsize, 150, WIDTH//4, 40)
Button_Instructions=pygame.Rect(boxsize, 150, WIDTH//4, 40)
Button_settings=pygame.Rect(boxsize, 200, WIDTH//4, 40)
Button_Level1=pygame.Rect(boxsize, 250, WIDTH//4, 40)
Button_Level2=pygame.Rect(boxsize, 300, WIDTH//4, 40)
Button_scoreboard=pygame.Rect(boxsize, 350, WIDTH//4, 40)
Button_exit=pygame.Rect(boxsize, 400, WIDTH//4, 40)
Button_changecolors=pygame.Rect(boxsize, 150, WIDTH//3, 40)
Button_changescreensize=pygame.Rect(boxsize, 200, WIDTH//3, 40)
Button_changesound=pygame.Rect(boxsize, 250, WIDTH//3, 40)

#background
bg=pygame.image.load('pygame.files\images\images\\bg1.jpg')
#character
character = pygame.image.load('pygame.files\images\images\standing.png')

#square variables
heightbox=50
widthbox=50
xbox=100
ybox=300

characterx = xbox
charactery = ybox

cx=350
cy=350
rad=25
speed=2
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse variables
mx = 0
my = 0

#inscribed square and circle variables
square=pygame.Rect(xbox,ybox,widthbox,heightbox)
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squarecolor=colors.get("pink")

mountainSquare=pygame.Rect(250,320,180,250)
circlecolor=colors.get("blue")

run = True
Game = False

#namebox variables
clock= pygame.time.Clock()
backgrndClr=(255,255,255)
run=True #run the while
namecolor=(colors.get("BLACK"))  
boxcolor= (colors.get("PINK"))  

#settings variable
menuColor = colors.get("white")


#menu function
def Menu(Title, message, MENU):
    
    Title = TITLE_FONT.render(Title, 1, colors.get("BLACK"))
    screen.fill(menuColor)
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    for item in message:

        Button_menu=pygame.Rect(boxsize, yMenu, WIDTH//3, 40)
        text=MENU_FONT.render(item, 1, colors.get("BLACK"))
        pygame.draw.rect(screen, colors.get("PINK"), Button_menu)
        screen.blit(text, (boxsize, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Title = TITLE_FONT.render("Play Again Soon!", 1, colors.get("BLACK"))
                screen.fill(menuColor)
                xd = WIDTH//2 - (Title.get_width()//2)
                yd = HEIGHT//2- 40
                screen.blit(Title, (xd, yd))
                pygame.display.update()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_Instructions.collidepoint((mx, my)):
                    instructions("Instructions","pygame.files\menu\instructions.txt")
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Level1.collidepoint((mx,my)):
                    game()
                if Button_Level2.collidepoint((mx,my)):
                    game2()
                if Button_scoreboard.collidepoint((mx,my)):
                    score("Scoreboard","python.files\scre.txt")
                if Button_exit.collidepoint((mx,my)):
                    Title = TITLE_FONT.render("Play Again Soon!", 1, colors.get("PINK"))
                    name="Sophia"
                    scorenum=374
                    date=datetime.datetime.now()
                    scoreLine=str(scorenum)+"      "+name + "      "+date.strftime("%m-%d-%Y")+ "\n"
                    scoreile = open("scre.txt", 'a')
                    scoreile.write(scoreLine)
                    scoreile.close()
                    screen.fill(colors.get('white'))
                    xd = WIDTH//2 - (Title.get_width()//2)
                    yd = HEIGHT//2- 40
                    screen.blit(Title, (xd, yd))
                    pygame.display.update()
                    pygame.quit()
                    sys.exit()

def namebox():
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Get Name")
    screen.fill(menuColor)
    username=''
    title=TITLE_FONT.render("Enter Name", 1, boxcolor)
    screen.blit(title,(200,50))
    #make box
    inputrectangle = pygame.Rect(WIDTH//3, HEIGHT//3, 140, 32)
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                pygame.quit()
                sys.exit()
                print("You quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                #draw box
                print()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    print(username)
                    Menu(titleMain, messageMenu, Menu)
                if event.key==pygame.K_BACKSPACE:
                    username=username[:-1]
                else:
                    username += event.unicode
            pygame.draw.rect(screen, boxcolor, inputrectangle)
    
            textsurface = MENU_FONT.render(username, True, namecolor)
            screen.blit(textsurface, (inputrectangle.x+10, inputrectangle.y-5))
            
            pygame.display.flip()
            
            #clock.tick(60) means that for every second
            clock.tick(60)

#instructions function                   
def instructions(titleF,fileN):
    
    #white bg
    screen.fill(menuColor)
    
    #title
    Title = TITLE_FONT.render(titleF, 1, colors.get("BLACK"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))

    #play button 
    Button_1 = pygame.Rect(200, 400, 100, 50)
    text1 = MENU_FONT.render("play", 1, colors.get("BLACK"))
    pygame.draw.rect(screen, colors.get("ORANGE"), Button_1)
    screen.blit(text1, (225, 410))

    #variables to read files 
    myFile = open(fileN, "r")
    content = myFile.readlines()
    myFile.close()

    #variable to control line
    yi = 150
    for line in content:
        Item = MENU_FONT.render(line[0:-1], 1, colors.get("BLACK"))
        screen.blit(Item, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+= 40

    #mouse
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Menu(titleMain,messageMenu, True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    Menu(titleMain,messageMenu, True) 

#score function
def score(titleF,fileN):
    
    #fills screen with white
    screen.fill(menuColor)
    Title = TITLE_FONT.render(titleF, 1, colors.get("BLACK"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))

    #variables to read files 
    myFile = open(fileN, "r")
    content = myFile.readlines()
    myFile.close()

    #variable to control line
    yi = 150
    for line in content:
        Item = MENU_FONT.render(line[0:-1], 1, colors.get("BLACK"))
        screen.blit(Item, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+= 40

    #back to menu button
    Button_1 = pygame.Rect(50, 50, 100, 50)
    pygame.draw.rect(screen, colors.get("RED"), Button_1)
    text1 = MENU_FONT.render("Menu", 1, colors.get("BLACK"))
    screen.blit(text1, (55, 55))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Menu(titleMain,messageMenu, True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    Menu(titleMain,messageMenu, True) 

#settings function
def settings():
    global menuColor
    global screen 
    global WIDTH
    global HEIGHT
    title=TITLE_FONT.render('Settings', 1, colors.get('BLACK'))

    screen.fill(menuColor)

    color=MENU_FONT.render('Change Background Color:', 1, colors.get('PINK'))
    screen.blit(color, (WIDTH/18, HEIGHT/4))
    pygame.display.update()
    pygame.time.delay(50)
    
    
    #changing background colors randomly
    colorbutton = pygame.Rect(WIDTH/21, HEIGHT/3, WIDTH//3.8, 40)
    pygame.draw.rect(screen, colors.get('PINK'), colorbutton)

    textcolor = MENU_FONT.render('Random', 1, colors.get('BLACK'))
    screen.blit(textcolor, (WIDTH/20, HEIGHT/3))

    #buttons to change size  
    sizeupbutton=pygame.Rect(WIDTH/20, HEIGHT/1.8, WIDTH//7, 40)
    sizedownbutton=pygame.Rect(WIDTH/4, HEIGHT/1.8, WIDTH//5, 40)
    pygame.draw.rect(screen, colors.get('PINK'), sizeupbutton)
    pygame.draw.rect(screen, colors.get('PINK'), sizedownbutton)

    #text 
    screen.blit(title, (WIDTH/2.5,50))
    uptext=MENU_FONT.render('+ 50', 1, colors.get('BLACK'))
    downtext=MENU_FONT.render('- 50', 1, colors.get('BLACK'))
    screen.blit(uptext, (WIDTH/18, HEIGHT/1.8))
    screen.blit(downtext, (WIDTH/4, HEIGHT/1.8))
    text10=MENU_FONT.render('Change screen size:', 1, colors.get('PINK'))
    screen.blit(text10, (WIDTH/18, HEIGHT/2.1))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                Menu(titleMain, messageMenu, True)
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                #buttons for color
                #notworking?? idk why
                if colorbutton.collidepoint((mx, my)):
                    menuColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    print("change color")
                    pygame.display.update()
                    settings()
                if sizeupbutton.collidepoint((mx,my)) and WIDTH <1000 and HEIGHT<1000:
                    WIDTH +=50
                    HEIGHT +=50
                    screen=pygame.display.set_mode((WIDTH, HEIGHT))
                    settings()
                if sizedownbutton.collidepoint((mx,my)) and WIDTH>600 and HEIGHT>600:
                    WIDTH -=50
                    HEIGHT -=50
                    screen=pygame.display.set_mode((WIDTH, HEIGHT))
                    settings()
            pygame.display.update()

def game():
    global mx,my, insSquare, characterx,charactery, cx,cy, rad
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Menu(titleMain,messageMenu,True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
        screen.blit(bg, (0,0))
        keys= pygame.key.get_pressed() 
        
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(widthbox):
            square.x += speed
            characterx += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            characterx -= speed
        if keys[pygame.K_UP] and square.y >speed:   
            square.y -= speed
            charactery -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -heightbox:  
            square.y += speed
            charactery += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
        if square.colliderect(mountainSquare):
            square.x=10
            square.y=10
            characterx=10
            charactery=10
        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, squarecolor,square)
        screen.blit(character, (characterx, charactery))
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, circlecolor, (cx,cy), rad)
        pygame.draw.rect(screen, squarecolor, insSquare)

        #pygame.draw.rect(screen, colors.get('white'), mountainSquare,)
        pygame.display.update()
        clock.tick(60)
player1score = 0
player2score = 0
def game2():
        #Sophia Sachedina
        #TicTacToe Game
        #Functions: 
            #grid(), 
            #zeroGrid()
            #drawMarkers()
            #checkWinner()
            #gameOver()

    import pygame, time, random, math, sys, os, datetime
    os.system('cls')
    pygame.init()


    WIDTH=700 
    HEIGHT=700

    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//30)
    colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), 'red':(255, 0, 0), 'purple': (138,43,226), 'yellow':(255,215,0), 'black':(0,0,0), 'lblue':(0,206,209)}

    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
    pygame.display.set_caption('Tic Tac Toe')

    clock = pygame.time.Clock()

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
        scorex = str(player1score)
        scoreo = str(player2score)
        textx = MENU_FONT.render('Player X won!', 1, (circlecolor))
        pl1txt = MENU_FONT.render('Player X score = '+scorex, 1, (circlecolor))
        pl2txt = MENU_FONT.render('Player O score = '+scoreo, 1, (circlecolor))
        screen.blit(pl1txt, (WIDTH/4, HEIGHT/1.5))
        screen.blit(pl2txt, (WIDTH/1.5, HEIGHT/1.5))
        screen.blit(textx, (WIDTH/size, HEIGHT/size))
        pygame.display.update()
        pygame.time.delay(2000)
        gameEnd()

    #function for if o wine
    def o_winner():
        screen.fill(backgrnd)
        scorex = str(player1score)
        scoreo = str(player2score)
        texto=MENU_FONT.render('Player O won!', 1, (circlecolor))
        pl1txt = MENU_FONT.render('Player X score = '+scorex, 1, (circlecolor))
        pl2txt = MENU_FONT.render('Player O score = '+scoreo, 1, (circlecolor))
        screen.blit(pl1txt, (WIDTH/4, HEIGHT/1.5))
        screen.blit(pl2txt, (WIDTH/1.5, HEIGHT/1.5))
        screen.blit(texto, (WIDTH/2.5, HEIGHT/2.5))
        pygame.display.update()
        pygame.time.delay(2000)
        gameEnd() 

    #function for tie
    def tieGame():
        screen.fill(backgrnd)
        scorex = str(player1score)
        scoreo = str(player2score)
        texto=MENU_FONT.render('Player O won!', 1, (circlecolor))
        pl1txt = MENU_FONT.render('Player X score = '+scorex, 1, (circlecolor))
        pl2txt = MENU_FONT.render('Player O score = '+scoreo, 1, (circlecolor))
        screen.blit(pl1txt, (WIDTH/4, HEIGHT/1.5))
        screen.blit(pl2txt, (WIDTH/1.5, HEIGHT/1.5))
        textTie=MENU_FONT.render("It's a tie!", 1, (circlecolor))
        screen.blit(textTie, (WIDTH/2.5, HEIGHT/2.5))
        pygame.display.update()
        pygame.time.delay(2000)
        gameEnd()

    #function to check for winners
    #notfullyworking
    def checkWinner():
        global gameOver, winner, player1score, player2score
        x_position=0
        for x in markers:
            if sum(x)==3:
                winner = 1
                player1score += 1
                gameOver=True
                x_winner()
            if sum(x)==-3:
                winner = -1
                player2score += 1
                gameOver = True
                o_winner()
            #check rows for winner
            #out of range??
            if markers[0][x_position]+markers[1][x_position]+markers[2][x_position] ==3:
                winner = 1
                player1score += 1
                gameOver=True
                x_winner()        
            if markers[0][x_position]+markers[1][x_position]+markers[2][x_position] ==-3:
                winner = -1
                player2score += 1
                gameOver=True
                o_winner()
            x_position +=1
        #check diagonals for winner
        if markers[0][0]+markers[1][1]+markers[2][2] == 3 or markers[2][0]+markers[1][1]+markers[0][2] ==3:
            winner=1
            player1score += 1
            gameOver=True
            x_winner()
        if markers[0][0]+markers[1][1]+markers[2][2] == -3 or markers[2][0]+markers[1][1]+markers[0][2] == -3:
            winner=-1
            player2score += 1
            gameOver=True
            o_winner()
        #check for tie
        #if gameOver == False:
            #tie = True
            #for ROW in markers:
                #for COL in ROW:
                    #if COL ==0:
                        #tie = False
            #return winner 
            #if tie:  
                #gameOver=True
                #winner=0
                #print(winner)
                #tieGame()

    def gameEnd():
        global markers, gameOver
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
        run = True
        while run:
            for event in pygame.event.get():
                for event in pygame.event.get():
                    Menu(titleMain, messageMenu, True)
                if event.type==pygame.QUIT:
                        Title = TITLE_FONT.render("Play Again Soon!", 1, colors.get("black"))
                        screen.fill(colors.get('white'))
                        xd = WIDTH//2 - (Title.get_width()//2)
                        yd = HEIGHT//2- 40
                        screen.blit(Title, (xd, yd))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        pygame.quit()
                        sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    if Button_yes.collidepoint((mx, my)):
                        run = False
                        markers = []
                        zero_Array()
                        gameOver = False
                    if Button_no.collidepoint((mx, my)):
                        text=MENU_FONT.render('Bye!', 1, (circlecolor))
                        screen.fill(backgrnd)
                        screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
                        Game = False
                        Menu(titleMain, messageMenu, True)
                        #go to main meny
                
                    
    zero_Array()

    while Game:
        clock.tick(60)
        screen.fill(backgrnd)
        grid()
        draw_Markers()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Title = TITLE_FONT.render("Play Again Soon!", 1, colors.get("black"))
                screen.fill(colors.get('white'))
                xd = WIDTH//2 - (Title.get_width()//2)
                yd = HEIGHT//2- 40
                screen.blit(Title, (xd, yd))
                pygame.display.update()
                pygame.time.delay(1000)
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
                        gameOver = False
                        gameEnd()
                        print("im back")

    pygame.display.update()
    clock.tick(60)

namebox()