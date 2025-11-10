import pygame
import random


# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)

# Clock
clock = pygame.time.Clock()

# Bird
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 15
bird_velocity = 0
gravity = 0.5
flap_power = -8

# Pipes
pipe_width = 60
pipe_gap = 150
pipe_x = WIDTH
pipe_height = random.randint(100, 400)

# Score
score = 0
font = pygame.font.SysFont(None, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Flap with SPACEBAR
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = flap_power

    # Apply gravity
    bird_velocity += gravity
    bird_y += bird_velocity

    # Move pipe
    pipe_x -= 5
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_height = random.randint(100, 400)
        score += 1

    # Collision detection
    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        running = False  # hit top/bottom
    if (bird_x + bird_radius > pipe_x and bird_x - bird_radius < pipe_x + pipe_width):
        if bird_y - bird_radius < pipe_height or bird_y + bird_radius > pipe_height + pipe_gap:
            running = False  # hit pipe

    # Draw
    screen.fill(WHITE)
    # Bird
    pygame.draw.circle(screen, BLUE, (bird_x, int(bird_y)), bird_radius)
    # Pipes
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT))

    # Score
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
