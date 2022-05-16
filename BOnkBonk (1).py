'''
Edward Yang & William Zhao
2018-12-15
BonkBonk.py
our isp game
'''

# import necessities
import pygame, os, sys
import random
from pygame.locals import *

# iniate variables
pygame.init()
print "Enter your username"
pygame.init()
WIDTH = 800
HEIGHT = 600
WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

GRIDSIZE = 10
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
PINK = (255, 102, 128)
WHITE2 = (224, 224, 255)
dark_WHITE = (224, 244, 255)
totalScore = 0

# define the songs in a list
songs = ["PutOnYourSundayClothes.mp3", 'Dreams.mp3', 'WeStayedUpAllNight.mp3', "Masquerade.mp3", "Nevada.mp3",
        "Predawn.mp3", "Grafiore.mp3", "Howling.mp3", "PandorA.mp3", "Phototropic.mp3", "DoubleAgent.mp3"]

# load the background music
pygame.mixer.music.load("DoubleAgent.mp3")


# load the background
def backGround():
   picture = pygame.image.load("Background(1).jpg").convert_alpha()
   picture = pygame.transform.scale(picture, (800, 600))
   gameWindow.blit(picture, (0, 0))


# load the secoond background
def background1():
   gameMenu = pygame.image.load("GameMenu.jpg").convert_alpha()
   gameMenu = pygame.transform.scale(gameMenu, (800, 600))
   gameWindow.blit(gameMenu, (0, 0))


# defining running
running = True


# defining the grid
def grid():
   for x in range(0, WIDTH, 10):
       pygame.draw.line(gameWindow, BLACK, (x, 0), (x, HEIGHT), 1)
   for y in range(0, HEIGHT, 10):
       pygame.draw.line(gameWindow, BLACK, (0, y), (WIDTH, y), 1)
   for x in range(0, WIDTH, 10 * 10):
       pygame.draw.line(gameWindow, BLACK, (x, 0), (x, HEIGHT), 2)
   for y in range(0, HEIGHT, 10 * 10):
       pygame.draw.line(gameWindow, BLACK, (0, y), (WIDTH, y), 2)


# our first screen, user enters user name and select mode
def main():
   global mouseMode, keyboardMode
   # defining varibles
   mouseMode = False
   keyboardMode = False
   backGround()
   font = pygame.font.Font(None, 32)
   clock = pygame.time.Clock()
   input_box = pygame.Rect(460, 230, 400, 54)
   active = False
   main.text = ''
   done = False
   drawRect = False
   drawRect2 = False
   w = 0
   l = 0
   x = 0
   y = 0
   color_inactive = pygame.Color('lightskyblue3')
   color_active = pygame.Color('dodgerblue2')
   color = color_inactive
   mouse = pygame.image.load("Mouse.png").convert_alpha()
   mouse = pygame.transform.scale(mouse, (70, 70))
   keyboard = pygame.image.load("Keyboard.png").convert_alpha()
   keyboard = pygame.transform.scale(keyboard, (150, 100))
   # running the loop
   while not done:
       backGround()
       gameWindow.blit(mouse, (475, 320))
       gameWindow.blit(keyboard, (600, 300))
       mouseX, mouseY = pygame.mouse.get_pos()

       if drawRect == True or drawRect2 == True:
           border = pygame.image.load("Border.png").convert_alpha()
           border = pygame.transform.scale(border, (w, l))
           gameWindow.blit(border, (x, y))
       for event in pygame.event.get():
           if mouseX >= 490 and mouseX <= 530 and mouseY >= 320 and mouseY <= 390:  # switching the mode to mousemode
               w = 250
               l = 430
               x = 385
               y = 170
               drawRect = True
               if event.type == pygame.MOUSEBUTTONDOWN:
                   mouseMode = True
                   keyboardMode = False
                   print "Mouse Mode"
           else:
               drawRect = False
           if mouseX >= 600 and mouseX <= 750 and mouseY >= 330 and mouseY <= 390:  # switching the mode to keyboard
               w = 550
               l = 500
               x = 400
               y = 150
               drawRect2 = True
               if event.type == pygame.MOUSEBUTTONDOWN:
                   keyboardMode = True
                   mouseMode = False
                   print "Keyboard mode"
           else:
               drawRect2 = False

           if event.type == pygame.QUIT:
               done = True
           if event.type == pygame.MOUSEBUTTONDOWN:
               # If the user clicked on the input_box rect.
               if input_box.collidepoint(event.pos):
                   # Toggle the active variable.
                   active = not active
               else:
                   active = False
               # Change the current color of the input box.
               color = color_active if active else color_inactive
           if event.type == pygame.KEYDOWN:
               if active:
                   if event.key == pygame.K_RETURN:
                       print 'Your username has been set to:', main.text
                       done = True
                   elif event.key == pygame.K_BACKSPACE:
                       main.text = main.text[:-1]
                   else:
                       main.text += event.unicode

       # Render the current text.
       txt_surface = font.render(main.text, True, color)
       # Resize the box if the text is too long.
       width = max(300, txt_surface.get_width() + 10)
       input_box.w = width
       # backGround()
       # Blit the text.
       gameWindow.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
       msg(gameWindow, 'BONK BONK', color=(180, 180, 180), size=100, pos=(400, 50))
       msg(gameWindow, 'select keyboard or mouse mode by clicking the icon above this message', color=(RED), size=28,
           pos=(450, 450))
       msg(gameWindow, 'use mouse to click on the box, enter username then press enter', color=(RED), size=28,
           pos=(450, 525))
       # Blit the input_box rect.
       # grid()
       pygame.draw.rect(gameWindow, color, input_box, 2)
       pygame.display.update()
       clock.tick(30)


# redrawing the background when updating
def redrawGameWindow():
   gameWindow.blit(ship, (shipX, shipY))
   '''background = pygame.image.load("BackGround(2).jpg").convert_alpha()
   background = pygame.transform.scale(background, (800, 600))
   gameWindow.blit(background, (0, 0))'''
   pygame.display.update()


# rotating the pendulum image for effects
def rotate(image, angle):
   ORIGINALrect = image.get_rect()
   rotatedImage = pygame.transform.rotate(image, angle)
   rotatedRect = ORIGINALrect.copy()
   rotatedRect.center = rotatedImage.get_rect().center
   rotatedImage = rotatedImage.subsurface(rotatedRect).copy()
   return rotatedImage


# --------------------------------------------------------------#

# --------------------------------------------------------------#

# the main menu, user choooses between the tutorial and gameplay and exit
def mainMenu():
   global tutorials
   tutorials = False
   background2 = pygame.image.load("BackGround(2).jpg").convert_alpha()
   background2 = pygame.transform.scale(background2, (800, 600))
   gameWindow.blit(background2, (0, 0))
   pygame.display.update()
   clock = pygame.time.Clock()
   clock.tick(FPS)
   pygame.event.get()
   keys = pygame.key.get_pressed()
   inPlay = True
   global ship, shipY, shipX, shipAngle
   ORIGINALship = pygame.image.load("Pendulum(2).png").convert_alpha()
   ORIGINALship = pygame.transform.scale(ORIGINALship, (400, 400))
   ship = ORIGINALship.copy()
   shipX = -10
   shipY = 100
   shipAngle = 0
   rotationStep = 4
   active = False
   while inPlay:
       '''redrawGameWindow()
       # gameWindow.blit(backGround, (0, 0))
       clock.tick(FPS)
       pygame.event.get()
       shipAngle = shipAngle + rotationStep
       ship = rotate(ORIGINALship, shipAngle)
       #pygame.display.update()'''
       if keys[pygame.K_ESCAPE]:
           inPlay = False
       for event in pygame.event.get():
           if event.type == pygame.MOUSEBUTTONDOWN and mouseX <= 710 and mouseX >= 390 and mouseY >= 170 and mouseY <= 240: # If user clicks on the play button, function will end; move on to game menu
               transition(800, 600)
               inPlay = False
           if event.type == pygame.MOUSEBUTTONDOWN and mouseX <= 730 and mouseX >= 400 and mouseY >= 260 and mouseY <= 320: # If user clicks on tutorial, function will end; move to tutorial
               tutorials = True
               transition(800, 600)
               inPlay = False
           if event.type == pygame.MOUSEBUTTONDOWN and mouseX <= 710 and mouseX >= 390 and mouseY >= 340 and mouseY <= 410: # If user clicks on exit, function will end; game exits
               transition(800, 600)
               pygame.quit()
       mouseX, mouseY = pygame.mouse.get_pos()
       # grid()


# ---------------------------------------------#
# Shop feature
def shop():
   font = pygame.font.SysFont("Monospaced", 30)    #Setting variables and images
   graphics = font.render("10 Bonkcoins", 1, WHITE)
   graphics1 = font.render("10 Bonkcoins", 1, WHITE)
   graphics2 = font.render("10 Bonkcoins", 1, WHITE)
   graphics3 = font.render("10 Bonkcoins", 1, WHITE)
   graphics4 = font.render("10 Bonkcoins", 1, WHITE)
   graphics5 = font.render("20 Bonkcoins", 1, WHITE)
   shopBackground = pygame.image.load("ShopBackground.jpg").convert_alpha()
   shopBackground = pygame.transform.scale(shopBackground, (800, 600))
   bonkCoins = pygame.image.load("Coins.png").convert_alpha()
   bonkCoins = pygame.transform.scale(bonkCoins, (100, 100))
   backButton = pygame.image.load("BackButton.png").convert_alpha()
   backButton = pygame.transform.scale(backButton, (150, 75))
   inShop = True
   global bonkCoin, totalScore,blue,red,yellow,green,pink
   bonkCoin = totalScore // 10
   while inShop == True: #While in shop blit the background/skins for the tiles. Bonkcoins will be depended on the score of each game, one bonkcoin equals 10 score.
       mouseX, mouseY = pygame.mouse.get_pos()
       gameWindow.blit(shopBackground, (0, 0))
       pygame.draw.rect(gameWindow, BLUE, (50, 100, 200, 100))
       gameWindow.blit(fire,(50,100))
       pygame.draw.rect(gameWindow, RED, (300, 100, 200, 100))
       gameWindow.blit(redPattern,(300,100))
       pygame.draw.rect(gameWindow, YELLOW, (550, 100, 200, 100))
       gameWindow.blit(yellowPattern,(550,100))
       pygame.draw.rect(gameWindow, GREEN, (50, 300, 200, 100))
       gameWindow.blit(greenPattern,(50,300))
       pygame.draw.rect(gameWindow, PINK, (300, 300, 200, 100))
       gameWindow.blit(pinkPattern,(300,300))
       pygame.draw.rect(gameWindow, WHITE2, (550, 300, 200, 120))
       gameWindow.blit(bonkCoins, (600, 0))
       msg(gameWindow, str(bonkCoin), color=(0, 128, 255), size=70, pos=(720, 50))
       gameWindow.blit(graphics, (75, 225))
       gameWindow.blit(graphics1, (325, 225))
       gameWindow.blit(graphics2, (575, 225))
       gameWindow.blit(graphics3, (75, 425))
       gameWindow.blit(graphics4, (325, 425))
       gameWindow.blit(graphics5, (575, 425))
       gameWindow.blit(backButton, (0, 500))
       msg(gameWindow, 'One bonkcoin for every 10 score, click on colors to purchase',
           color=(RED), size=24, pos=(300, 50))
       # grid()
       global r, g, b
       pygame.display.update()
       for event in pygame.event.get():    #Lets the user purchase the skins
           if (event.type == KEYDOWN and event.key == K_ESCAPE):
               inShop = False
               pygame.quit()
           elif event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 0 and mouseX <= 150 and mouseY >= 500 and mouseY <= 570:  # going back
               inshop = False
               return True
           if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 50 and mouseX <= 250 and mouseY >= 100 and mouseY <= 200 and bonkCoin >= 10:  # colors
               bonkCoin -= 10
               totalScore -= 100
               blue, red, yellow, green, pink = False, False, False, False, False
               blue = True
               r, g, b = (0, 0, 255)
           elif event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 300 and mouseX <= 500 and mouseY >= 100 and mouseY <= 200 and bonkCoin >= 10:
               bonkCoin -= 10
               totalScore -= 100
               blue, red, yellow, green, pink = False, False, False, False, False
               red = True
               r, g, b = (255, 0, 0)
           elif event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 550 and mouseX <= 750 and mouseY >= 100 and mouseY <= 200 and bonkCoin >= 10:
               bonkCoin -= 10
               totalScore -= 100
               blue, red, yellow, green, pink = False, False, False, False, False
               yellow = True
               r, g, b = (255, 255, 0)
           elif event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 50 and mouseX <= 250 and mouseY >= 300 and mouseY <= 400 and bonkCoin >= 10:
               bonkCoin -= 10
               totalScore -= 100
               blue, red, yellow, green, pink = False, False, False, False, False
               green = True
               r, g, b = (0, 255, 0)
           elif event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 300 and mouseX <= 500 and mouseY >= 300 and mouseY <= 400 and bonkCoin >= 10:
               bonkCoin -= 10
               totalScore -= 100
               blue, red, yellow, green, pink = False, False, False, False, False
               pink = True
               r, g, b = (255, 102, 128)
           elif event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 550 and mouseX <= 750 and mouseY >= 300 and mouseY <= 400 and bonkCoin >= 10:
               bonkCoin -= 20
               totalScore -= 100
               r, g, b = (224,224,255)

           elif event.type == pygame.MOUSEBUTTONDOWN and bonkCoin < 10:  # when not having
               print "Unable to purchase"

           # ---------------------------------------#


print "Hit ESC to end the program."
clock = pygame.time.Clock()
FPS = 30

#The game menu where the player enters the number of the song to get in to a game
def gameMenu():
   pygame.mixer.music.stop #Setting variables
   background1()
   font = pygame.font.Font(None, 32)
   clock = pygame.time.Clock()
   input_box = pygame.Rect(425, 230, 310, 60)
   color_inactive = pygame.Color('lightskyblue3')
   color_active = pygame.Color('dodgerblue2')
   color = color_inactive
   active = False
   gameMenu.song = ''
   done = False
   true = False
   global openShop
   pygame.init()
   while not done: #Includes all the user input: shop, exit, and text box
       openShop = False
       for event in pygame.event.get():
           mouseX1, mouseY1 = pygame.mouse.get_pos()
           if event.type == pygame.QUIT:
               done = True
           if event.type == pygame.MOUSEBUTTONDOWN and mouseX1 <= 790 and mouseX1 >= 610 and mouseY1 >= 520 and mouseY1 <= 600:
               transition(800, 600)
               done = True
               pygame.quit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               # If the user clicked on the input_box rect.
               if input_box.collidepoint(event.pos):
                   # Toggle the active variable.
                   active = not active
               else:
                   active = False
               # Change the current color of the input box.
               color = color_active if active else color_inactive
           if event.type == pygame.KEYDOWN:
               if active:
                   if event.key == pygame.K_RETURN:
                       done = True
                   elif event.key == pygame.K_BACKSPACE:
                       gameMenu.song = gameMenu.song[:-1]
                   else:
                       gameMenu.song += event.unicode
           elif event.type == pygame.MOUSEBUTTONDOWN and mouseX1 >= 580 and mouseX1 <= 630 and mouseY1 >= 10 and mouseY1 <= 70:
               openShop = True
               if openShop == True:
                   shop()
                   if shop() == True:
                       done = False
                       continue
           else:
               openShop = False

       # Render the current text.
       txt_surface = font.render(gameMenu.song, True, color)
       # Resize the box if the text is too long.
       width = max(270, txt_surface.get_width() + 10)
       input_box.w = width
       background1()
       # Blit the text.
       gameWindow.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
       # Blit the input_box rect.
       pygame.draw.rect(gameWindow, color, input_box, 2)
       msg(gameWindow, 'Click on the box and enter the # of the song that you want', color=(RED), size=28,
           pos=(530, 165))
       # grid()
       pygame.display.update()
       clock.tick(30)


# a transition between screens
def transition(width, height):
   fade = pygame.Surface((width, height))
   fade.fill((0, 0, 0))
   for alpha in range(50):
       fade.set_alpha(alpha)
       gameWindow.blit(fade, (0, 0))
       pygame.display.update()
       pygame.time.delay(10)


# the different screen used for different songs
def MusicScreen():
   # loading the screens
   musicbackground1 = pygame.image.load("MusicBackGround(1).png").convert_alpha()
   musicbackground2 = pygame.image.load("MusicBackGround(2).png").convert_alpha()
   musicbackground3 = pygame.image.load("MusicBackGround(3).png").convert_alpha()
   musicbackground4 = pygame.image.load("MusicBackGround(4).png").convert_alpha()
   musicbackground5 = pygame.image.load("MusicBackGround(5).png").convert_alpha()
   musicbackground6 = pygame.image.load("MusicBackGround(6).png").convert_alpha()
   musicbackground7 = pygame.image.load("MusicBackGround(7).png").convert_alpha()
   musicbackground8 = pygame.image.load("MusicBackGround(8).png").convert_alpha()
   musicbackground9 = pygame.image.load("MusicBackGround(9).png").convert_alpha()
   musicbackground10 = pygame.image.load("MusicBackGround(10).png").convert_alpha()
   musicbackground1 = pygame.transform.scale(musicbackground1, (400, 400))
   musicbackground2 = pygame.transform.scale(musicbackground2, (600, 400))
   musicbackground3 = pygame.transform.scale(musicbackground3, (550, 400))
   musicbackground4 = pygame.transform.scale(musicbackground4, (600, 400))
   musicbackground5 = pygame.transform.scale(musicbackground5, (650, 400))
   musicbackground6 = pygame.transform.scale(musicbackground6, (525, 400))
   musicbackground7 = pygame.transform.scale(musicbackground7, (450, 400))
   musicbackground8 = pygame.transform.scale(musicbackground8, (550, 400))
   musicbackground9 = pygame.transform.scale(musicbackground9, (600, 400))
   musicbackground10 = pygame.transform.scale(musicbackground10, (525, 400))
   running = True
   global speedNum
   speedNum = 4
   drawRect, drawRect2, drawRect3 = False, False, False
   # applying the screens when songs are selected
   while running:
       mouseX, mouseY = pygame.mouse.get_pos()
       background1()
       # ____________________________________________________________________
       # for every song , the screen that you choose the three difficulties
       # ___________________________________________________________________
       if gameMenu.song == "1":
           gameWindow.blit(musicbackground2, (100, 75))
           if drawRect == True or drawRect2 == True or drawRect3 == True:
               box_surface_rect = pygame.Surface((140, 50), pygame.SRCALPHA)
               pygame.draw.rect(box_surface_rect, (255, 255, 255, 90), (0, 0, 80, 50))
               gameWindow.blit(box_surface_rect, (x, y))
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 320 and mouseX <= 490 and mouseY >= 340 and mouseY <= 400:
                   running = False
               if mouseX >= 260 and mouseX <= 350 and mouseY >= 220 and mouseY <= 270:
                   drawRect = True
                   x = 265
                   y = 220
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Easy"
                       speedNum = 2
               else:
                   drawRect = False

               if mouseX >= 370 and mouseX <= 450 and mouseY >= 220 and mouseY <= 270:
                   drawRect2 = True
                   x = 370
                   y = 220
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Normal"
                       speedNum = 4
               else:
                   drawRect2 = False
               if mouseX >= 470 and mouseX <= 550 and mouseY >= 220 and mouseY <= 270:
                   drawRect3 = True
                   x = 470
                   y = 220
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Hard"
                       speedNum = 6
               else:
                   drawRect3 = False
       elif gameMenu.song == "2":
           gameWindow.blit(musicbackground3, (125, 100))
           if drawRect == True or drawRect2 == True or drawRect3 == True:
               box_surface_rect = pygame.Surface((140, 50), pygame.SRCALPHA)
               pygame.draw.rect(box_surface_rect, (255, 255, 255, 90), (0, 0, 80, 50))
               gameWindow.blit(box_surface_rect, (x, y))
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 340 and mouseX <= 460 and mouseY >= 300 and mouseY <= 400:
                   running = False
               if mouseX >= 250 and mouseX <= 330 and mouseY >= 230 and mouseY <= 280:
                   drawRect = True
                   x = 250
                   y = 230
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Easy"
                       speedNum = 2
               else:
                   drawRect = False
               if mouseX >= 360 and mouseX <= 440 and mouseY >= 230 and mouseY <= 280:
                   drawRect2 = True
                   x = 360
                   y = 230
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Normal"
                       speedNum = 4
               else:
                   drawRect2 = False
               if mouseX >= 470 and mouseX <= 550 and mouseY >= 230 and mouseY <= 280:
                   drawRect3 = True
                   x = 470
                   y = 230
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Hard"
                       speedNum = 6
               else:
                   drawRect3 = False

       elif gameMenu.song == "3":
           gameWindow.blit(musicbackground4, (90, 75))
           if drawRect == True or drawRect2 == True or drawRect3 == True:
               box_surface_rect = pygame.Surface((140, 50), pygame.SRCALPHA)
               pygame.draw.rect(box_surface_rect, (255, 255, 255, 90), (0, 0, 90, 40))
               gameWindow.blit(box_surface_rect, (x, y))
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 340 and mouseX <= 450 and mouseY >= 340 and mouseY <= 380:
                   running = False
               if mouseX >= 240 and mouseX <= 330 and mouseY >= 220 and mouseY <= 260:
                   drawRect = True
                   x = 240
                   y = 220
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Easy"
                       speedNum = 2
               else:
                   drawRect = False
               if mouseX >= 350 and mouseX <= 440 and mouseY >= 220 and mouseY <= 260:
                   drawRect2 = True
                   x = 350
                   y = 220
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Normal"
                       speedNum = 4
               else:
                   drawRect2 = False
               if mouseX >= 470 and mouseX <= 550 and mouseY >= 220 and mouseY <= 260:
                   drawRect3 = True
                   x = 470
                   y = 220
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Hard"
                       speedNum = 6
               else:
                   drawRect3 = False
       elif gameMenu.song == "4":
           gameWindow.blit(musicbackground1, (200, 75))
           if drawRect == True or drawRect2 == True or drawRect3 == True:
               box_surface_rect = pygame.Surface((140, 50), pygame.SRCALPHA)
               pygame.draw.rect(box_surface_rect, (255, 255, 255, 90), (0, 0, 90, 50))
               gameWindow.blit(box_surface_rect, (x, y))
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 300 and mouseX <= 500 and mouseY >= 350 and mouseY <= 420:
                   running = False
               if mouseX >= 220 and mouseX <= 310 and mouseY >= 210 and mouseY <= 260:
                   drawRect = True
                   x = 220
                   y = 210
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Easy"
                       speedNum = 2
               else:
                   drawRect = False
               if mouseX >= 350 and mouseX <= 440 and mouseY >= 210 and mouseY <= 260:
                   drawRect2 = True
                   x = 350
                   y = 210
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Normal"
                       speedNum = 4
               else:
                   drawRect2 = False
               if mouseX >= 480 and mouseX <= 570 and mouseY >= 210 and mouseY <= 260:
                   drawRect3 = True
                   x = 480
                   y = 210
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Hard"
                       speedNum = 6
               else:
                   drawRect3 = False
       elif gameMenu.song == "5":
           gameWindow.blit(musicbackground5, (65, 75))
           if drawRect == True or drawRect2 == True or drawRect3 == True:
               box_surface_rect = pygame.Surface((140, 50), pygame.SRCALPHA)
               pygame.draw.rect(box_surface_rect, (255, 255, 255, 90), (0, 0, 85, 40))
               gameWindow.blit(box_surface_rect, (x, y))
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 350 and mouseX <= 450 and mouseY >= 340 and mouseY <= 380:
                   running = False
               if mouseX >= 230 and mouseX <= 310 and mouseY >= 220 and mouseY <= 260:
                   drawRect = True
                   x = 230
                   y = 220
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Easy"
                       speedNum = 2
               else:
                   drawRect = False
               if mouseX >= 360 and mouseX <= 440 and mouseY >= 220 and mouseY <= 260:
                   drawRect2 = True
                   x = 360
                   y = 220
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Normal"
                       speedNum = 4
               else:
                   drawRect2 = False
               if mouseX >= 480 and mouseX <= 560 and mouseY >= 220 and mouseY <= 260:
                   drawRect3 = True
                   x = 480
                   y = 220
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Hard"
                       speedNum = 6
               else:
                   drawRect3 = False
       elif gameMenu.song == "6":
           gameWindow.blit(musicbackground6, (125, 100))
           if drawRect == True or drawRect2 == True or drawRect3 == True:
               box_surface_rect = pygame.Surface((140, 50), pygame.SRCALPHA)
               pygame.draw.rect(box_surface_rect, (255, 255, 255, 90), (0, 0, 100, 47))
               gameWindow.blit(box_surface_rect, (x, y))
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 320 and mouseX <= 460 and mouseY >= 370 and mouseY <= 420:
                   running = False
               if mouseX >= 220 and mouseX <= 320 and mouseY >= 240 and mouseY <= 290:
                   drawRect = True
                   x = 223
                   y = 243
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Easy"
                       speedNum = 2
               else:
                   drawRect = False
               if mouseX >= 340 and mouseX <= 440 and mouseY >= 240 and mouseY <= 290:
                   drawRect2 = True
                   x = 343
                   y = 243
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Normal"
                       speedNum = 4
               else:
                   drawRect2 = False
               if mouseX >= 460 and mouseX <= 560 and mouseY >= 240 and mouseY <= 290:
                   drawRect3 = True
                   x = 463
                   y = 243
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Hard"
                       speedNum = 6
               else:
                   drawRect3 = False
       elif gameMenu.song == "7":
           gameWindow.blit(musicbackground7, (175, 100))
           if drawRect == True or drawRect2 == True or drawRect3 == True:
               box_surface_rect = pygame.Surface((140, 50), pygame.SRCALPHA)
               pygame.draw.rect(box_surface_rect, (255, 255, 255, 90), (0, 0, 90, 50))
               gameWindow.blit(box_surface_rect, (x, y))
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 340 and mouseX <= 460 and mouseY >= 380 and mouseY <= 420:
                   running = False
               if mouseX >= 240 and mouseX <= 330 and mouseY >= 250 and mouseY <= 290:
                   drawRect = True
                   x = 240
                   y = 246
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Easy"
                       speedNum = 2
               else:
                   drawRect = False
               if mouseX >= 350 and mouseX <= 440 and mouseY >= 250 and mouseY <= 290:
                   drawRect2 = True
                   x = 354
                   y = 246
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Normal"
                       speedNum = 4
               else:
                   drawRect2 = False
               if mouseX >= 470 and mouseX <= 550 and mouseY >= 250 and mouseY <= 290:
                   drawRect3 = True
                   x = 466
                   y = 246
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Hard"
                       speedNum = 6
               else:
                   drawRect3 = False

       elif gameMenu.song == "8":
           gameWindow.blit(musicbackground8, (125, 100))
           if drawRect == True or drawRect2 == True or drawRect3 == True:
               box_surface_rect = pygame.Surface((140, 50), pygame.SRCALPHA)
               pygame.draw.rect(box_surface_rect, (255, 255, 255, 90), (0, 0, 90, 50))
               gameWindow.blit(box_surface_rect, (x, y))
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 350 and mouseX <= 460 and mouseY >= 390 and mouseY <= 430:
                   running = False
               if mouseX >= 230 and mouseX <= 320 and mouseY >= 240 and mouseY <= 290:
                   drawRect = True
                   x = 230
                   y = 240
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Easy"
                       speedNum = 2
               else:
                   drawRect = False
               if mouseX >= 350 and mouseX <= 430 and mouseY >= 240 and mouseY <= 290:
                   drawRect2 = True
                   x = 346
                   y = 240
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Normal"
                       speedNum = 4
               else:
                   drawRect2 = False
               if mouseX >= 470 and mouseX <= 550 and mouseY >= 240 and mouseY <= 290:
                   drawRect3 = True
                   x = 466
                   y = 240
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Hard"
                       speedNum = 6
               else:
                   drawRect3 = False
       elif gameMenu.song == "9":
           gameWindow.blit(musicbackground9, (100, 100))
           if drawRect == True or drawRect2 == True or drawRect3 == True:
               box_surface_rect = pygame.Surface((140, 50), pygame.SRCALPHA)
               pygame.draw.rect(box_surface_rect, (255, 255, 255, 90), (0, 0, 95, 50))
               gameWindow.blit(box_surface_rect, (x, y))
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 330 and mouseX <= 460 and mouseY >= 370 and mouseY <= 410:
                   running = False
               if mouseX >= 230 and mouseX <= 320 and mouseY >= 240 and mouseY <= 280:
                   drawRect = True
                   x = 225
                   y = 235
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Easy"
                       speedNum = 2
               else:
                   drawRect = False
               if mouseX >= 340 and mouseX <= 440 and mouseY >= 240 and mouseY <= 280:
                   drawRect2 = True
                   x = 340
                   y = 235
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Normal"
                       speedNum = 4
               else:
                   drawRect2 = False
               if mouseX >= 460 and mouseX <= 550 and mouseY >= 240 and mouseY <= 280:
                   drawRect3 = True
                   x = 460
                   y = 235
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Hard"
                       speedNum = 6
               else:
                   drawRect3 = False
       elif gameMenu.song == "10":
           gameWindow.blit(musicbackground10, (125, 100))
           if drawRect == True or drawRect2 == True or drawRect3 == True:
               box_surface_rect = pygame.Surface((140, 50), pygame.SRCALPHA)
               pygame.draw.rect(box_surface_rect, (255, 255, 255, 90), (0, 0, 90, 50))
               gameWindow.blit(box_surface_rect, (x, y))
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= 330 and mouseX <= 450 and mouseY >= 360 and mouseY <= 390:
                   running = False
               if mouseX >= 220 and mouseX <= 310 and mouseY >= 250 and mouseY <= 300:
                   drawRect = True
                   x = 220
                   y = 250
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Easy"
                       speedNum = 2
               else:
                   drawRect = False
               if mouseX >= 350 and mouseX <= 430 and mouseY >= 250 and mouseY <= 300:
                   drawRect2 = True
                   x = 345
                   y = 250
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Normal"
                       speedNum = 4
               else:
                   drawRect2 = False
               if mouseX >= 450 and mouseX <= 550 and mouseY >= 250 and mouseY <= 300:
                   drawRect3 = True
                   x = 460
                   y = 250
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       print "Hard"
                       speedNum = 6
               else:
                   drawRect3 = False
       # _______________________________________________________
       # _______________________________________________________
       pygame.display.update()


# making a function to make writing messages easier
def msg(screen, text, color=(55, 55, 55), size=36, pos=(-1, -1)):
   if pos[0] == -1: pos = (screen.get_rect().centerx, pos[1])
   if pos[1] == -1: pos = (pos[0], screen.get_rect().centery)
   font = pygame.font.Font(None, size)
   text = font.render(text, 1, color)
   textpos = text.get_rect()
   textpos.centerx = pos[0]
   textpos.centery = pos[1]
   screen.blit(text, textpos)


# variable for color of tiles
r, g, b = 0, 0, 0
blue,red,yellow,green,pink = False,False,False,False,False
fire = pygame.image.load("Fire.png").convert_alpha()
fire = pygame.transform.scale(fire,(200,120))
redPattern = pygame.image.load("Red.png").convert_alpha()
redPattern = pygame.transform.scale(redPattern,(200,120))
yellowPattern = pygame.image.load("YellowPattern.jpg")
yellowPattern = pygame.transform.scale(yellowPattern,(200,120))
greenPattern = pygame.image.load("GreenPattern.jpg").convert_alpha()
greenPattern = pygame.transform.scale(greenPattern,(200,120))
pinkPattern = pygame.image.load("PinkPattern.jpg").convert_alpha()
pinkPattern = pygame.transform.scale(pinkPattern,(200,120))

#class for drawing the tiles
class button():
   x = 0
   y = -HEIGHT // 5
   h = WIDTH // 4 - 1
   l = HEIGHT // 5
   enclick = True

   def pos(self, n):
       self.x = n * WIDTH // 4

   def update(self, screen): #Changes the skin depended on the shop purchase
       if self.enclick and blue:
           pygame.draw.rect(screen, (r, g, b), [self.x, self.y, self.h, self.l])
           gameWindow.blit(fire, [self.x, self.y, self.h, self.l])
       elif self.enclick and red:
           gameWindow.blit(redPattern, [self.x, self.y, self.h, self.l])
       elif self.enclick and yellow:
           pygame.draw.rect(screen, (r, g, b), [self.x, self.y, self.h, self.l])
           gameWindow.blit(yellowPattern, [self.x, self.y, self.h, self.l])
       elif self.enclick and green:
           pygame.draw.rect(screen, (r, g, b), [self.x, self.y, self.h, self.l])
           gameWindow.blit(greenPattern, [self.x, self.y, self.h, self.l])
       elif self.enclick and pink:
           gameWindow.blit(pinkPattern, [self.x, self.y, self.h, self.l])
       elif self.enclick:
           pygame.draw.rect(screen, (r, g, b), [self.x, self.y, self.h, self.l])
       else:
           pygame.draw.rect(screen, (180, 180, 180), [self.x, self.y, self.h, self.l])

   def click(self, ps):
       if ps[0] in range(self.x, self.x + self.h):
           if ps[1] in range(self.y, self.y + self.l):
               self.enclick = False
               return 0
       return 1


totalScore = 0


# Mouse mode
def game():
   pygameQuit = False
   pygame.mixer.music.load(songs[int(gameMenu.song)])
   pygame.mixer.music.play(-1)
   pygame.mixer.music.set_volume(0.5)
   clock = pygame.time.Clock()
   screen = pygame.display.set_mode((WIDTH, HEIGHT))
   ingame = 0
   time = 0
   delt = 60
   block = []
   speed = speedNum
   score = 0
   global bonkCoin, totalScore
   while ingame == 0:
       for i in range(35):
           block.append(button())  # adding to the list
           block[-1].pos(random.randrange(4))  # random generating tiles
           if ingame != 0: break
           for j in range(HEIGHT // (5 * speed) + 1):
               time += 1 / delt
               clock.tick(delt)
               screen.fill((224, 224, 255))
               if ingame != 0: break
               for k in range(len(block)):
                   try:
                       if block[k].y >= 1000:
                           block[k].y = block[k].y
                       else:
                           block[k].y += speed
                       block[k].update(screen)
                       if block[k].y > HEIGHT - block[k].l and block[k].enclick == True:
                           ingame = 1
                   except:
                       pass
               for event in pygame.event.get():
                   if event.type == QUIT or \
                           (event.type == KEYDOWN and event.key == K_ESCAPE):
                       pygameQuit == True
                       pygame.quit()
                   elif event.type == MOUSEBUTTONDOWN:
                       ingame = block[score].click(pygame.mouse.get_pos())
                       score += 1


               if pygameQuit == False:
                   msg(screen, "SCORE " + str(score), color=(0, 128, 255), pos=(-1, 30))
               pygame.draw.line(gameWindow, GREY, (200, 0), (200, 600), 1)
               pygame.draw.line(gameWindow, GREY, (400, 0), (400, 600), 1)
               pygame.draw.line(gameWindow, GREY, (600, 0), (600, 600), 1)
               pygame.draw.line(gameWindow, GREY, (800, 0), (800, 600), 1)
               pygame.display.update()
       if speed <= 9:
           speed += 1

   totalScore += score
   bonkCoin = totalScore // 10
   msg(gameWindow, str(main.text), color=(110, 128, 225), size=75, pos=(400, 200))
   msg(gameWindow, " YOU LOSE ", color=(110, 128, 225), size=100, pos=(-1, -1))
   pygame.mixer.music.stop()
   pygame.mixer.music.load("DoubleAgent.mp3")
   pygame.mixer.music.play(1)
   pygame.mixer.music.set_volume(0.5)
   msg(gameWindow, "SCORE " + str(score - 1), color=(0, 128, 255), pos=(-1, 50))
   pygame.event.get()
   pygame.display.update()
   pygame.time.wait(4000)


bottomBlock = pygame.image.load("BottomBlock.png").convert_alpha()
bottomBlock = pygame.transform.scale(bottomBlock, (195, 120))
font = pygame.font.SysFont("Monospaced", 130)
graphics = font.render("A", 1, WHITE)
graphics1 = font.render("S", 1, WHITE)
graphics2 = font.render("J", 1, WHITE)
graphics3 = font.render("K", 1, WHITE)


def press():
   if (event.type == KEYDOWN and event.key == K_a):
       return 1
   if (event.type == KEYDOWN and event.key == K_s):
       return 2
   if (event.type == KEYDOWN and event.key == K_j):
       return 3
   if (event.type == KEYDOWN and event.key == K_k):
       return 4


score = 0

#Keyboard mode
class button2():
   global score
   x = 0
   y = -HEIGHT // 5
   h = WIDTH // 4 - 1
   l = HEIGHT // 5
   pressed = False
   enpress = True

   def pos2(self, n):
       self.x = n * WIDTH // 4

   def update2(self, screen):

       global score, pressed
       pressed = False
       if self.x == 0 and self.y >= 340 and press() == 1:
           pressed = True
           self.enpress = False
       elif self.x == 200 and self.y >= 340 and press() == 2:
           pressed = True
           self.enpress = False
       elif self.x == 400 and self.y >= 340 and press() == 3:
           pressed = True
           self.enpress = False
       elif self.x == 600 and self.y >= 340 and press() == 4:
           pressed = True
           self.enpress = False
       else:
           health - 10
       if self.enpress and blue:
           pygame.draw.rect(screen, (r, g, b), [self.x, self.y, self.h, self.l])
           gameWindow.blit(fire, [self.x, self.y, self.h, self.l])
       elif self.enpress and red:
           gameWindow.blit(redPattern, [self.x, self.y, self.h, self.l])
       elif self.enpress and yellow:
           pygame.draw.rect(screen, (r, g, b), [self.x, self.y, self.h, self.l])
           gameWindow.blit(yellowPattern, [self.x, self.y, self.h, self.l])
       elif self.enpress and green:
           pygame.draw.rect(screen, (r, g, b), [self.x, self.y, self.h, self.l])
           gameWindow.blit(greenPattern, [self.x, self.y, self.h, self.l])
       elif self.enpress and pink:
           gameWindow.blit(pinkPattern, [self.x, self.y, self.h, self.l])
       elif self.enpress:
           pygame.draw.rect(screen, (r, g, b), [self.x, self.y, self.h, self.l])
       else:
           pygame.draw.rect(screen, (180, 180, 180), [self.x, self.y, self.h, self.l])


# Mouse mode tutorial

def tutorial():
   pygameQuit = False
   pygame.mixer.music.load("DoubleAgent.mp3")
   pygame.mixer.music.play(1)
   pygame.mixer.music.set_volume(0.5)
   clock = pygame.time.Clock()
   screen = pygame.display.set_mode((WIDTH, HEIGHT))
   ingame = 0
   time = 0
   delt = 60
   block = []
   speed = 2
   score = 0
   playAgain = False
   while ingame == 0:
       for i in range(25):
           block.append(button())
           block[-1].pos(random.randrange(4))  # (i)
           if ingame != 0: break
           for j in range(HEIGHT // (5 * speed) + 1):
               time += 1 / delt
               clock.tick(delt)
               screen.fill((224, 224, 255))
               if ingame == 0:
                   msg(screen, "Click on the tiles with the mouse!", color=(0, 128, 255), pos=(-1, 50))
                   msg(screen, "Each Ten tiles clicked will give you one BonkCoin", color=(0, 128, 255), pos=(-1, 100))
               if ingame != 0: break
               for k in range(len(block)):
                   try:
                       block[k].y += speed
                       block[k].update(screen)
                       if block[k].y > HEIGHT - block[k].l and block[k].enclick == True:
                           ingame = 1
                   except:
                       pass
               for event in pygame.event.get():
                   if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                       pygameQuit = True
                       ingame = 1
                       pygame.quit()
                   elif event.type == MOUSEBUTTONDOWN:
                       ingame = block[score].click(pygame.mouse.get_pos())
                       score += 1
               if pygameQuit == False:
                   msg(screen, "SCORE " + str(score), color=(0, 128, 255), pos=(-1, 30))
               pygame.draw.line(gameWindow, GREY, (200, 0), (200, 600), 1)
               pygame.draw.line(gameWindow, GREY, (400, 0), (400, 600), 1)
               pygame.draw.line(gameWindow, GREY, (600, 0), (600, 600), 1)
               pygame.draw.line(gameWindow, GREY, (800, 0), (800, 600), 1)
               pygame.display.update()
       if speed <= 9:
           speed += 1
   if pygameQuit == False:
       msg(screen, "YOU LOSE ", color=(110, 128, 225), size=100, pos=(-1, -1))
   pygame.mixer.music.stop()
   pygame.display.update()
   pygame.time.wait(2000)


count = 0
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
pygame.event.get()
keys = pygame.key.get_pressed()
pygameQuit = False
while running: #Main loop
   if count == 0:
       count = 1
       main()
   while True:
       mainMenu()
       if keyboardMode == True and tutorials:
           score = 0
           healthBar = pygame.image.load("Health.png").convert_alpha()
           healthBar = pygame.transform.scale(healthBar, (50, 50))
           pygame.mixer.music.load("DoubleAgent.mp3")
           pygame.mixer.music.play(1)
           pygame.mixer.music.set_volume(0.5)
           clock = pygame.time.Clock()
           screen = pygame.display.set_mode((WIDTH, HEIGHT))
           time = 0
           delt = 60
           block = []
           speed = 2
           clock = pygame.time.Clock()
           x1 = 200
           y1 = 0
           x2 = 200
           y2 = 600
           global health
           health = 100
           while health != 0:
               for i in range(20):
                   a = random.randrange(4)
                   block.append(button2())
                   block[-1].pos2(a)
                   cnnt = 0
                   cnt = 0
                   if health == 0:
                       break
                   for j in range(HEIGHT // (5 * speed) + 1):
                       time += 1 / delt
                       clock.tick(delt)
                       screen.fill((224, 224, 255))
                       if health >= 0:
                           msg(screen, "Use A,S,J,K on the keyboard to match the tiles!", color=(0, 128, 255),
                               pos=(-1, 50))
                           msg(screen, "Each Ten tiles clicked will give you one BonkCoin", color=(0, 128, 255),
                               pos=(-1, 100))
                       if health == 0:
                           break
                       for k in range(len(block)):
                           try:
                               if block[k].y >= 1000:
                                   block[k].y = block[k].y
                               else:
                                   block[k].y += speed
                               block[k].update2(screen)
                               if pressed == True and cnnt == 0:  # giving the user score and only letting them get one score per press
                                   score += 1
                                   cnnt += 1
                               if block[k].y > HEIGHT - block[k].l and block[k].enpress == True and cnt == 0:
                                   cnt += 1
                                   health -= 10
                                   # print health
                           except:
                               pass
                       for event in pygame.event.get():
                           if (event.type == KEYDOWN and event.key == K_ESCAPE):
                               pygameQuit = True
                               pygame.quit()

                       if pygameQuit == False:
                           msg(screen, "SCORE " + str(score), color=(0, 128, 255), pos=(-1, 30))
                       pygame.draw.line(gameWindow, GREY, (200, 0), (200, 600), 1)
                       pygame.draw.line(gameWindow, GREY, (400, 0), (400, 600), 1)
                       pygame.draw.line(gameWindow, GREY, (600, 0), (600, 600), 1)
                       pygame.draw.line(gameWindow, GREY, (800, 0), (800, 600), 1)
                       gameWindow.blit(bottomBlock, (0, 460))
                       gameWindow.blit(bottomBlock, (200, 460))
                       gameWindow.blit(bottomBlock, (400, 460))
                       gameWindow.blit(bottomBlock, (600, 460))
                       gameWindow.blit(graphics, (60, 480))
                       gameWindow.blit(graphics1, (260, 480))
                       gameWindow.blit(graphics2, (460, 480))
                       gameWindow.blit(graphics3, (660, 480))
                       pygame.draw.rect(gameWindow, RED, (635, 20, health, 10))
                       gameWindow.blit(healthBar, (600, 0))
                       pygame.display.update()
               speed += 1

           if pygameQuit == False:
               msg(screen, "YOU LOSE ", color=(110, 128, 225), size=100, pos=(-1, -1))
           pygame.time.wait(4000)
           pygame.display.update()

       elif mouseMode == True and tutorials:
           tutorial()
       gameMenu()
       MusicScreen()
       transition(800, 600)

       if mouseMode == True:
           game()
       elif keyboardMode == True:
           score = 0
           healthBar = pygame.image.load("Health.png")
           healthBar = pygame.transform.scale(healthBar, (50, 50))
           pygameQuit = False
           pygame.mixer.music.load(songs[int(gameMenu.song)])
           pygame.mixer.music.play(-1)
           pygame.mixer.music.set_volume(0.5)
           clock = pygame.time.Clock()
           screen = pygame.display.set_mode((WIDTH, HEIGHT))
           time = 0
           delt = 60
           block = []
           speed = speedNum
           clock = pygame.time.Clock()
           x1 = 200
           y1 = 0
           x2 = 200
           y2 = 600
           health = 100
           while health != 0:

               for i in range(20):
                   a = random.randrange(4)
                   block.append(button2())
                   block[-1].pos2(a)
                   cnnt = 0  # variables so that later the score or health would only be deducted once per missed block
                   cnt = 0
                   if health == 0:
                       break
                   for j in range(HEIGHT // (5 * speed) + 1):
                       time += 1 / delt
                       clock.tick(delt)
                       screen.fill((224, 224, 255))
                       if health == 0:
                           totalScore += score
                           bonkCoin = totalScore // 10
                           break
                       for k in range(len(block)):
                           try:
                               if block[k].y >= 1000:
                                   block[k].y = block[k].y
                               else:
                                   block[k].y += speed
                               block[k].update2(screen)

                               if pressed == True and cnnt == 0:  # giving the user score and only letting them get one score per press
                                   score += 1
                                   cnnt += 1
                               if block[k].y > HEIGHT - block[k].l and block[k].enpress == True and cnt == 0:
                                   cnt += 1
                                   health -= 10
                                   print health
                           except:
                               pass
                       for event in pygame.event.get():
                           if (event.type == KEYDOWN and event.key == K_ESCAPE):
                               pygame.quit()
                               pygameQuit = True

                       if pygameQuit == False:
                           msg(screen, "SCORE " + str(score), color=(0, 128, 255), pos=(-1, 30))
                       pygame.draw.line(gameWindow, GREY, (200, 0), (200, 600), 1)
                       pygame.draw.line(gameWindow, GREY, (400, 0), (400, 600), 1)
                       pygame.draw.line(gameWindow, GREY, (600, 0), (600, 600), 1)
                       pygame.draw.line(gameWindow, GREY, (800, 0), (800, 600), 1)
                       gameWindow.blit(bottomBlock, (0, 460))
                       gameWindow.blit(bottomBlock, (200, 460))
                       gameWindow.blit(bottomBlock, (400, 460))
                       gameWindow.blit(bottomBlock, (600, 460))
                       gameWindow.blit(graphics, (60, 480))
                       gameWindow.blit(graphics1, (260, 480))
                       gameWindow.blit(graphics2, (460, 480))
                       gameWindow.blit(graphics3, (660, 480))
                       pygame.draw.rect(gameWindow, RED, (635, 20, health, 10))
                       gameWindow.blit(healthBar, (600, 0))
                       pygame.display.update()
               speed += 1
           if pygameQuit == False:
               msg(screen, "YOU LOSE ", color=(110, 128, 225), size=100, pos=(-1, -1))
               pygame.mixer.music.stop()
               pygame.mixer.music.load("DoubleAgent.mp3")
               pygame.mixer.music.play(1)
               pygame.mixer.music.set_volume(0.5)
               msg(screen, str(main.text) + ' ', color=(110, 128, 225), size=100, pos=(400, 200))
               msg(screen, "Your score is " + str(score), color=(110, 128, 225), size=50, pos=(400, 50))
           pygame.display.update()
           pygame.time.wait(4000)
   pygame.event.get()
   keys = pygame.key.get_pressed()
   if keys[pygame.K_ESCAPE]:
       running = False
   pygame.display.update()

pygame.quit()
