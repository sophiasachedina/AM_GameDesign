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

#menu function
def Menu(Title, message, MENU):
    
    Title = TITLE_FONT.render(Title, 1, colors.get("BLACK"))
    screen.fill(colors.get('white'))
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
                screen.fill(colors.get('white'))
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
                    instructions("Instructions","pygame.files\instructions.txt")
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Level1.collidepoint((mx,my)):
                    game()
                if Button_Level2.collidepoint((mx,my)):
                    game()
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

#instructions function                   
def instructions(titleF,fileN):
    
    #white bg
    screen.fill(colors.get("white"))
    
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
    screen.fill(colors.get("white"))
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
    Menu("Settings",messageSettings, False)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Menu(titleMain,messageMenu,True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_changecolors.collidepoint((mx, my)):
                    print("code to change colors")
                if Button_changescreensize.collidepoint((mx, my)):
                    print("code to change size")
                if Button_changesound.collidepoint((mx, my)):
                    print("code to change sounds")

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
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(widthbox):
            square.x += speed
            characterx += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            characterx -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            charactery -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -heightbox:  #means clser t max value HEIGHT
            square.y += speed
            charactery += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
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

Menu(titleMain,messageMenu, True)