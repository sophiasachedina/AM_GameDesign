#SophiaSachedina
#06/17/22
#get username in pygame

import pygame, sys, os

pygame.init()
os.system("cls")

clock = pygame.time.Clock()
background = (255,255,255)
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Get Name")
screen.fill(background)
run = True #to run the while loop
username = ""
namecolor = (0, 105, 105) #tect of the name
boxcolor = (200, 200, 200) #text box

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)

title = TITLE_FONT.render("Enter Name", 1, namecolor)
screen.blit(title, (250, 50))
#make box
while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #drawbox
            print()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RETURN:
                print("name is in")
            if event == pygame.K_BACKSPACE:
                print("username == username[:-1}")
            else:
                print("username += event.unicode")
