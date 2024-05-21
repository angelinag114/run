import pygame
from character import Character

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times', 20)
pygame.display.set_caption("  What happened?")

size = (800, 600)
screen = pygame.display.set_mode(size)
transparent = (0, 0, 0, 0)
background = pygame.image.load("map.png")

c=  Character(20,240)

welcome = my_font.render("What happened in this abandoned city?", True,
                         (255, 255, 255))
start = my_font.render("Press space to start.", True, (255, 255, 255))

keys = pygame.key.get_pressed()
screen.blit(background, (0, 0))
screen.blit(welcome, (200, 230))
screen.blit(start, (300, 250))
run = True
game_start = False
while run:
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE]:
    screen.blit(background, (0, 0))
  if keys[pygame.K_d]:
      c.move_direction("right")
  if keys[pygame.K_a]:
      c.move_direction("left")
  if keys[pygame.K_w]:
      c.move_direction("up")
  if keys[pygame.K_s]:
      c.move_direction("down")

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      game_start = False
    if event.type == pygame.MOUSEBUTTONUP:
      game_start = True

    if game_start == True:
      screen.blit(c.image, c.rect)
    pygame.display.update()

pygame.quit()
