import pygame
import sys

print("Welcome to Ben's Game!")


# =========================
# Ben's Game - Main Script
# =========================

# --- Initialization ---
pygame.init()
pygame.mixer.init()

# --- Screen Setup ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ben's Game")
clock = pygame.time.Clock()
# Background image
background_image = pygame.image.load("adventuretime.jpg").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


# --- Colors ---
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# --- Asset Loading ---
new_size = (50, 50)

# Player 1 image (Potato)
Potato_img = pygame.image.load("Potato.png").convert()
Potato_img.set_colorkey((255, 255, 255))
potato_img = pygame.transform.scale(Potato_img, new_size)

# Player 2 image (Mashed Potato)
Mashed_potato_img = pygame.image.load("mashedpotatoes.jpg").convert()
Mashed_potato_img.set_colorkey((255, 255, 255))
Mashed_potato_img = pygame.transform.scale(Mashed_potato_img, new_size)



# Bullet image
bullet_image = pygame.image.load("mashedpotatoes.jpg").convert()
bullet_image.set_colorkey((255, 255, 255))
bullet_image = pygame.transform.scale(bullet_image, (20, 20))

# --- Music ---
# ...existing code...
try:
    pygame.mixer.music.load("SpotifyMate.com - Oh Potato Dog - Parry Gripp.mp3")  # Replace with your file name
    pygame.mixer.music.play(-1)  # Loop forever
    pygame.mixer.music.set_volume(0.5)  # Volume: 0.0 to 1.0
except pygame.error as e:
    print(f"Error loading music: {e}")
# ...existing code...

# --- Game Variables ---
# --- Game Variables ---
x1, y1 = 0, 0  # Player 1 position
x2, y2 = 750, 550  # Player 2 position
speed = 5  # Movement speed
bullets = []  # List of active bullets
bullet_speed = 10
last_shot_time1 = 0  # For Player 1
last_shot_time2 = 0  # For Player 2
shoot_delay = 500  # milliseconds
mashed_potato_health = 5
score = 10 

# =========================
# Functions
# =========================

def handle_shooting():
    """Move bullets and remove those off-screen."""
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

# =========================
# Main Game Loop
# =========================
 
pygame.init()
pygame.mixer.init()



# --- Screen Setup ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ben's Game")
clock = pygame.time.Clock()
# Background image
background_image = pygame.image.load("adventuretime.jpg").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# --- Asset Loading ---
new_size = (50, 50)

# Player 1 image (Potato)
Potato_img = pygame.image.load("Potato.png").convert()
Potato_img.set_colorkey((255, 255, 255))
potato_img = pygame.transform.scale(Potato_img, new_size)

# Player 2 image (Mashed Potato)
Mashed_potato_img = pygame.image.load("mashedpotatoes.jpg").convert()
Mashed_potato_img.set_colorkey((255, 255, 255))
Mashed_potato_img = pygame.transform.scale(Mashed_potato_img, new_size)



# Bullet image
bullet_image = pygame.image.load("mashedpotatoes.jpg").convert()
bullet_image.set_colorkey((255, 255, 255))
bullet_image = pygame.transform.scale(bullet_image, (20, 20))

# --- Music ---
# ...existing code...
try:
    pygame.mixer.music.load("SpotifyMate.com - Oh Potato Dog - Parry Gripp.mp3")  # Replace with your file name
    pygame.mixer.music.play(1)  # Loop forever
    pygame.mixer.music.set_volume(1.0 )  # Volume: 0.0 to 1.0
            
except pygame.error as e:
    print(f"Error loading music: {e}")
# --- Game Variables ---



# =========================
# Functions
# =========================

# --- Game Variables ---
    x1, y1 = 0, 0  # Player 1 position
x2, y2 = 750, 550  # Player 2 position
speed = 5  # Movement speed
bullets = []  # List of active bullets
bullet_speed = 5
last_shot_time = 0
shoot_delay = 500  # milliseconds
mashed_potato_health = 5
score = 10




def handle_shooting():
    """Move bullets and remove those off-screen."""
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        bullet
        if bullet[1] < 0:
            bullets.remove(bullet)
 
# ...existing code...

running = True
while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # --- Player 1 Movement (WASD) ---
    if keys[pygame.K_w] and y1 > 0:
        y1 -= speed
    if keys[pygame.K_s] and y1 < SCREEN_HEIGHT - new_size[1]:
        y1 += speed
    if keys[pygame.K_a] and x1 > 0:
        x1 -= speed
    if keys[pygame.K_d] and x1 < SCREEN_WIDTH - new_size[0]:
        x1 += speed

    # --- Player 2 Movement (Arrow Keys) ---
    if keys[pygame.K_UP] and y2 > 0:
        y2 -= speed
    if keys[pygame.K_DOWN] and y2 < SCREEN_HEIGHT - new_size[1]:
        y2 += speed
    if keys[pygame.K_LEFT] and x2 > 0:
        x2 -= speed
    if keys[pygame.K_RIGHT] and x2 < SCREEN_WIDTH - new_size[0]:
        x2 += speed

    

    # --- Shooting Mechanic with Delay ---
       # --- Shooting Mechanic with Delay ---
    current_time = pygame.time.get_ticks()
    # Player 1 (LSHIFT)
    # ...existing code...

# REMOVE these lines from inside your game loop!
# last_shot_time1 = 2
# last_shot_time2 = 4


    current_time = pygame.time.get_ticks()
    # Player 1 (LSHIFT)
    if keys[pygame.K_LSHIFT] and current_time - last_shot_time1 > shoot_delay:
        bullets.append([x1 + new_size[0] // 2 - 10, y1])
        last_shot_time1 = current_time
    # Player 2 (RSHIFT)
    if keys[pygame.K_RSHIFT] and current_time - last_shot_time2 > shoot_delay:
        bullets.append([x2 + new_size[0] // 2 - 10, y2])
        last_shot_time2 = current_time

    # --- Handle Shooting ---
    handle_shooting()

    # --- Drawing ---
    screen.blit(background_image, (0, 0))
    screen.blit(potato_img, (x1, y1))
    screen.blit(Mashed_potato_img, (x2, y2))

    # --- Collision Rectangles ---
    mashed_potato_rect = Mashed_potato_img.get_rect(topleft=(x2, y2))
    potato_rect = potato_img.get_rect(topleft=(x1, y1))
    if mashed_potato_rect.colliderect(potato_rect):
        mashed_potato_rect = mashed_potato_rect.move(0, -speed)

    # --- Draw Bullets & Check Collisions ---
    for bullet in bullets[:]:
        screen.blit(bullet_image, bullet)
        bullet_rect = pygame.Rect(bullet[1], bullet[1], 20, 20)
        if bullet_rect.colliderect(mashed_potato_rect):
            bullet.rect -=bullet_speed
        if bullet_rect.colliderect(mashed_potato_rect):
            print("Bullet hit the mashed potato!")
            bullets.remove(bullet)
        elif bullet_rect.colliderect(potato_rect):
            bullet.rect.colliderect(potato_rect)
            bullet[1] -= bullet_speed
            mashed_potato_health -= 1
            print("Bullet hit the potato!")
            bullets.remove(bullet)

    # --- Player Collision Highlight ---
    if mashed_potato_rect.colliderect(potato_rect):
        if mashed_potato_rect.colliderect(potato_rect):
           x1 -= speed
           y1 -= speed
           x2 += speed
           y2 += speed


    bullets = []
     

    # --- Check Bullet Collisions ---
    # This section checkis for bullet collisions with the mashed potato
    # if a collision is detected the health of the mashed potato is reduced
    # if the health reaches 0, the game ends
    bullets = [1,1, 20, 20]
    bullets_rect = pygame.Rect(bullets[1], bullets[1], 20, 20)
    if bullets_rect.colliderect(mashed_potato_rect):  speed
    if bullets_rect.colliderect(mashed_potato_rect):
      mashed_potato_health -= 1
      if mashed_potato_health <= 0:
           print("Mashed Potato defeated!")
           
    running = False
    for bullet in bullets[:]:
        if bullets_rect.colliderect(mashed_potato_rect):
            bullets.remove(bullet)


        
    # --- Update Display ---
pygame.display.flip()
clock.tick(60)

pygame.quit()