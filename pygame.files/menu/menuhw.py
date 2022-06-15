#SophiaSachedina
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
# K_w                   w key
# K_a                   a key
# K_s                   s key
# K_d                   d key

import pygame, os, time, random, math, sys
pygame.init()

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 50)
MENU_FONT = pygame.font.SysFont('comicsans', 30)

os.system('cls')

#screen dimentions
WIDTH = 700
HEIGHT = 700

#colors
colors = {"white":(255,255,255), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr = colors.get("white")

#create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game 1") # title of the window

#images
bg = pygame.image.load("pygame.files\images\images\\bg1.jpg")
char = pygame.image.load("pygame.files\images\images\standing.png")
char = pygame.transform.scale(char, (50,50))
walkRight = [pygame.image.load('pygame.files\images\images\R1.png'), pygame.image.load('pygame.files\images\images\R2.png'), pygame.image.load('pygame.files\images\images\R3.png'), pygame.image.load('pygame.files\images\images\R4.png'), pygame.image.load('pygame.files\images\images\R5.png'), pygame.image.load('pygame.files\images\images\R5.png'), pygame.image.load('pygame.files\images\images\R7.png'), pygame.image.load('pygame.files\images\images\R8.png'), pygame.image.load('pygame.files\images\images\R9.png')]
walkLeft = [pygame.image.load('pygame.files\images\images\L1.png'), pygame.image.load('pygame.files\images\images\L2.png'), pygame.image.load('pygame.files\images\images\L3.png'), pygame.image.load('pygame.files\images\images\L4.png'), pygame.image.load('pygame.files\images\images\L5.png'), pygame.image.load('pygame.files\images\images\L6.png'), pygame.image.load('pygame.files\images\images\L7.png'), pygame.image.load('pygame.files\images\images\L8.png'), pygame.image.load('pygame.files\images\images\L9.png')]
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#circle var
cx = 350
cy = 350
rad = 25

#square var
hb = 50
wb = 50
xb = 325
yb = 325
square = pygame.Rect(xb,yb,wb,hb) #create the object to draw

#char var
charx = xb
chary = yb

#inscribed square
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)
insSquare=pygame.Rect(xig,yig,ibox,ibox)

#bounce
mountainSquare = pygame.Rect(250, 320, 180, 250)

#Game Code
speed = 2
run = True
background = colors.get("grey")

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
    
def menu():
    #title font
    screen.fill(colors.get("white"))
    Title = TITLE_FONT.render("Game Menu", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 30))\

    
    #creating buttons
    Button_1 = pygame.Rect(250, 150, 200, 50)
    Button_2 = pygame.Rect(250, 225, 200, 50)
    Button_3 = pygame.Rect(250, 300, 200, 50)
    Button_4 = pygame.Rect(250, 375, 200, 50)
    Button_5 = pygame.Rect(250, 450, 200, 50)
    Button_6 = pygame.Rect(250, 525, 200, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_1)
    pygame.draw.rect(screen, colors.get("pink"), Button_2)
    pygame.draw.rect(screen, colors.get("pink"), Button_3)
    pygame.draw.rect(screen, colors.get("pink"), Button_4)
    pygame.draw.rect(screen, colors.get("pink"), Button_5)
    pygame.draw.rect(screen, colors.get("pink"), Button_6)

    #render yes and no
    text1 = MENU_FONT.render("Instructions", 1, colors.get("black"))
    text2 = MENU_FONT.render("Level 1", 1, colors.get("black"))
    text3 = MENU_FONT.render("Level 2", 1, colors.get("black"))
    text4 = MENU_FONT.render("Score", 1, colors.get("black"))
    text5 = MENU_FONT.render("Settings", 1, colors.get("black"))
    text6 = MENU_FONT.render("Exit", 1, colors.get("black"))
    screen.blit(text1, (265, 155))
    screen.blit(text2, (300, 230))
    screen.blit(text3, (300, 305))
    screen.blit(text4, (300, 380))
    screen.blit(text5, (300, 455))
    screen.blit(text6, (300, 530))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint(mx, my):
                    instructions()
                if Button_2.collidepoint(mx, my):
                    game()
                if Button_3.collidepoint(mx, my):
                    game()
                if Button_4.collidepoint(mx, my):
                    score()
                if Button_5.collidepoint(mx, my):
                    settings()
                if Button_6.collidepoint(mx, my):
                    pygame.quit()
                
def settings():
    #title font
    screen.fill(colors.get("white"))
    Title = TITLE_FONT.render("Settings", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 30))
    myFile = open("pygame.files\instructions.txt", "r")
    content = myFile.readlines()

    
    #creating buttons
    Button_7 = pygame.Rect(250, 150, 200, 50)
    Button_8 = pygame.Rect(250, 225, 200, 50)
    Button_9 = pygame.Rect(250, 300, 200, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_7)
    pygame.draw.rect(screen, colors.get("pink"), Button_8)
    pygame.draw.rect(screen, colors.get("pink"), Button_9)

    #render yes and no
    text7 = MENU_FONT.render("Background Color", 1, colors.get("black"))
    text8 = MENU_FONT.render("Screen Size", 1, colors.get("black"))
    text9 = MENU_FONT.render("Sound On/Off", 1, colors.get("black"))
    screen.blit(text7, (265, 155))
    screen.blit(text8, (300, 230))
    screen.blit(text9, (300, 305))
    pygame.time.delay(5000)

def instructions():
    screen.fill(colors.get("white"))
    Title = TITLE_FONT.render("Instructions", 1, colors.get("black"))
    #Instructions File
    myFile = open("pygame.files\instructions.txt", "r")
    content = myFile.readlines()

    #print instructions
    yi = 150
    for line in content:
        Insctruc = MENU_FONT.render(line[0:-1], 1, colors.get('black'))
        screen.blit(Insctruc, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 40
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                menu()
def score():
    screen.fill(colors.get("white"))
    Title = TITLE_FONT.render("Scoreboard", 1, colors.get("black"))
    #Score File
    myFile = open("python.files\scre.txt", "r")
    content = myFile.readlines()

    #print instructions
    yi = 150
    for line in content:
        Insctruc = MENU_FONT.render(line[0:-1], 1, colors.get('black'))
        screen.blit(Insctruc, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 40
#main Game
#Game Code
speed = 2
run = True
background = colors.get("grey")

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
def game():
    while run:
        # screen.fill(background)
        pygame.draw.rect(screen, colors.get("white"), mountainSquare)
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # print(mousePos)
        keys = pygame.key.get_pressed() #allow us to see what key was pressed

        

        #square movement
        if keys[pygame.K_d] and square.x < WIDTH-wb:
            square.x += speed
            charx += speed
        if keys[pygame.K_a] and square.x > 0:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_s] and square.y < HEIGHT-hb:
            square.y += speed
            chary += speed
        if keys[pygame.K_w] and square.y > 0:
            square.y -= speed
            chary -= speed

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
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
        #mountain collide square
        if square.colliderect(mountainSquare):
            square.x = 10
            square.y = 10
            charx = 10
            chary = 10
        
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
        screen.blit(char, (charx, chary))

        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("red"), (cx, cy), rad)
        
        pygame.display.update()
        pygame.time.delay(500000)

menu()