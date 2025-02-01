import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
ScreenWidth = 1000
ScreenHeight = 600

# Create window
gamewindow = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("My Snake Game")
pygame.display.update()

#background image
bgimg=pygame.image.load("wp2409705.jpg")
bgimg=pygame.transform.scale(bgimg,(1000,600)).convert_alpha()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue= (0, 0, 255)

# Game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# Functions
def text_screen(text, color, x, y):
    """Displays text on the game screen."""
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

def plot_snake(gamewindow, color, snk_list, snk_size):
    """Plots the snake on the screen."""
    for x, y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snk_size, snk_size])

def game_loop():
    # Game variables
    exitGame = False
    gameOver = False
    snake_x = 45
    snake_y = 55
    food_x = random.randint(20, ScreenWidth - 20)
    food_y = random.randint(20, ScreenHeight - 20)
    snake_size = 20
    vel_x = 0
    vel_y = 0
    score = 0
    init_velocity = 5
    fps = 30

    snk_list = []
    snk_length = 1

    while not exitGame:
        if gameOver:
            gamewindow.fill(white)
            text_screen("Game Over! Press Enter to Restart", red, 200, 250)
            text_screen(f"Your Score: {score * 10}", black, 350, 300)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x = init_velocity
                        vel_y = 0
                    if event.key == pygame.K_LEFT:
                        vel_x = -init_velocity
                        vel_y = 0
                    if event.key == pygame.K_DOWN:
                        vel_y = init_velocity
                        vel_x = 0
                    if event.key == pygame.K_UP:
                        vel_y = -init_velocity
                        vel_x = 0

            snake_x += vel_x
            snake_y += vel_y

            # Check collision with food
            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
                score += 1
                snk_length += 5
                food_x = random.randint(20, ScreenWidth - 20)
                food_y = random.randint(20, ScreenHeight - 20)

            # Fill the game window with a color
            gamewindow.fill(white)
            gamewindow.blit(bgimg,(0,0))
            text_screen("Score: " + str(score * 10), blue, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # Check collision with itself
            if head in snk_list[:-1]:
                gameOver = True

            # Check collision with boundaries
            if snake_x < 0 or snake_x > ScreenWidth or snake_y < 0 or snake_y > ScreenHeight:
                gameOver = True

            plot_snake(gamewindow, black, snk_list, snake_size)
            pygame.display.update()
            clock.tick(fps)

    pygame.quit()
    quit()

# Start the game
game_loop()

