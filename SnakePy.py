import pygame
import time
import random

pygame.init()

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width,dis_height)) #dis = display e tamanho do display
#pygame.display.update()
pygame.display.set_caption('Jogo da cobrinha na cobrinha, João Pedro de Rossi')

blue = (0,0,255) #RGB 
lightBlue = (51,204,255)  
red = (255,0,0) #RGB
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
green = (0,128,0)

snakeSize = 20

font_style = pygame.font.SysFont("timesnewsroman",25)
score_font = pygame.font.SysFont("comicsansms", 30)

def Player_score(score):
    value = score_font.render("Your Score is: "+ str(score), True,green)
    dis.blit(value, [0,0])

def our_snake(snakeSize,snake_List):
    for x in snake_List:
        pygame.draw.rect(dis,red,[x[0],x[1], snakeSize, snakeSize])

def message(msg,color):
    mesg = font_style.render(msg, True,color)
    dis.blit(mesg,[dis_width/6, dis_height/3])


def gameLoop():
    game_over = False
    game_close = False

    foodX = round(random.randrange(0,dis_width - snakeSize+5)/10.0)*10.0
    foodY = round(random.randrange(0,dis_height - snakeSize+5)/10.0)*10.0

    foodZ = round(random.randrange(0,dis_width - snakeSize+5)/10.0)*10.0
    foodW = round(random.randrange(0,dis_height - snakeSize+5)/10.0)*10.0

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    #foodCount = 0
    snakeSpeed = 20
    

    clock = pygame.time.Clock()

    while not game_over:
        
        while game_close == True:
            dis.fill(lightBlue)
            message("Game over! Aperte R para jogar novamente, Q para fechar.", black)
            Player_score(Length_of_snake -1)

            pygame.display.update()

            for event in pygame.event.get():
                #print (event) perfect for debugging
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != 10:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -10:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != 10:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN and y1_change != -10:
                    x1_change = 0
                    y1_change = 10
        #scrolling across the screen when reaching the screen maximum size
        if x1 >= dis_width:
            x1 = 0
        elif x1<= 0:
            x1 = dis_width
        elif y1 <= 0:
            y1 = dis_height
        elif y1 >= dis_height:
            y1 = 0


        x1+= x1_change
        y1+= y1_change
        
        dis.fill(white)
        #pygame.draw.rect(dis,red,[x1,y1,snakeSize,snakeSize])
        pygame.draw.rect(dis,blue,[foodX,foodY,snakeSize,snakeSize])
        pygame.draw.rect(dis,green,[foodZ,foodW,snakeSize,snakeSize])
        
        

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snakeSize, snake_List)
        Player_score(Length_of_snake -1)

        pygame.display.update()

        if x1 == foodX and y1 == foodY:
            foodX = round(random.randrange(0,dis_width - snakeSize)/10.0)*10.0
            foodY = round(random.randrange(0,dis_height - snakeSize)/10.0)*10.0

            Length_of_snake +=1

            if snakeSpeed <39:
                snakeSpeed +=1

            print("Yummy!")
            print('Speed =',snakeSpeed)

        if x1 == foodZ and y1 == foodW:
            foodZ = round(random.randrange(0,dis_width - snakeSize)/10.0)*10.0
            foodW = round(random.randrange(0,dis_height - snakeSize)/10.0)*10.0

            Length_of_snake +=1

            if snakeSpeed<39:
                snakeSpeed +=1

            print("Yummy!")
            print('Speed =',snakeSpeed)

        clock.tick(snakeSpeed) #update speed
        

    pygame.quit()
    quit()

gameLoop()