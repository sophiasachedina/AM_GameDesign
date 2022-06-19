#Ruth Gebru
#6/9/2022
#We are learning pygame basic functins, 
# creating screens, clrs, shape ,move 
# move  the square
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
#picture = pygame. image. load(filename)
#picture = pygame. transform. scale(picture, (1280, 720))
#bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')


import sys
import pygame, time,os,random, math
pygame.init()#initialize the pygame package

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
clr=colors.get("limeGreen")
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window

#boxes for menu
Bx=WIDTH//3
Button_menu=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_instruct=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_settings=pygame.Rect(Bx, 200, WIDTH//4, 40)
Button_Game1=pygame.Rect(Bx, 250, WIDTH//4, 40)
Button_Game2=pygame.Rect(Bx, 300, WIDTH//4, 40)
Button_score=pygame.Rect(Bx, 350, WIDTH//4, 40)
Button_exit= pygame.Rect(Bx, 400, WIDTH//4, 40)
Button_colors=pygame.Rect(Bx, 150, WIDTH//3, 40)
Button_size=pygame.Rect(Bx, 200, WIDTH//3, 40)
Button_sound=pygame.Rect(Bx, 250, WIDTH//3, 40)
#images
bg=pygame.image.load('images\\bgSmaller.jpg')
char = pygame.image.load('images\standing.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#square Var
hb=50
wb=50
xb=100
yb=300

#character vars
charx = xb
chary = yb

#circle
cx=350
cy=350
rad=25

#inscribed box
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)
insSquare=pygame.Rect(xig,yig,ibox,ibox)

#mouse varuables
mx = 0
my = 0

#objects to draw
squareClr=colors.get("limeGreen")
#keep running create a lp
circleClr=colors.get("blue")
backgrnd=colors.get("Pink")

#colors
squareClr=colors.get("pink")
mountainSquare=pygame.Rect(250,320,180,250)
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")

#Game control
run = True
Game = False
speed=2

#Menu items
menuMessage = ["Instructions", "Setting", "Game 1", "Game 2", "Scoreboard", "Exit"]
menuSetting = ["Background","Screensize","Sound off/on"]

def menu(message):
    screen.fill(colors.get("white"))
    ymenu = 155
    Title = TITLE_FONT.render("Circle Eats Square", 1, colors.get("blue"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 100))
    Button_1 = pygame.Rect(30, 145, 150, 50)
    Button_2 = pygame.Rect(30, 195, 150, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)
    Button_3 = pygame.Rect(30, 245, 150, 50)
    Button_4 = pygame.Rect(30, 295, 150, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_4)
    Button_5 = pygame.Rect(30, 345, 150, 50)
    Button_6 = pygame.Rect(30, 395, 150, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_5)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_6)
    for item in message:
        text = MENU_FONT.render(item, 1, colors.get('blue'))
        screen.blit(text, (40, ymenu))
        pygame.display.update()
        pygame.time.delay(50)
        ymenu += 50
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    Instructions()
                if Button_2.collidepoint((mx, my)):
                    setting(menuSetting)
                if Button_3.collidepoint((mx, my)):
                    game("HWimage.py")
                if Button_4.collidepoint((mx, my)):
                    game()
                if Button_5.collidepoint((mx, my)):
                    scoreboard()
                    print()
                if Button_6.collidepoint((mx, my)):
                    pygame.quit()
                    sys.exit()
def setting(message):
    global screen, WIDTH, HEIGHT
    global menuSetting
    global mx,my
    screen.fill(colors.get("white"))
    ymenu = 155
    Title = TITLE_FONT.render("Settings", 1, colors.get("blue"))  
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 100))
    Button_1 = pygame.Rect(30, 145, 150, 50)
    Button_2 = pygame.Rect(30, 195, 150, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)
    Button_3 = pygame.Rect(30, 245, 150, 50)
    for item in message:
        text = MENU_FONT.render(item, 1, colors.get('blue'))
        screen.blit(text, (40, ymenu))
        pygame.display.update()
        pygame.time.delay(50)
        ymenu += 50
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
            if Button_1.collidepoint((mx, my)):
                    # backgroundcolor()
                    menucolor= (random.randint (255,255,255), random.randint(255,0,255), random.randint(0,0,255), random.randint(153,255,51))
                    print("color change")
            if Button_2.collidepoint((mx, my)):
                    # screensize()
                    WIDTH+=100
                    HEIGHT+=100
            if Button_3.collidepoint((mx, my)):
                   #Sound off/on()
                    pygame.quit()
                    sys.exit()

def scoreboard():
    #rendering text objects
    Title = TITLE_FONT.render("Scoreboard", 1, colors.get("blue"))
    text1 = MENU_FONT.render( 1, colors.get("blue"))
    text2 = MENU_FONT.render( 1, colors.get("blue"))  

    myFile = open("instructions.txt", "r")
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

def Instructions():
    #rendering text objects
    Title = TITLE_FONT.render("instructions.txt", 1, colors.get("blue"))
    text1 = MENU_FONT.render( 1, colors.get("blue"))
    text2 = MENU_FONT.render( 1, colors.get("blue"))

    #fills screen with white
    screen.fill(colors.get("white"))

    #creating button options
    Button_1 = pygame.Rect(200, 400, 100, 50)
    Button_2 = pygame.Rect(400, 400, 100, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)


    #Instructions
    myFile = open("instructions.txt", "r")
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
    screen.blit(text1, (225, 410))
    screen.blit(text2, (425, 410))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    return True
                if Button_2.collidepoint((mx, my)):
                    return False

def game():
    global charx, chary, rad
    while run:
    # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
        screen.blit(bg, (0,0))
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and squareClr.x < WIDTH -(wb):
            squareClr.x += speed
            charx += speed
        if keys[pygame.K_LEFT] and  squareClr.x > speed:
            squareClr.x -= speed
            charx -= speed
        if keys[pygame.K_UP] and squareClr.y >speed:   #means clser t 0
            squareClr.y -= speed
            chary -= speed
        if keys[pygame.K_DOWN] and squareClr.y <HEIGHT -hb:  #means clser t max value HEIGHT
            squareClr.y += speed
            chary += speed
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

        if squareClr.colliderect(insSquare):
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, squareClr,squareClr)
        screen.blit(char, (charx, chary))
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, circleClr, (cx,cy), rad)
        pygame.draw.rect(screen, squareClr, insSquare)
        pygame.display.update()

menu(menuMessage)