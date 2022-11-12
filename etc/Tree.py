import pygame

class Tree(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height):
    super().__init__()
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.image = pygame.image.load("tree.png")
    self.rect = self.image.get_rect()
  

  
    