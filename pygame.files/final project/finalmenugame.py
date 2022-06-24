#SophiaSachedina
#PLEASE PLEASE WORK PLEASE

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
bg=pygame.image.load('pygame.files\\not final project\images\images\\bg1.jpg')
#character
character = pygame.image.load('pygame.files\\not final project\images\images\standing.png')

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

#menu function
def Menu(Title, message, MENU):
    global menuColor
    global screen 
    global WIDTH
    global HEIGHT
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
                    instructions("Instructions","pygame.files\\not final project\menu\instructions.txt")
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Level1.collidepoint((mx,my)):
                    game()
                if Button_Level2.collidepoint((mx,my)):
                    game2()
                if Button_scoreboard.collidepoint((mx,my)):
                    score("Scoreboard","scre.txt")
                if Button_exit.collidepoint((mx,my)):
                    Title = TITLE_FONT.render("Play Again Soon!", 1, colors.get("PINK"))
                    name="Sophia"
                    scorenum= score
                    date=datetime.datetime.now()
                    scoreLine=str(scorenum)+"      "+name + "      "+date.strftime("%m-%d-%Y")+ "\n"
                    scoreile = open("scre.txt", 'a')
                    scoreile.write(scoreLine)
                    scoreile.close()
                    screen.fill(colors.get('white'))
                    xd = WIDTH//2 - (Title.get_width()//2)
                    yd = HEIGHT//2- 40
                    screen.blit(Title, (xd, yd))
                    pygame.display.update(2000)
                    pygame.quit()
                    sys.exit()

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
    global screen, WIDTH, HEIGHT
    #while run:
        #for event in pygame.event.get():
            #if event.type==pygame.QUIT:
                #Menu(titleMain,messageMenu,True)
    #SophiaSachedina
#pianoTilesGame
    import pygame, os, sys, random
    os.system('cls')
    pygame.init()

    GWIDTH = 300
    GHEIGHT = 510
    gscreen = pygame.display.set_mode((GWIDTH, GHEIGHT))
    pygame.display.set_caption("Piano Tiles Game")

    #fonts
    TITLE_FONT = pygame.font.SysFont('comicsans', GWIDTH//20)
    MENU_FONT = pygame.font.SysFont('comicsans', GWIDTH//30)
    size = 3

    #tile size variables
    tilewidth = GWIDTH//4
    tileheight = 130



    #list for colors
    colors={"limeGreen":(153,255,51),
    "RED" : (255, 0, 0), "GREEN" : (0, 255, 0), "BLUE" : (0, 0,255), 
    "BLACK" : (0, 0, 0), "GREY" : (190, 190, 190), "WHITE" : (255, 255,255), 
    "BROWN" : (166, 42, 42), "GREEN_1" : (0, 255, 0), 
    "ORANGE" : (255, 165, 0),"PINK" : (205, 96, 144),
    "LIGHTBLUE" : (108, 166, 205)}
    textcolor = colors.get("BLACK")

    #image variables
    #background
    bgimage = pygame.image.load("pygame.files\\final project\\bgpt.png")
    bgimage = pygame.transform.scale(bgimage, (GWIDTH, GHEIGHT))
    #startbutton
    startbutton = pygame.image.load("pygame.files\\final project\startbutton.JPG")
    startbutton = pygame.transform.scale(startbutton, (GWIDTH/2.5, GHEIGHT//10))
    startrect = startbutton.get_rect(center = (GWIDTH//2, GHEIGHT - 100))
    #logo
    logo = pygame.image.load("pygame.files\\final project\piano.png")
    logo = pygame.transform.scale(logo, (GWIDTH//1.3, GHEIGHT//2.5))
    #Piano Tiles Game Title
    gametitle = pygame.image.load("pygame.files\\final project\gametitle.JPG")
    gametitle = pygame.transform.scale(gametitle, (GWIDTH/1.2, GHEIGHT//8))
    gametitlerect = startbutton.get_rect(center = (GWIDTH//3.5, GHEIGHT - 200))
    clock = pygame.time.Clock()
    FPS = 30

    #tile variables
    tilewidth = GWIDTH//4
    tileheight = 130

    def gameEnd():
        global MENU_FONT
        Game = False
        screen=pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(backgrndClr)
        #question
        textagn=MENU_FONT.render('Would you like to play again?', 1, (colors.get("PINK")))
        screen.blit(textagn,(WIDTH//4, HEIGHT//8))
        #buttons yes and no
        Button_yes=pygame.Rect(WIDTH/4, HEIGHT//2, 100, 50)
        Button_no=pygame.Rect(size*WIDTH/4, HEIGHT//2, 100, 50)
        pygame.draw.rect(screen, colors.get('PINK'), Button_yes)
        pygame.draw.rect(screen, colors.get('PINK'), Button_no)
        #text yes and no
        textYes=MENU_FONT.render('Yes', 1, (colors.get("BLACK")))
        textNo=MENU_FONT.render('No', 1, (colors.get("BLACK")))
        screen.blit(textYes, (WIDTH//4, HEIGHT//2))
        screen.blit(textNo, (size*WIDTH//4, HEIGHT//2))
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                for event in pygame.event.get():
                    Menu(titleMain, messageMenu, True)
                if event.type==pygame.QUIT:
                        Title = TITLE_FONT.render("Play Again Soon!", 1, colors.get("BLACK"))
                        screen.fill(menuColor)
                        xd = WIDTH//2 - (Title.get_width()//2)
                        yd = HEIGHT//2- 40
                        screen.blit(Title, (xd, yd))
                        name= "Sophia"
                        scorenum= score
                        date=datetime.datetime.now()
                        scoreLine=str(scorenum)+"      "+name + "      "+date.strftime("%m-%d-%Y")+ "\n"
                        scoreile = open("scre.txt", 'a')
                        scoreile.write(scoreLine)
                        scoreile.close()
                        pygame.display.update()
                        pygame.time.delay(2000)
                        Menu(titleMain, messageMenu, True)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    if Button_yes.collidepoint((mx, my)):
                        run = False
                        name= "Sophia"
                        scorenum= score
                        date=datetime.datetime.now()
                        scoreLine=str(scorenum)+"      "+name + "      "+date.strftime("%m-%d-%Y")+ "\n"
                        scoreile = open("scre.txt", 'a')
                        scoreile.write(scoreLine)
                        scoreile.close()
                        markers = []
                        #zero_Array()
                        gameOver = False
                        game()
                    if Button_no.collidepoint((mx, my)):
                        text=MENU_FONT.render('Bye!', 1, (circlecolor))
                        screen.fill(backgrndClr)
                        screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
                        name= "Sophia"
                        scorenum= score
                        date=datetime.datetime.now()
                        scoreLine=str(scorenum)+"      "+name + "      "+date.strftime("%m-%d-%Y")+ "\n"
                        scoreile = open("scre.txt", 'a')
                        scoreile.write(scoreLine)
                        scoreile.close()
                        Game = False
                        Menu(titleMain, messageMenu, True)

    run = True

    #creating tile
    class Tile(pygame.sprite.Sprite):
        def __init__(self, x, y, gscreen):
            super(Tile, self).__init__()

            self.gscreen = gscreen
            self.x = x
            self.y = y
            self.color = colors.get("BLACK")

            #rectangle
            self.surface = pygame.Surface((tilewidth, tileheight), pygame.SRCALPHA)
            self.rect = self.surface.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.center = tilewidth//2, tileheight//2 +15
            self.circlecolor = colors.get("LIGHTBLUE")
            self.linecolor = colors.get("LIGHTBLUE")
            self.circlepos = tilewidth//2, tileheight//1.5
            self.linestart = self.circlepos[0], self.circlepos[1] - 14
            self.lineend = self.center[0], 20
        
        def update(self, speed):
            self.rect.y += speed
            if self.rect.y>= GHEIGHT:
                self.kill()

            pygame.draw.rect(self.surface, self.color, (0,0, tilewidth, tileheight))
            pygame.draw.circle(self.surface, self.circlecolor, self.circlepos, 12, 3)
            pygame.draw.line(self.surface, self.linecolor, self.linestart, self.lineend, 3)

            self.gscreen.blit(self.surface, self.rect)

    #t = Tile(0,10, gscreen)
    tile_group = pygame.sprite.Group()


    #variables to move tiles
    #scroll = 0
    numtile = 1
    score = 0
    speed = 5

    pos = None

    homescreen = True
    gamepage = False
    gameover = False

    def scorescreen():
        global MENU_FONT
        Game = False
        screen=pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(backgrndClr)
        score1 = str(score)
        scoretext = MENU_FONT.render('Congrats! Your score is: '+score1, 1, (colors.get("PINK")))
        screen.blit(scoretext, (WIDTH/4, HEIGHT/8))
        pygame.display.update()
        pygame.time.delay(2000)
        gameEnd()

    run = True
    while run:
        pos = None
        gscreen.blit(bgimage, (0,0)) 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
                #Menu(titleMain,messageMenu,True)
                screen=pygame.display.set_mode((WIDTH, HEIGHT))
                Menu(titleMain,messageMenu,True)
                #pygame.quit()
                #sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                print(pos)
        if homescreen:
            gscreen.blit(logo, (GWIDTH//8, GWIDTH//10))
            gscreen.blit(startbutton, startrect)
            gscreen.blit(gametitle, gametitlerect)

            if pos and startrect.collidepoint(pos):
                homescreen = False
                gamepage = True

                x = random.randint(0,3)
                t = Tile(x*tilewidth, -tileheight, gscreen)
                tile_group.add(t)

                pos = None

        if gamepage:
            #tile_group.update(speed)
            for tile in tile_group:
                tile.update(speed)
                if pos:
                    if tile.rect.collidepoint(pos):
                        tile.kill()
                        score += 1
                        print(score)
                        #print score on the screen
                if tile.rect.bottom >= GHEIGHT:
                    gameover = True
                    #tilebottom()

            #if scroll >= (numtile*tileheight):
            if len(tile_group) > 0:
                t = tile_group.sprites()[-1]
                if t.rect.top + speed >= 0:
                    x = random.randint(0,3)
                    y = -tileheight - (0-t.rect.top)
                    t = Tile(x*tilewidth, y, gscreen)
                    tile_group.add(t)
                    numtile += 1
                    #score+=1

            if gameover: 
                speed = 0
                scorescreen()
                
        clock.tick(FPS)
        pygame.display.update()
            
def game2():
    global screen, WIDTH, HEIGHT
    #while run:
        #for event in pygame.event.get():
            #if event.type==pygame.QUIT:
                #Menu(titleMain,messageMenu,True)
    #SophiaSachedina
#pianoTilesGame
    import pygame, os, sys, random
    os.system('cls')
    pygame.init()

    GWIDTH = 300
    GHEIGHT = 510
    gscreen = pygame.display.set_mode((GWIDTH, GHEIGHT))
    pygame.display.set_caption("Piano Tiles Game")

    #fonts
    TITLE_FONT = pygame.font.SysFont('comicsans', GWIDTH//20)
    MENU_FONT = pygame.font.SysFont('comicsans', GWIDTH//30)
    size = 3

    #tile size variables
    tilewidth = GWIDTH//4
    tileheight = 130



    #list for colors
    colors={"limeGreen":(153,255,51),
    "RED" : (255, 0, 0), "GREEN" : (0, 255, 0), "BLUE" : (0, 0,255), 
    "BLACK" : (0, 0, 0), "GREY" : (190, 190, 190), "WHITE" : (255, 255,255), 
    "BROWN" : (166, 42, 42), "GREEN_1" : (0, 255, 0), 
    "ORANGE" : (255, 165, 0),"PINK" : (205, 96, 144),
    "LIGHTBLUE" : (108, 166, 205)}
    textcolor = colors.get("BLACK")

    #image variables
    #background
    bgimage = pygame.image.load("pygame.files\\final project\\bgpt.png")
    bgimage = pygame.transform.scale(bgimage, (GWIDTH, GHEIGHT))
    #startbutton
    startbutton = pygame.image.load("pygame.files\\final project\startbutton.JPG")
    startbutton = pygame.transform.scale(startbutton, (GWIDTH/2.5, GHEIGHT//10))
    startrect = startbutton.get_rect(center = (GWIDTH//2, GHEIGHT - 100))
    #logo
    logo = pygame.image.load("pygame.files\\final project\piano.png")
    logo = pygame.transform.scale(logo, (GWIDTH//1.3, GHEIGHT//2.5))
    #Piano Tiles Game Title
    gametitle = pygame.image.load("pygame.files\\final project\gametitle.JPG")
    gametitle = pygame.transform.scale(gametitle, (GWIDTH/1.2, GHEIGHT//8))
    gametitlerect = startbutton.get_rect(center = (GWIDTH//3.5, GHEIGHT - 200))
    clock = pygame.time.Clock()
    FPS = 30

    #tile variables
    tilewidth = GWIDTH//4
    tileheight = 130

    def scorescreen():
        global MENU_FONT
        Game = False
        screen=pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(backgrndClr)
        score1 = str(score)
        scoretext = MENU_FONT.render('Congrats! Your score is: '+score1, 1, (colors.get("PINK")))
        screen.blit(scoretext, (WIDTH/4, HEIGHT/8))
        pygame.display.update()
        pygame.time.delay(2000)
        gameEnd()

    def gameEnd():
        global MENU_FONT
        Game = False
        screen=pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(backgrndClr)
        #question
        textagn=MENU_FONT.render('Would you like to play again?', 1, (colors.get("PINK")))
        screen.blit(textagn,(WIDTH//4, HEIGHT//8))
        #textscore=MENU_FONT.render("Congrats! Your score is: ", +score, 1, (colors.get("PINK")))
        #screen.blit(textscore, (WIDTH/2.5, HEIGHT/1.5))
        #buttons yes and no
        Button_yes=pygame.Rect(WIDTH/4, HEIGHT//2, 100, 50)
        Button_no=pygame.Rect(size*WIDTH/4, HEIGHT//2, 100, 50)
        pygame.draw.rect(screen, colors.get('PINK'), Button_yes)
        pygame.draw.rect(screen, colors.get('PINK'), Button_no)
        #text yes and no
        textYes=MENU_FONT.render('Yes', 1, (colors.get("BLACK")))
        textNo=MENU_FONT.render('No', 1, (colors.get("BLACK")))
        screen.blit(textYes, (WIDTH//4, HEIGHT//2))
        screen.blit(textNo, (size*WIDTH//4, HEIGHT//2))
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                for event in pygame.event.get():
                    Menu(titleMain, messageMenu, True)
                if event.type==pygame.QUIT:
                        Title = TITLE_FONT.render("Play Again Soon!", 1, colors.get("BLACK"))
                        screen.fill(menuColor)
                        xd = WIDTH//2 - (Title.get_width()//2)
                        yd = HEIGHT//2- 40
                        screen.blit(Title, (xd, yd))
                        name= "Sophia"
                        scorenum= score
                        date=datetime.datetime.now()
                        scoreLine=str(scorenum)+"      "+name + "      "+date.strftime("%m-%d-%Y")+ "\n"
                        scoreile = open("scre.txt", 'a')
                        scoreile.write(scoreLine)
                        scoreile.close()
                        pygame.display.update()
                        pygame.time.delay(2000)
                        Menu(titleMain, messageMenu, True)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    if Button_yes.collidepoint((mx, my)):
                        run = False
                        name= "Sophia"
                        scorenum= score
                        date=datetime.datetime.now()
                        scoreLine=str(scorenum)+"      "+name + "      "+date.strftime("%m-%d-%Y")+ "\n"
                        scoreile = open("scre.txt", 'a')
                        scoreile.write(scoreLine)
                        scoreile.close()
                        #markers = []
                        #zero_Array()
                        gameOver = False
                        game2()
                    if Button_no.collidepoint((mx, my)):
                        text=MENU_FONT.render('Bye!', 1, (circlecolor))
                        screen.fill(backgrndClr)
                        screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
                        name= "Sophia"
                        scorenum= score
                        date=datetime.datetime.now()
                        scoreLine=str(scorenum)+"      "+name + "      "+date.strftime("%m-%d-%Y")+ "\n"
                        scoreile = open("scre.txt", 'a')
                        scoreile.write(scoreLine)
                        scoreile.close()
                        Game = False
                        Menu(titleMain, messageMenu, True)

    run = True

    #creating tile
    class Tile(pygame.sprite.Sprite):
        def __init__(self, x, y, gscreen):
            super(Tile, self).__init__()

            self.gscreen = gscreen
            self.x = x
            self.y = y
            self.color = colors.get("BLACK")

            #rectangle
            self.surface = pygame.Surface((tilewidth, tileheight), pygame.SRCALPHA)
            self.rect = self.surface.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.center = tilewidth//2, tileheight//2 +15
            self.circlecolor = colors.get("LIGHTBLUE")
            self.linecolor = colors.get("LIGHTBLUE")
            self.circlepos = tilewidth//2, tileheight//1.5
            self.linestart = self.circlepos[0], self.circlepos[1] - 14
            self.lineend = self.center[0], 20
        
        def update(self, speed):
            self.rect.y += speed
            if self.rect.y>= GHEIGHT:
                self.kill()

            pygame.draw.rect(self.surface, self.color, (0,0, tilewidth, tileheight))
            pygame.draw.circle(self.surface, self.circlecolor, self.circlepos, 12, 3)
            pygame.draw.line(self.surface, self.linecolor, self.linestart, self.lineend, 3)

            self.gscreen.blit(self.surface, self.rect)

    #t = Tile(0,10, gscreen)
    tile_group = pygame.sprite.Group()


    #variables to move tiles
    #scroll = 0
    numtile = 1
    score = 0
    speed = 10

    pos = None

    homescreen = True
    gamepage = False
    gameover = False

    run = True
    while run:
        pos = None
        gscreen.blit(bgimage, (0,0)) 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
                #Menu(titleMain,messageMenu,True)
                screen=pygame.display.set_mode((WIDTH, HEIGHT))
                Menu(titleMain,messageMenu,True)
                #pygame.quit()
                #sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                print(pos)
        if homescreen:
            gscreen.blit(logo, (GWIDTH//8, GWIDTH//10))
            gscreen.blit(startbutton, startrect)
            gscreen.blit(gametitle, gametitlerect)

            if pos and startrect.collidepoint(pos):
                homescreen = False
                gamepage = True

                x = random.randint(0,3)
                t = Tile(x*tilewidth, -tileheight, gscreen)
                tile_group.add(t)

                pos = None

        if gamepage:
            #tile_group.update(speed)
            for tile in tile_group:
                tile.update(speed)
                if pos:
                    if tile.rect.collidepoint(pos):
                        tile.kill()
                        score += 1
                        print(score)
                        #print score on the screen
                if tile.rect.bottom >= GHEIGHT:
                    gameover = True
                    #tilebottom()

            #if scroll >= (numtile*tileheight):
            if len(tile_group) > 0:
                t = tile_group.sprites()[-1]
                if t.rect.top + speed >= 0:
                    x = random.randint(0,3)
                    y = -tileheight - (0-t.rect.top)
                    t = Tile(x*tilewidth, y, gscreen)
                    tile_group.add(t)
                    numtile += 1
                    #score+=1

            if gameover: 
                speed = 0
                scorescreen()
                
        clock.tick(FPS)
        pygame.display.update()

namebox()