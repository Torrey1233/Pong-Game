# Welcome to my test of making the game pong using pygame
# I created a two player pong game that you can play with a friend on your keyboard
# Similarly to Fireboy and Watergirl one player will use WASD while the other uses arrow keys
# By Torrey Liu

# Importing Libraries
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 1000
HEIGHT = 800
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_SIZE = 15
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
windowSize = pygame.display.set_mode((WIDTH, HEIGHT))

# Game caption name
pygame.display.set_caption("Torrey's Pong Game")

# Initialize paddles and ball positions
# Creating the paddles and ball
player1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Initialize ball direction
ballDirection = [4, 4]

# Initialize ball color
ballColor = (255, 255, 255)

# Initialize scores
scorePlayer1 = 0
scorePlayer2 = 0

# Set up the clock for the fps of the game
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.Font(None, 36)

# Exit the program by pressing the exit to terminate program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    # If the key is pressed
    keys = pygame.key.get_pressed()
    # Setting the pressed keys to have up and down movements of the paddle
    # Also controls the speed it moves
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= 5
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += 5
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= 5
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += 5

    # Move the ball in x and y directions
    ball.x += ballDirection[0]
    ball.y += ballDirection[1]

    # Ball collisions with walls and paddles
    # Change the ball colour randomly when it hits a paddle
    if ball.colliderect(player1) or ball.colliderect(player2):
        ballDirection[0] = -ballDirection[0]
        ballColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # When the ball hits the bottom or top of the window it deflects back into the game
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ballDirection[1] = -ballDirection[1]  # Reverse the vertical direction

    # Check for a point scored (reset game and update scores)
    # When the ball exits the game from left or right side
    # Add a score to the player from the opposite side it exits to keep score
        
    if ball.left <= 0:
        scorePlayer2 += 1
        ballDirection[0] = -ballDirection[0]    # Reverse the horizontal direction
        ball.x = WIDTH // 2 - BALL_SIZE // 2    # Resets ball x position to center
        ball.y = HEIGHT // 2 - BALL_SIZE // 2   # Resets ball y position to center
        ballColor = (255, 255, 255)            # Reset ball color

    elif ball.right >= WIDTH:
        scorePlayer1 += 1
        ballDirection[0] = -ballDirection[0]    # Reverse the horizontal direction
        ball.x = WIDTH // 2 - BALL_SIZE // 2    # Resets ball x position to center
        ball.y = HEIGHT // 2 - BALL_SIZE // 2   # Resets ball y position to center
        ballColor = (255, 255, 255)            # Reset ball color

    # Draw everything
    # Makes the colour black
    windowSize.fill(BLACK)
    pygame.draw.rect(windowSize, WHITE, player1)
    pygame.draw.rect(windowSize, WHITE, player2)
    pygame.draw.ellipse(windowSize, ballColor, ball)  # Use ballColor for the ball

    # Render scores
    score_text_player1 = font.render(str(scorePlayer1), True, WHITE)
    score_text_player2 = font.render(str(scorePlayer2), True, WHITE)

    # Draw the score on top of the black background
    windowSize.blit(score_text_player1, (WIDTH // 4, 20))
    windowSize.blit(score_text_player2, (3 * WIDTH // 4 - score_text_player2.get_width(), 20))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)
