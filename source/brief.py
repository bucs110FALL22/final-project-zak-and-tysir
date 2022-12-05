import pygame
from source.weather import Weather
from source.news import News
from source.quotes import Quotes
from source.jokes import Jokes


class main():

  def morning_brief(self):
    pygame.init()
    Width = 600
    Height = 400
    CANVAS = (Width, Height)
    screen = pygame.display.set_mode([Width, Height])
    fps = 60
    timer = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Morning Brief!')
    was_button_clicked = False

    #  import
    run = True
    

    weather_image = pygame.image.load('assets/weather2.png')
    weather_image = pygame.transform.scale(weather_image, (290, 150))

    quotes_image = pygame.image.load('assets/quote_image.png')
    quotes_image = pygame.transform.scale(quotes_image, (290, 143))

    news_image = pygame.image.load('assets/news2.png')
    news_image = pygame.transform.scale(news_image, (290, 150))

    joke_image = pygame.image.load('assets/joke.png')
    joke_image = pygame.transform.scale(joke_image, (290, 142))

    #Scrolling Text
    st_messages = ['  Good Morning   ']
    FONT_COLOR = (255, 0, 255)
    st_message = '  '
    st_font = pygame.font.SysFont("arial", 32)
    st_surface = st_font.render(st_message, True, FONT_COLOR)
    x = 0
    y = (CANVAS[1] - st_surface.get_height()) - (CANVAS[1] * .05)
    messages_indx = -1
    while run:
      screen.fill("white")
      timer.tick(fps)
      # Draw Images
      screen.blit(weather_image, (300, 0))
      weather_rect = weather_image.get_rect(topleft=(300, 0))

      screen.blit(news_image, (0, 0))
      news_rect = news_image.get_rect(topleft=(0, 0))

      screen.blit(quotes_image, (300, 160))
      quote_rect = quotes_image.get_rect(topleft=(300, 160))

      screen.blit(joke_image, (0, 160))
      joke_rect = joke_image.get_rect(topleft=(0, 160))

      #screen.blit(weather_image, weather_rect)
      for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
          run = False
        if event.type == pygame.MOUSEBUTTONDOWN:

          if weather_rect.collidepoint(event.pos):
            FONT_COLOR = (55, 55, 55)
            messages_indx = 0
            st_surface = st_font.render("  LOADING WEATHER          ", True,
                                        FONT_COLOR)

            weather = Weather()
            st_messages = weather.get_alerts()
            messages_indx = -1

          elif news_rect.collidepoint(event.pos):
            FONT_COLOR = (15, 0, 155)
            messages_indx = 0
            st_surface = st_font.render("  LOADING NEWS          ", True,
                                        FONT_COLOR)
            news = News()
            st_messages = news.get_articles()

          elif joke_rect.collidepoint(event.pos):
            FONT_COLOR = (255, 0, 255)
            messages_indx = 0
            st_surface = st_font.render("  LOADING JOKE          ", True,
                                        FONT_COLOR)
            joke = Jokes()
            st_messages = joke.get_joke()
            messages_indx = -1

          elif quote_rect.collidepoint(event.pos):
            FONT_COLOR = (255, 0, 255)
            st_surface = st_font.render("  LOADING QUOTE          ", True,
                                        FONT_COLOR)
            q = Quotes()
            my_quote = q.get_quote()
            st_messages = []
            st_messages.append(my_quote)
            messages_indx = -1

          
      #Text Scroller
      x -= 2
      if x < -st_surface.get_width():
        x = CANVAS[0]
        messages_indx += 1
        if messages_indx > len(st_messages) - 1:
          messages_indx = 0
        st_surface = st_font.render(st_messages[messages_indx], True,
                                    FONT_COLOR)

      screen.blit(st_surface, (x, y))
      pygame.display.update()
      pygame.display.flip()

    pygame.quit()
