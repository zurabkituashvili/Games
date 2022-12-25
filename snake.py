#[Menu line, Score, End screen, Replay, Background]  

import pygame
import random

class App:
    
    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None
        self.posX = 375
        self.posY = 325
        self.moveX = 0
        self.moveY = 0
        self.loosingScreen = False
        self.foodX = 10 * (random.randint(1, 75))
        self.foodY = 10 * (random.randint(4, 65))
        self.snakeLength = 5
        self.counter = 0
        self.head = [375, 325]
        self.snakeList = [self.head, [350, 325], [325, 325], [300, 325], [275, 325]]
        self.start = True
        self.dir = 5

    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        self.cleanUp()

    def init(self):
        self.screen = pygame.display.set_mode((800, 700))
        pygame.display.set_caption("SSSNAKE")
        pygame.font.init()

        self.clock = pygame.time.Clock()
        self.running = True
        

    def update(self):
        self.events()
        if self.posX < 0:
            self.loosingScreen = True
        if self.posX > 800:
            self.loosingScreen = True
        if self.posY < 30:
            self.loosingScreen = True
        if self.posY > 700:
            self.loosingScreen = True


    def events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.start:
                self.moveX = 10
                self.start = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.dir != 2:
                    self.moveX = -10
                    self.moveY = 0
                    self.dir = 1
                elif event.key == pygame.K_RIGHT and self.dir != 1:
                    self.moveX = 10
                    self.moveY = 0
                    self.dir = 2
                elif event.key == pygame.K_UP and self.dir != 4:
                    self.moveY = -10
                    self.moveX = 0
                    self.dir = 3
                elif event.key == pygame.K_DOWN and self.dir != 3:
                    self.moveY = 10
                    self.moveX = 0
                    self.dir = 4

        self.posX += self.moveX 
        self.posY += self.moveY

        if self.loosingScreen:
            #if backspace is pressed game will end
            if keys[pygame.K_BACKSPACE]:
                self.running = False

            #if enter is pressed start again
            if keys[pygame.K_RETURN]:
                self.loosingScreen = False
                self.posX = 375
                self.posY = 325
                self.moveX = 0
                self.moveY = 0
                self.snakeLength = 5
                self.counter = 0
                self.head = [375, 325]
                self.snakeList = [self.head, [350, 325], [325, 325], [300, 325], [275, 325]]
                self.dir = 5
                self.start = True





    def render(self):
        if not self.loosingScreen:
            snakeBackground = pygame.image.load("snakeBackground.jpg")
            snakeBackground = pygame.transform.scale(snakeBackground, (900, 700))
            self.screen.blit(snakeBackground, (0, 0))
            pygame.draw.rect(self.screen, (255, 0, 0), (0, 0, 800, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, 800, 700), 1)
                        
        
            #draw random food
            food = pygame.Rect(self.foodX, self.foodY, 10, 10)
            pygame.draw.rect(self.screen, (225, 255, 0), food)


            snakeHead = []
            snakeHead.append(self.posX)
            snakeHead.append(self.posY)
            self.snakeList.append(snakeHead)

            if len(self.snakeList) > self.snakeLength:
                del self.snakeList[0]

            for body in self.snakeList:
                snake = pygame.Rect(body[0], body[1], 10, 10)
                pygame.draw.rect(self.screen, (0, 225, 255), snake)

            if self.counter >= 1:
                for x in self.snakeList[:-1]:
                    if x == snakeHead:
                        self.loosingScreen = True



                
           #collision
            if snake.colliderect(food):
                self.foodX = 10 * (random.randint(1, 75))
                self.foodY = 10 * (random.randint(4, 65))
                self.snakeLength += 1
                self.counter+=1


            

        #Draw ScoreBoard
        font_style = pygame.font.SysFont("bahnschrift", 20)
        msg = ("Score: " + str(self.counter))
        mesg = font_style.render(msg, True, (255, 255, 0))
        self.screen.blit(mesg, [700, 5])


        if self.loosingScreen:
            loosingScreen = pygame.image.load("loosingScreen.jpg")
            loosingScreen = pygame.transform.scale(loosingScreen, (800, 700))
            self.screen.blit(loosingScreen, (0, 0))


        pygame.display.flip()
        self.clock.tick(15)

    def cleanUp(self):
        pass

if __name__ == "__main__":
    app = App()
    app.run()