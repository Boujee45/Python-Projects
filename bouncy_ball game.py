import pygame
import sys
import random

# --- Initialize Pygame ---
pygame.init()

# --- Screen setup ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Clone Game")

# --- Colors ---
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
PURPLE = (160, 32, 240)

# --- Ball setup ---
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dy = 0
gravity = 0.5
jump_power = -10

# --- Ground ---
ground_y = HEIGHT - 50

# --- Game variables ---
score = 0
lives = 3
level = 1
font = pygame.font.SysFont("Arial", 28)

clock = pygame.time.Clock()


# --- Level generator ---
def generate_level():
    """Create platforms, coins, spikes, and portal for the level."""
    platforms = [
        pygame.Rect(200, 450, 200, 20),
        pygame.Rect(500, 350, 200, 20),
        pygame.Rect(300, 250, 150, 20),
    ]
    coins = [pygame.Rect(plat.centerx, plat.top - 30, 20, 20) for plat in platforms]

    spikes = [
        pygame.Rect(400, ground_y - 20, 40, 20),
        pygame.Rect(600, 430, 40, 20),
    ]
    portal = pygame.Rect(WIDTH - 80, ground_y - 80, 50, 80)  # exit on the right side
    return platforms, coins, spikes, portal


platforms, coins, spikes, portal = generate_level()

# --- Game loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= 5
    if keys[pygame.K_RIGHT]:
        ball_x += 5
    if keys[pygame.K_SPACE] and ball_dy == 0:
        ball_dy = jump_power

    # Gravity
    ball_dy += gravity
    ball_y += ball_dy

    # Ground collision
    if ball_y >= ground_y - ball_radius:
        ball_y = ground_y - ball_radius
        ball_dy = 0

    # Platform collision
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    for plat in platforms:
        if ball_rect.colliderect(plat) and ball_dy > 0:
            ball_y = plat.top - ball_radius
            ball_dy = 0

    # Wall collision
    if ball_x - ball_radius < 0:
        ball_x = ball_radius
    if ball_x + ball_radius > WIDTH:
        ball_x = WIDTH - ball_radius

    # Coin collection
    for coin in coins[:]:
        if ball_rect.colliderect(coin):
            coins.remove(coin)
            score += 1

    # Spike collision (lose life + reset ball)
    for spike in spikes:
        if ball_rect.colliderect(spike):
            lives -= 1
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2
            ball_dy = 0
            if lives <= 0:
                screen.fill(BLACK)
                game_over_text = font.render("GAME OVER", True, RED)
                screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                sys.exit()

    # --- Portal (advance to next level) ---
    if ball_rect.colliderect(portal):
        level += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dy = 0
        platforms, coins, spikes, portal = generate_level()

    # --- Drawing section ---
    screen.fill(WHITE)

    # Ground + platforms
    pygame.draw.rect(screen, GREEN, (0, ground_y, WIDTH, 50))
    for plat in platforms:
        pygame.draw.rect(screen, BLUE, plat)

    # Coins
    for coin in coins:
        pygame.draw.circle(screen, GOLD, coin.center, 10)

    # Spikes
    for spike in spikes:
        pygame.draw.polygon(screen, GRAY, [
            (spike.left, spike.bottom),
            (spike.centerx, spike.top),
            (spike.right, spike.bottom)
        ])

    # Portal (purple rectangle)
    pygame.draw.rect(screen, PURPLE, portal)

    # Ball
    pygame.draw.circle(screen, RED, (ball_x, int(ball_y)), ball_radius)

    # HUD
    score_text = font.render(f"Score: {score}", True, BLACK)
    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))
    screen.blit(level_text, (10, 70))

    pygame.display.flip()
    clock.tick(60)
