import pygame # type: ignore
import time 
import random

# Init Pygame
pygame.init()

#Defining colors
white = (255, 255, 255) # White is for Snake 
black = (0, 0, 0) # Black for Background
yellow = (255, 255, 0) # Yellow for the score message
red = (255, 0, 0) # Red for The food
green = (0, 255, 0) # Green for game over

width, height =600, 400 # Setting the dimensions of the game window

# setting up the display of the game window
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")


clock = pygame.time.Clock()


snake_size = 10

snake_speed = 15

message_font = pygame.font.SysFont("ubuntu", 28)
score_font = pygame.font.SysFont("ubuntu",20)

def print_score(score):
    text = score_font.render("Score : " + str(score), True, yellow)
    game_display.blit(text, [0,0])


def draw_snake(snake_size, snake_pixel):
    for pixel in snake_pixel:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])


def run_game():
    game_over = False
    game_close = False

    x = width/2
    y = height/2

    x_speed = 0
    y_speed  = 0

    snake_pixel= []
    snake_length= 1

    target_x= round(random.randrange(0, width-snake_size)/10.0)*10.0
    target_y= round(random.randrange(0, height-snake_size)/10.0)*10.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render('Game Over ! Press 2 to Restart ', True, green)
            game_display.blit(game_over_message, [width/4, height/4])
            print_score(snake_length -1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over= True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                     game_over= True
                     game_close = False



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0 :
            game_close = True
        
        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, red, [target_x, target_y, snake_size, snake_size])
        
        snake_pixel.append([x, y])

        if len(snake_pixel) > snake_length:
            del snake_pixel[0]
        
        for pixel in snake_pixel[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixel)
        print_score(snake_length -1)

        pygame.display.update()

        if x== target_x and y == target_y:
            target_x= round(random.randrange(0, width-snake_size)/10.0)*10
            target_y= round(random.randrange(0, height-snake_size)/10.0)*10
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()






        




