# #shreyaChhaya
# #6/9/2022
# #We are learning pygame basic functins, 
# # creating screens, clrs, shape ,move 
# # move  the square
# # K_UP                  up arrow
# # K_DOWN                down arrow
# # K_RIGHT               right arrow
# # K_LEFT                left arrow
# #picture = pygame. image. load(filename)
# #picture = pygame. transform. scale(picture, (1280, 720))
# #bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')


from subprocess import HIGH_PRIORITY_CLASS
import sys
import pygame, time, os,random, math, datetime
date=datetime.datetime.now()
from pygame import mixer
from pygame.locals import*
pygame.init()#initialize the pygame package

os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
clock=pygame.time.Clock()

menuColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//30)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), 'red':(255, 0, 0), 'purple': (138,43,226), 'yellow':(255,215,0), 'black':(0,0,0), 'lblue':(0,206,209)}

message=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window


#background music
mixer.music.load('background (1).wav')
mixer.music.play(-1)

#boxes for menu
Bx=WIDTH/2.5
Button_menu=pygame.Rect(Bx, 125, WIDTH/4, 40)
Button_instruct=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_settings=pygame.Rect(Bx, 200, WIDTH/4, 40)
Button_Game1=pygame.Rect(Bx, 250, WIDTH/4, 40)
Button_Game2=pygame.Rect(Bx, 300, WIDTH/4, 40)
Button_score=pygame.Rect(Bx, 350, WIDTH/4, 40)
Button_exit=pygame.Rect(Bx, 400, WIDTH/4, 40)
#images
bg=pygame.image.load('PygameFiles\images\\bgSmaller.jpg')
char = pygame.image.load('PygameFiles\images\PixelArtTutorial.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

mx = 0
my = 0


def mainMenu():
    global menuColor
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_settings)
    Title = TITLE_FONT.render("Circle eats Square Menu", 1, colors.get("blue"))
    screen.fill(menuColor)
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    
    for item in message:
        Button_menu=pygame.Rect(WIDTH/2.5, yMenu, WIDTH/4, 40)
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
        screen.blit(text, (WIDTH/2.5, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    MENU=True
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("You quit")
                pygame.display.quit()
                MENU=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct.collidepoint((mx, my)):
                    Instructions()
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Game1.collidepoint((mx, my)):
                    Game_1()
                if Button_score.collidepoint((mx, my)):
                    scoreboard()
                if Button_exit.collidepoint((mx, my)):
                    exit()
                if Button_Game2.collidepoint((mx, my)):
                    Game_2()


    
def Instructions():
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))
    text = MENU_FONT.render('Return to Menu', 1, colors.get('blue'))

    #fills screen with white
    screen.fill(menuColor)

    #creating button options
    Button_1 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)

    #Instructions
    myFile = open("PygameFiles\instructions.txt", "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    screen.blit(text, (WIDTH//17,HEIGHT/1.1))

    pygame.display.update()
    Instructions = True
    while Instructions:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Instructions=False
                pygame.display.quit()
                print("You quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    mainMenu() 


def settings():
    global menuColor
    global screen 
    global WIDTH
    global HEIGHT
    title=TITLE_FONT.render('Settings', 1, colors.get('blue'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))

    screen.fill(menuColor)

    color=MENU_FONT.render('Change Background Color:', 1, colors.get('blue'))
    screen.blit(color, (WIDTH/18, HEIGHT/4))
    pygame.display.update()
    pygame.time.delay(50)
    
    
#changing color random
    Button_color = pygame.Rect(WIDTH/21, HEIGHT/3, WIDTH//3.8, 40)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_color)

    textcolor = MENU_FONT.render('Random', 1, colors.get('blue'))
    screen.blit(textcolor, (WIDTH/20, HEIGHT/3))
#back to menu
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)

    #buttons for size changing 
    Button_4=pygame.Rect(WIDTH/20, HEIGHT/1.8, WIDTH//7, 40)
    Button_5=pygame.Rect(WIDTH/4, HEIGHT/1.8, WIDTH//5, 40)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_4)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_5)

    #buttons for sound
    Button_on=pygame.Rect(WIDTH/20, HEIGHT/1.3, WIDTH//6, 40)
    Button_off=pygame.Rect(WIDTH/3, HEIGHT/1.3, WIDTH//6, 40)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_on)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_off)

    #text for buttons/screen
    screen.blit(title, (WIDTH/2.5,50))
    screen.blit(text, (WIDTH//18, HEIGHT/1.1))
    text5=MENU_FONT.render('UP 100', 1, colors.get('blue'))
    text6=MENU_FONT.render('DOWN 100', 1, colors.get('blue'))
    screen.blit(text5, (WIDTH/18, HEIGHT/1.8))
    screen.blit(text6, (WIDTH/4, HEIGHT/1.8))
    
    text7=MENU_FONT.render('Sound On', 1, colors.get('blue'))
    text8=MENU_FONT.render('Sound Off', 1, colors.get('blue'))
    screen.blit(text7, (WIDTH/18, HEIGHT/1.3))
    screen.blit(text8, (WIDTH/3, HEIGHT/1.3))
    text10=MENU_FONT.render('Change screen size:', 1, colors.get('blue'))
    text11=MENU_FONT.render('Change sound settings:', 1, colors.get('blue'))
    screen.blit(text10, (WIDTH/18, HEIGHT/2.1))
    screen.blit(text11, (WIDTH/18, HEIGHT/1.5))
    pygame.display.update()

    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                mainMenu()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                #button for menu
                if Button_3.collidepoint((mx, my)):
                    mainMenu()
                    #button for color
                if Button_color.collidepoint((mx, my)):
                    menuColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    print("change color")
                    pygame.display.update()
                    settings()
                    #buttons for sound
                if Button_on.collidepoint((mx,my)):
                    mixer.music.play(-1)
                    print("music on")
                if Button_off.collidepoint((mx,my)):
                    mixer.music.stop()
                    print("music off")
                    #buttons for sizing
                if Button_4.collidepoint((mx,my)) and WIDTH <1000 and HEIGHT<1000:
                    WIDTH +=100
                    HEIGHT +=100
                    screen=pygame.display.set_mode((WIDTH, HEIGHT))
                    settings()
                if Button_5.collidepoint((mx,my)) and WIDTH>600 and HEIGHT>600:
                    WIDTH -=100
                    HEIGHT -=100
                    screen=pygame.display.set_mode((WIDTH, HEIGHT))
                    settings()
            pygame.display.update()


def scoreboard():
    high=0
    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    screen.fill(menuColor)
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    
    screen.blit(title, (WIDTH//3,50))
    screen.blit(text3, (WIDTH//17, HEIGHT/1.1))
    pygame.display.update()
    
    
    print(score)
    # if score>high:
    #     high=score
    # scrLine=str(high)+"\t " (':')+ "\t" +date.strftime('%m/%d/%Y')+ "\n"
    scrLine=str(score)+(': ')+ '\t'+ userName+ "\t"+date.strftime("%m-%d-%Y")+ "\n"
    myFile = open("PygameFiles\scoreboard.txt", "a")
    myFile.write(str(scrLine))
    myFile.close()

    myFile=open('pygameFiles\scoreboard.txt', 'r')
    content = myFile.readlines()

    #var to controll change of line
    yscore = 150
    for lines in content:
        Instruc = MENU_FONT.render(lines[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yscore))
        pygame.display.update()
        pygame.time.delay(50)
        yscore += 40

    myFile.close()

    scoreboard=True
    while scoreboard:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()

def exit():
    title=TITLE_FONT.render('Bye-Bye!', 1, colors.get('blue'))
    screen.fill(menuColor)

    screen.blit(title, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()

    pygame.time.delay(1000)
    pygame.display.quit()
    



def Game_1():
    global score 
    score=0
    hb=50
    wb=50
    xb=100
    rad=25
    yb=300
    high=0

    charx = xb
    chary = yb

    cx=350
    cy=350
    speed=2
    ibox = rad*math.sqrt(2)
    xig = cx-(ibox/2)
    yig = cy-(ibox/2)

    #mouse varuables
    global mx
    global my


    #bg=pygame.image.load('PygameFiles\images\\bgSmaller.jpg')
    #char = pygame.image.load('PygameFiles\images\PixelArtTutorial.png')
    #char = pygame.transform.scale(char, (50, 50))

    square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
    insSquare=pygame.Rect(xig,yig,ibox,ibox)
    squareClr=colors.get("pink")
    #keep running create a lp
    mountainSquare=pygame.Rect(250,320,180,250)
    circleClr=colors.get("blue")
    backgrnd=colors.get("pink")
    run = True
    while run:
        pygame.draw.rect(screen, colors.get("white"), mountainSquare)
        #screen.blit(bg, (0,0))
        screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # print(mousePos)
        keys = pygame.key.get_pressed() #allow us to see what key was pressed

        #square movement
        if keys[pygame.K_d] and square.x < WIDTH-wb:
            square.x += speed
            #charx += speed
        if keys[pygame.K_a] and square.x > 0:
            square.x -= speed
            #charx -= speed
        if keys[pygame.K_s] and square.y < HEIGHT-hb:
            square.y += speed
            #chary += speed
        if keys[pygame.K_w] and square.y > 0:
            square.y -= speed
            #chary -= speed

        #circle and inscribed square movement
        if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_LEFT] and cx > 0+rad:
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
            cy += speed
            insSquare.y += speed
        if keys[pygame.K_UP] and cy > 0+rad:
            cy -= speed
            insSquare.y -= speed
        
        #circle square collide
        if square.colliderect(insSquare): 
            print("BOOM")
            cx = random.randint(rad, WIDTH-rad)
            cy = random.randint(rad, HEIGHT-rad)
            rad += 5
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            score+=1
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
        #mountain collide square
        if square.colliderect(mountainSquare):
            square.x = 10
            square.y = 10
            #charx = 10
            #chary = 10
        
        #mountain collide circle
        if insSquare.colliderect(mountainSquare):
            cx = rad + 10
            cy = rad + 10
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, object)
        pygame.draw.rect(screen, colors.get("blue"), square)
        pygame.draw.rect(screen, colors.get("blue"), insSquare)
        #screen.blit(char, (charx, chary))

        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("red"), (cx, cy), rad)
        
        pygame.display.update()
        clock.tick(60)

    print(score)

    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    screen.blit(text, (WIDTH//18, HEIGHT/1.1))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()

    

def Game_2():
    global mx
    global my
    player=1   #change player
    gameOver=False #check if game is over
    markers=[] #control cells
    global scoreOne
    global scoreTwo
    scoreOne=0
    scoreTwo=0
    winner = 0 #this means tie - save winner here either 1 or -1
    lineWidth=10 #line thickness
    Game=True #control game
    MxMy=(0,0) #clicks
    cirClr=colors.get("lblue") #colors
    xClr=colors.get("lblue")

    #function to zero array
    def zero_Array(): 
        for x in range(3):
            row= [0] *3
            markers.append(row)
    backgrnd=colors.get('black')


    def grid():
        lineClr=colors.get("purple")
        for x in range(1,3):
            pygame.draw.line(screen,lineClr,(0,HEIGHT//3*x),(WIDTH,HEIGHT//3*x),lineWidth)  #Hztal line
            pygame.draw.line(screen,lineClr,(WIDTH//3*x, 0),(WIDTH//3*x,HEIGHT),lineWidth)  #Vert line
        pygame.time.delay(100)

    def draw_Markers():
        xValue=0
        for x in markers:   # getting a rw
            yValue=0
            for y in x:  #each elem fthe rw
                if y ==1:
                    pygame.draw.line(screen,xClr,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),lineWidth)
                    pygame.draw.line(screen, xClr,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),lineWidth)
                if y==-1:
                    pygame.draw.circle(screen,cirClr,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, lineWidth)
                yValue +=1
            xValue +=1
        pygame.display.update()

    def x_winner():
        screen.fill(backgrnd)
        sx=str(scoreOne)
        so=str(scoreTwo)
        text=MENU_FONT.render('Player X won!', 1, (cirClr))
        textScore=MENU_FONT.render('Player X score = '+sx, 1, (cirClr))
        text2Score=MENU_FONT.render('Player O score = '+so, 1, (cirClr))
        screen.blit(textScore, (WIDTH/4, HEIGHT/1.5))
        screen.blit(text2Score, (WIDTH/1.75, HEIGHT/1.5))
        screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
        ButtonBack = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
        pygame.draw.rect(screen, colors.get("limeGreen"), ButtonBack)
        text = MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
        screen.blit(text, (WIDTH/18, HEIGHT/1.1))
        pygame.display.update()
        run=True 
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    mainMenu()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    #button for menu
                    if ButtonBack.collidepoint((mx, my)):
                        mainMenu()
        pygame.time.delay(5000)

        pygame.display.update()


    def o_winner():
        global mx, my
        screen.fill(backgrnd)
        sx=str(scoreOne)
        so=str(scoreTwo)
        texto=MENU_FONT.render('Player O won!', 1, (cirClr))
        textScore=MENU_FONT.render('Player X score = '+sx, 1, (cirClr))
        text2Score=MENU_FONT.render('Player O score = '+so, 1, (cirClr))
        screen.blit(textScore, (WIDTH/4, HEIGHT/1.5))
        screen.blit(text2Score, (WIDTH/1.75, HEIGHT/1.5))
        screen.blit(texto, (WIDTH/2.5, HEIGHT/2.5))
        Button_1 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
        pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
        text = MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
        screen.blit(text, (WIDTH/18, HEIGHT/1.1))
        pygame.display.update()
        run=True 
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    mainMenu()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    #button for menu
                if Button_1.collidepoint((mx, my)):
                    mainMenu()
        pygame.display.update()
        pygame.time.delay(5000)


    def tieGame():
        screen.fill(backgrnd)
        textTie=MENU_FONT.render("It's a tie!", 1, (cirClr))
        screen.blit(textTie, (WIDTH/2.5, HEIGHT/2.5))
        pygame.display.update()
        Button_1 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
        pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
        text = MENU_FONT.render('Return to Menu', 1, (cirClr))
        screen.blit(text, (WIDTH/18, HEIGHT/1.1))
        run=True 
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    mainMenu()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    #button for menu
                if Button_1.collidepoint((mx, my)):
                    mainMenu()
        pygame.time.delay(5000)
        pygame.display.update()
        

    def checkWinner():
        global gameOver, winner, scoreOne, scoreTwo
        x_position=0
        for x in markers:
            if sum(x)==3:
                winner =1
                scoreOne+=1
                gameOver=True
                x_winner()
            if sum(x)==-3:
                winner = -1
                scoreTwo+=1
                gameOver = True
                o_winner()
            #check rows
            if markers[0][x_position]+markers[1][x_position]+markers[2][x_position] ==3:
                winner = 1
                scoreOne+=1
                gameOver=True
                x_winner()
            
            if markers[0][x_position]+markers[1][x_position]+markers[2][x_position] ==-3:
                winner = -1
                scoreTwo+=1
                gameOver=True
                o_winner()
            x_position +=1
        #check diagonals
        if markers[0][0]+markers[1][1]+markers[2][2] == 3 or markers[2][0]+markers[1][1]+markers[0][2] ==3:
            winner=1
            scoreOne+=1
            gameOver=True
            x_winner()
        if markers[0][0]+markers[1][1]+markers[2][2] == -3 or markers[2][0]+markers[1][1]+markers[0][2] == -3:
            winner=-1
            scoreTwo+=1
            gameOver=True
            o_winner()
        #check tie
        #this part is not working - gameOver==False not defined 
        # if gameOver == False:
        #     tie = True
        #     for ROW in markers:
        #         for COL in ROW:
        #             if COL ==0:
        #                 tie = False
        #     #return winner 
        #     if tie:  #in a boolean variable you dotn need ==
        #         gameOver=True
        #         winner=0
        #         print(winner)
        #         tieGame()

    zero_Array()
    while Game:
        screen.fill(backgrnd)
        grid()
        draw_Markers()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                mainMenu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                MxMy = pygame.mouse.get_pos()
                cellx=MxMy[0]//(WIDTH//3)
                celly=MxMy[1]//(HEIGHT//3)
                if markers[cellx][celly]==0:
                    markers[cellx][celly]=player
                    player *=-1
                    checkWinner()
                    print(winner)
                    if gameOver:
                        gameOver = False
    pygame.display.update()
 
run = True 
screen.fill(menuColor)
userName=''
nameClr=(colors.get('blue')) #for text for name
bxClr=(200, 200, 200) #text box 

title=TITLE_FONT.render('Enter Name', 1, bxClr)
screen.blit(title, (WIDTH/2.5, HEIGHT//7))
pygame.display.update()


nameBox=pygame.Rect(WIDTH//4, HEIGHT//3, WIDTH//2, HEIGHT//10)
pygame.draw.rect(screen, bxClr, nameBox)
pygame.display.update()
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            mainMenu()
            print("You quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(userName)
                #run main menu - if in main program
                mainMenu()
            if event.key ==pygame.K_BACKSPACE: 
                userName=userName[:-1]
                print('back')
            else:
                userName += event.unicode
        pygame.draw.rect(screen, bxClr, nameBox)
        textSurface=MENU_FONT.render(userName, True, nameClr)
        #use rect x and y to  allign the text 
        screen.blit(textSurface, (nameBox.x+5, nameBox.y+5))
        pygame.display.update()
        
        
mainMenu()
Instructions() 
exit()

        

            