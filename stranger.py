import pygame

class Stranger:


  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = pygame.image.load("stranger.png")
    self.rescale_image(self.image)
    self.image_size = self.image.get_size()
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
    self.delta =  2
    self.front = True

  def rescale_image(self, image):
    self.image_size = self.image.get_size()
    scale_size = (self.image_size[0] * .3, self.image_size[1] * .3)
    self.image = pygame.transform.scale(self.image, scale_size)
