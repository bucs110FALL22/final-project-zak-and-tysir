import pygame
pygame.init()
Width = 500
Height= 500
screen = pygame.display.set_mode([Width, Height])
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption('Daily News!')

class Button:
  def __init__(self, text, x_pos, y_pos, enabled):
    self.text = text
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.enabled = enabled
    self.draw()

  def draw(self):
    button_text = font.render(self.text, True, "Black")
    button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 25))
    if self.check_click():
      pygame.draw.rect(screen, "dark gray", button_rect, 0, 5)
    else: 
      pygame.draw.rect(screen, "light grey", button_rect, 0, 5)
    pygame.draw.rect(screen, "lightblue", button_rect, 0, 5)
    screen.blit(button_text, (self.x_pos + 3, self.y_pos + 3))

  def check_click(self): 
    mouse_pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 25))
    if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
      return True
    else:
      return False 
    
    



run = True
while run:
  screen.fill("white")
  timer.tick(fps)
  my_button = Button("Weather", 10, 10, True)
  my_button2 = Button("Sports", 10, 40, True)
  my_button3 = Button("Quote of the Day", 10, 70, True)
  my_button4 = Button("Current News", 10, 100, True)
  my_button5 = Button("Fun Fact", 10, 130, True)
  my_button6 = Button("On this day in history", 10, 150, True)
  my_button7 = Button("Stocks", 40, 10, True)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()
  