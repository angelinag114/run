import pygame

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times', 20)
pygame.display.set_caption("  What happened?")

size = (800, 600)
screen = pygame.display.set_mode(size)

background = pygame.image.load("map.png")

welcome = my_font.render("What happened in this abandoned city?", True, (255, 255, 255))
start = my_font.render("Press space to start.", True, (255, 255, 255))

keys = pygame.key.get_pressed()
screen.blit(background, (0, 0))
screen.blit(welcome, (200, 230))
screen.blit(start, (300, 250))
run = True
# while run:
#   keys = pygame.key.get_pressed()
#   if keys[pygame.K_SPACE]:




pygame.display.update()


