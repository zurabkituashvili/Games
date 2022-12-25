#[background image, bird image, image for pipes, end screen, replay, music, start]

import random
import pygame
from pygame import *



class App:
    
    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None
        self.posX = 0
        self.posX1 = 0
        self.backgroundSpeed = 10
        self.pipePosY = 10 * (random.randint(14, 56))
        self.pipePosX = 1480
        self.flapperY = 350
        self.jump = False
        self.start = False
        self.counter = 0
        self.floatY = 350
        self.collide = False
        self.hitboxes = False
        self.drawScore = False
        self.flapperX = 150
        self.loosingScreen = False

 

    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        self.cleanUp()


    def init(self):
        self.screen = pygame.display.set_mode((1480, 700))
        icon=pygame.image.load("download.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("FLAPPIEST BIRDIE")
        mixer.init()
        backgoundMusic = mixer.Sound("muzika.wav")
        backgoundMusic.play(-1)
        pygame.font.init()        


 
        self.clock = pygame.time.Clock()
        self.running = True

    def update(self):
        self.events()
        if self.start:
            self.posX -= self.backgroundSpeed
            self.posX1 += self.backgroundSpeed
            self.pipePosX -= self.backgroundSpeed


        if self.posX < -1480:
            self.posX = 0

        if self.posX1 > 1480:
            self.posX1 = 0



        if self.pipePosX < -180:
            self.pipePosY = 10 * (random.randint(14, 56))

        if self.pipePosX < -180:
            self.pipePosX = 1480

        if self.pipePosX == 10:
            self.counter += 1

        if self.flapperY > 700:
            self.loosingScreen = True   

        if self.flapperY < 0:
            self.loosingScreen = True



        if self.collide:
            self.loosingScreen = True
        
        if self.counter == 10:
            self.pipePosX = 1480
            self.flapperX += 10
            self.flapperY = 350
            self.backgroundSpeed = 0
            if self.flapperX > 1480:
                self.loosingScreen = True


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        jumpSound = mixer.Sound("fart.wav")
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]: 
            if self.start:
                jumpSound.play() 
                self.jump = True
                self.flapperY -= 8
        
        else:
            if self.start:
                self.jump = False
                self.flapperY += 8

        if keys[pygame.K_DOWN] and self.start:
            self.flapperY += 8

        if keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]:
            self.start = True

        if not self.start:
            self.floatY -= 4.5
            if self.floatY < 200:
                self.floatY = 350

        if pygame.key.get_pressed()[pygame.K_F1]:
            self.hitboxes = True

        if pygame.key.get_pressed()[pygame.K_F2]:
            self.hitboxes = False

        if self.loosingScreen:
            if keys[pygame.K_BACKSPACE]:
                self.running = False

                
            #if enter is pressed start again
            if keys[pygame.K_RETURN]:
                self.loosingScreen = False
                self.collide = False
                self.start = False
                self.counter = 0
                self.flapperX = 150
                self.flapperY = 350
                self.backgroundSpeed = 10
                self.pipePosX = 1480
                self.pipePosY = 10 * (random.randint(14, 56))



            
    def render(self):

        #MAKE PIPES
        pipe = pygame.image.load("pipe.png")
        pipe1 = pygame.image.load("pipe1.png")
        pipe = pygame.transform.scale(pipe, (300, 600))
        pipe1 = pygame.transform.scale(pipe1, (300, 600))

        weight, height = pipe.get_rect().size
        weight1, height1 = pipe1.get_rect().size



        #Collision
        if self.start:
            pipee1 = pygame.Rect(self.pipePosX+110, ((self.pipePosY - height/2) + 400), 80, 600)
            pygame.draw.rect(self.screen, (255, 0, 0), pipee1, 1)

            pipee2 = pygame.Rect(self.pipePosX+110, ((self.pipePosY - height1/2) - 400), 80, 600)
            pygame.draw.rect(self.screen, (255, 0, 0), pipee2, 1)

            flapperr = pygame.Rect(150, self.flapperY, 80, 80)
            pygame.draw.rect(self.screen, (255, 0, 0), flapperr, 1)

            if flapperr.colliderect(pipee1) or flapperr.colliderect(pipee2):
                self.collide = True


        #Draw Background
        background = pygame.image.load("background.jpg")
        background = pygame.transform.scale(background, (1480, 700))
        self.screen.blit(background, (self.posX, 0))
        self.screen.blit(background, (1480-self.posX1, 0))


        #Draw flapper
        flapper = pygame.image.load("notjump.png")
        flapper = pygame.transform.scale(flapper, (80, 80))
        flapperjumper = pygame.image.load("jump.png")
        flapperjumper = pygame.transform.scale(flapperjumper, (80, 80))

        if not self.jump:
            self.screen.blit(flapper, (self.flapperX, self.flapperY))

        else:
            self.screen.blit(flapperjumper, (self.flapperX, self.flapperY))

        if self.start:
            #Create Pipes
            self.screen.blit(pipe, (self.pipePosX, ((self.pipePosY - height/2) + 390)))
            self.screen.blit(pipe1, (self.pipePosX, ((self.pipePosY - height1/2) - 390)))



        if self.hitboxes:
        #draw hitboxes
            pipee1 = pygame.Rect(self.pipePosX+110, ((self.pipePosY - height/2) + 400), 80, 600)
            pygame.draw.rect(self.screen, (255, 0, 0), pipee1, 1)

            pipee2 = pygame.Rect(self.pipePosX+110, ((self.pipePosY - height1/2) - 400), 80, 600)
            pygame.draw.rect(self.screen, (255, 0, 0), pipee2, 1)

            flapperr = pygame.Rect(150, self.flapperY, 80, 80)
            pygame.draw.rect(self.screen, (255, 0, 0), flapperr, 1)



        #Draw Intro
        if not self.start:
            floating = pygame.image.load("floating.png")
            floating = pygame.transform.scale(floating, (700, 300))
            self.screen.blit(floating, (420, self.floatY)) 

        #Draw ScoreBoard
        font_style = pygame.font.SysFont("bahnschrift", 50)
        msg = ("Score: " + str(self.counter))
        mesg = font_style.render(msg, True, (255, 255, 0))
        self.screen.blit(mesg, [1250, 10])


        if self.loosingScreen:
            loosingScreen = pygame.image.load("loosingScreen.jpg")
            loosingScreen = pygame.transform.scale(loosingScreen, (1480, 1000))
            self.screen.blit(loosingScreen, (0, -200))


        pygame.display.flip()
        self.clock.tick(60)

        


    def cleanUp(self):
        pygame.quit()
        quit()

if __name__ == "__main__":
    app = App()
    app.run()