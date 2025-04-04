import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
cannonball_visible = False  # Initially hidden

# Pymunk Space Setup





# Load Images



# Resize Images





# Ground




# Create Cannonball (Initially Hidden)
cannonball_body = None
cannonball_shape = None

# Create Cannon
def create_cannon(x, y):
  
  


# Function to create a new cannonball when clicked
def create_cannonball(x, y):
    global cannonball_body, cannonball_shape, cannonball_visible

    # Remove existing ball from space if any
    if cannonball_body:
        space.remove(cannonball_body, cannonball_shape)

   #create cannon ball function here


# Draw function
def draw_objects():
    global game_over, game_won
    
    #background image



    # Draw Cannonball only if it's visible
    if cannonball_visible and cannonball_body:
        ball_pos = cannonball_body.position
        screen.blit(cannon_ball_image, (ball_pos.x - 25, ball_pos.y - 25))

    # Draw Cannon
    


# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # write the code to launch cannon ball on mouse click
       

    
   
    draw_objects()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
