import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)

# Game variables
paddle_width, paddle_height = 20, 100
ball_radius = 10
paddle_speed = 10
ball_speed_x, ball_speed_y = 5, 5

# Paddle positions
player1_y, player2_y = HEIGHT // 2 - paddle_height // 2, HEIGHT // 2 - paddle_height // 2

# Ball position
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < HEIGHT - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - paddle_height:
        player2_y += paddle_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (ball_x - ball_radius < paddle_width and player1_y < ball_y < player1_y + paddle_height) or \
            (ball_x + ball_radius > WIDTH - paddle_width and player2_y < ball_y < player2_y + paddle_height):
        ball_speed_x *= -1

    # Ball goes out of bounds
    if ball_x < 0 or ball_x > WIDTH:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # Reset ball position
        ball_speed_x *= -1  # Reverse direction

    # Drawing
    win.fill((0, 0, 0))  # Clear screen
    pygame.draw.rect(win, WHITE, (0, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(win, WHITE, (WIDTH - paddle_width, player2_y, paddle_width, paddle_height))
    pygame.draw.circle(win, WHITE, (ball_x, ball_y), ball_radius)
    pygame.display.flip()

    # Frame rate
    pygame.time.delay(30)
