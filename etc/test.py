import pygame

width = 800
height = 600
color_bg = (
    0,
    0,
    0,
)
color_text = (200, 200, 200)
button_clicked = False
running = True

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Morning Breif!")

weather = pygame.image.load('weather2.png')
stocks = pygame.image.load('stocks2.png')
quote = pygame.image.load('quote_image.png')
news = pygame.image.load('news2.png')

screen.blit(weather, (0, 0))
screen.blit(stocks, (0, 175))
screen.blit(quote, (300, 140))
screen.blit(news, (300, 0))

pygame.display.flip()

status = True
while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

pygame.quit()
