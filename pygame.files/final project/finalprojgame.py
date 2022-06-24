#SophiaSachedina
#pianoTilesGame
import pygame, os, sys, random
os.system('cls')
pygame.init()

GWIDTH = 300
GHEIGHT = 510
screen = pygame.display.set_mode((GWIDTH, GHEIGHT))
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

run = True

#creating tile
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super(Tile, self).__init__()

        self.screen = screen
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

        self.screen.blit(self.surface, self.rect)

#t = Tile(0,10, screen)
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

run = True
while run:
    pos = None
    screen.blit(bgimage, (0,0)) 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #GO BACK TO MENU
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            print(pos)
    if homescreen:
        screen.blit(logo, (GWIDTH//8, GWIDTH//10))
        screen.blit(startbutton, startrect)
        screen.blit(gametitle, gametitlerect)

        if pos and startrect.collidepoint(pos):
            homescreen = False
            gamepage = True

            x = random.randint(0,3)
            t = Tile(x*tilewidth, -tileheight, screen)
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
                t = Tile(x*tilewidth, y, screen)
                tile_group.add(t)
                numtile += 1
                #score+=1

        if gameover: 
            speed = 0
            
    clock.tick(FPS)
    pygame.display.update()