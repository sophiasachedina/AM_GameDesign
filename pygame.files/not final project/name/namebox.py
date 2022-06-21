#SophiaSachedina
#06/17/22
#get username in pygame
import pygame, sys,os

pygame.init()
os.system('cls')

clock= pygame.time.Clock()
backgrndClr=(255,255,255)
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Get Name")
screen.fill(backgrndClr)
run=True #run the while
username=''
namecolor=(0,105,105)  #text  the name
boxcolor= (200,200,200)  #text b

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)

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
                #run main menu
                pygame.quit()
                sys.exit()
            if event.key==pygame.K_BACKSPACE:
                username=username[:-1]
            else:
                username += event.unicode
        pygame.draw.rect(screen, boxcolor, inputrectangle)
  
        textsurface = MENU_FONT.render(username, True, namecolor)
        screen.blit(textsurface, (inputrectangle.x+5, inputrectangle.y+5))
           
        pygame.display.flip()
        
        #clock.tick(60) means that for every second
        clock.tick(60)
