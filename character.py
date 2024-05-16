import pygame

class Character:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image_list = ["frontfacing.png", "backfacing.png", "rightfacing.png", "leftfacing.png"]
    self.image = pygame.image.load(self.image_list[0])
    self.rescale_image(self.image)
    self.image_size = self.image.get_size()
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
    self.delta = 2
    self.front = True

  def rescale_image(self, image):
    self.image_size = self.image.get_size()
    scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
    self.image = pygame.transform.scale(self.image, scale_size)

  def move_direction(self, direction):
     if direction == "right":
         self.x = self.x + self.delta
     if direction == "left":
         self.x = self.x - self.delta
     if direction == "up":
         self.y = self.y - self.delta
     if direction == "down":
         self.y = self.y + self.delta
     self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

  def switch_image(self, direction):
    image_number = 0
    if not self.front and direction == "up":
      image_number = 1
      if not self.front and direction == "right":
        image_number = 2
        if not self.front and direction == " left":
          image_number = 3
    self.image = pygame.image.load(self.image_list[image_number])
    self.rescale_image(self.image)
    self.image_size = self.image.get_size()
    self.front = not self.front
