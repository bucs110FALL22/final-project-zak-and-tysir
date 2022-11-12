import pygame 

class Weapon(pygame.sprite.Sprite): 
  def __init__(self, x, y, width, height):
    super().__init__()
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.image.load = ("sword.png")
    self.image.get_rect()
    self.speed = 10



    


