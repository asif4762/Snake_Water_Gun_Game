import pygame
import random

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 600, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fancy Snake-Water-Gun Game")

# Load images
bg_image = pygame.image.load("background.jpg")  # Add a fancy background image
snake_img = pygame.image.load("snake.png")
water_img = pygame.image.load("water.png")
gun_img = pygame.image.load("gun.png")

# Resize images
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
snake_img = pygame.transform.scale(snake_img, (120, 120))
water_img = pygame.transform.scale(water_img, (120, 120))
gun_img = pygame.transform.scale(gun_img, (120, 120))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (180, 180, 180)

# Font
font = pygame.font.Font(None, 36)

# Choices
youDist = {"Snake": 1, "Water": -1, "Gun": 0}
reverseDist = {1: "Snake", -1: "Water", 0: "Gun"}
choices = ["Snake", "Water", "Gun"]

# Button positions
snake_rect = pygame.Rect(50, 350, 120, 120)
water_rect = pygame.Rect(240, 350, 120, 120)
gun_rect = pygame.Rect(430, 350, 120, 120)

# Game variables
user_choice = None
computer_choice = None
result = ""

# Function to display text
def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    win.blit(label, (x, y))

# Game loop
running = True
while running:
    win.blit(bg_image, (0, 0))  # Draw background

    draw_text("Choose Your Move:", 200, 50, BLACK)
    
    # Draw images as buttons
    win.blit(snake_img, (50, 350))
    win.blit(water_img, (240, 350))
    win.blit(gun_img, (430, 350))
    
    # Show results
    if user_choice:
        draw_text(f"You chose: {user_choice}", 50, 150, GREEN)
        draw_text(f"Computer chose: {computer_choice}", 50, 200, RED)
        draw_text(result, 50, 250, BLUE)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Play click sound (optional, if you want to enable it)
            # click_sound.play()
            if snake_rect.collidepoint(x, y):
                user_choice = "Snake"
            elif water_rect.collidepoint(x, y):
                user_choice = "Water"
            elif gun_rect.collidepoint(x, y):
                user_choice = "Gun"
            
            if user_choice:
                computer_choice = random.choice(choices)
                you = youDist[user_choice]
                comp = youDist[computer_choice]
                
                if you == comp:
                    result = "It's a Draw!"
                    # draw_sound.play()  # Optional sound for draw
                elif (comp == -1 and you == 1) or (comp == 0 and you == -1) or (comp == 1 and you == 0):
                    result = "You Win!"
                    # win_sound.play()  # Optional sound for win
                else:
                    result = "You Lose!"
                    # lose_sound.play()  # Optional sound for lose

pygame.quit()
