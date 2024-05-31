import pygame
from character import Character
from stranger import Stranger

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times', 20)
pygame.display.set_caption("  What happened?")

size = (800, 600)
screen = pygame.display.set_mode(size)
background = pygame.image.load("map.png")

c = Character(20,240)
s = Stranger(725,20)

welcome = my_font.render("Explore the abandoned city!", True,
                         (255, 255, 255))
start = my_font.render("Press space to start.", True, (255, 255, 255))

run = True
game_start = False

while run:
  
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE]:
    game_start = True
  if keys[pygame.K_d]:
    c.move_direction("right")
  if keys[pygame.K_a]:
    c.move_direction("left")
  if keys[pygame.K_s]:
    c.move_direction("down")
  if keys[pygame.K_w]:
    c.move_direction("up")
    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
      

  if game_start:
    screen.blit(background, (0, 0))
    screen.blit(c.image, c.rect)
    screen.blit(s.image, s. rect)
    
  if game_start == False:
    screen.blit(background, (0, 0))
    screen.blit(welcome, (265, 230))
    screen.blit(start, (300, 250))

   

  pygame.display.update()

pygame.quit()

   

  pygame.display.update()

pygame.quit()
