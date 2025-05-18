import pygame
import time
import random

pygame.init()

# Screen dimensions
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
dark_green = (0, 100, 0)
light_green = (0, 155, 0)
snake_color = (0, 0, 255)
food_color = (213, 50, 80)
white = (255, 255, 255)

# Snake settings
block_size = 20
snake_speed = 10

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def draw_checkered_background():
    for row in range(0, height // block_size):
        for col in range(0, width // block_size):
            color = light_green if (row + col) % 2 == 0 else dark_green
            pygame.draw.rect(win, color, [col * block_size, row * block_size, block_size, block_size])

def score_display(score):
    value = font.render("Score: " + str(score), True, white)
    win.blit(value, [0, 0])

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(win, snake_color, [x[0], x[1], block_size, block_size])

def game_loop():
    game_over = False
    game_close = False

    x1 = width // 2
    y1 = height // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:
        while game_close:
            win.fill((0, 0, 0))
            msg = font.render("You Lost! Press Q-Quit or C-Play Again", True, food_color)
            win.blit(msg, [width / 6, height / 3])
            score_display(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        draw_checkered_background()
        pygame.draw.rect(win, food_color, [foodx, foody, block_size, block_size])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_list)
        score_display(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
