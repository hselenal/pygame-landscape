# Landscape Lab 

import pygame
import random 

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

cloud1_x = 100 
cloud1_y = 100 
cloud2_x = 500 
cloud2_y = 175 

road_line1 = 10 
road_line2 = 700

bird_x = 100 
bird_y = 100 
bird_speed = 5 
fly = False 

current_time = 0 
flap = 0 

face_y = 345
peek_speed = 1
peek = False 

rain_list = [] 
for i in range(200): 
    rain_x = random.randrange(640) 
    rain_y = random.randrange(500)
    rain_list.append([rain_x, rain_y])

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            position = pygame.mouse.get_pos() 
            if position[1] >= 300: 
                peek = True 
                peek_speed *= -1
            else: 
                fly = True 

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # Make the clouds move 
    cloud1_x -= 3 
    if cloud1_x < -100: 
        cloud1_x = WIDTH + 100
   
    cloud2_x -= 3 
    if cloud2_x < -150: 
        cloud2_x = WIDTH + 50

    # Make the road lines move 
    road_line1 -= 3
    if road_line1 < -700: 
        road_line1 = 700
   
    road_line2 -= 3 
    if road_line2 < -700: 
        road_line2 = 700 

    # Make it rain 
    for item in rain_list: 
        item[1] += 10
        if item[1] > 500: 
            item[0] = random.randrange(640) 
            item[1] = random.randrange(-20, -5)
    
    # Make the bird fly to mouse position when sky is clicked 
    if fly == True: 
        if bird_x < position[0] and bird_y < position[1]: 
            bird_x += bird_speed 
            bird_y += bird_speed 
            if bird_x > position[0] and bird_y > position[1]: 
                fly = False     
        if bird_x > position[0] and bird_y < position[1]: 
            bird_x -= bird_speed 
            bird_y += bird_speed 
            if bird_x < position[0] and bird_y > position[1]: 
                fly = False     
        if bird_x < position[0] and bird_y > position[1]: 
            bird_x += bird_speed 
            bird_y -= bird_speed 
            if bird_x > position[0] and bird_y < position[1]: 
                fly = False     
        if bird_x > position[0] and bird_y > position[1]: 
            bird_x -= bird_speed 
            bird_y -= bird_speed 
            if bird_x < position[0] and bird_y < position[1]: 
                fly = False    
    if bird_y > 275: 
        fly = False  
    
    # Track time for the bird flapping its wings 
    current_time = pygame.time.get_ticks() 
    if current_time - flap > 800: 
        flap = current_time

    # Make the passenger face peek out when ground is clicked 
    if peek == True: 
        face_y += peek_speed 
    if face_y < 328: 
        peek_speed *= -1 
    if face_y > 345: 
        peek = False 

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    # The sky, grass, and road 
    pygame.draw.rect(screen, (130, 180, 200), (0, 0, 640, 480))
    pygame.draw.rect(screen, (34, 139, 34), (0, 300, 640, 180))
    pygame.draw.rect(screen, (128, 128, 128), (0, 350, 640, 100))
   
    # The first cloud 
    pygame.draw.circle(screen, (211, 211, 211), (cloud1_x, cloud1_y), 30)
    pygame.draw.circle(screen, (211, 211, 211), (cloud1_x + 40, cloud1_y), 30)
    pygame.draw.circle(screen, (211, 211, 211), (cloud1_x + 80, cloud1_y), 30)
    pygame.draw.circle(screen, (211, 211, 211), (cloud1_x + 20, cloud1_y - 20), 30)
    pygame.draw.circle(screen, (211, 211, 211), (cloud1_x + 60, cloud1_y - 20), 33)

    # The second cloud 
    pygame.draw.circle(screen, (211, 211, 211), (cloud2_x, cloud2_y), 35)
    pygame.draw.circle(screen, (211, 211, 211), (cloud2_x + 50, cloud2_y), 35)
    pygame.draw.circle(screen, (211, 211, 211), (cloud2_x + 100, cloud2_y), 35)
    pygame.draw.circle(screen, (211, 211, 211), (cloud2_x + 75, cloud2_y - 35), 35)
    pygame.draw.circle(screen, (211, 211, 211), (cloud2_x + 25, cloud2_y - 35), 35)
    
    # The road lines 
    for i in range(0, 700, 100): 
        pygame.draw.rect(screen, (255, 255, 255), (road_line1 + i, 390, 70, 20))
        pygame.draw.rect(screen, (255, 255, 255), (road_line2 + i, 390, 70, 20)) 
    
    #The car 
    pygame.draw.circle(screen, (0, 0, 0), (450, 380), 30)
    pygame.draw.circle(screen, (0, 0, 0), (280, 380), 30)
    pygame.draw.polygon(screen, (255, 0, 0), ((300, 280), (400, 280), (450, 330), (500, 330), (530, 380), (200, 380), (200, 330), (250, 330)))
    pygame.draw.polygon(screen, (173, 216, 255), ((310, 290), (350, 290), (350, 330), (270, 330)))
    pygame.draw.polygon(screen, (173, 216, 255), ((360, 290), (390, 290), (430, 330,), (360, 330)))

    # The passenger's face 
    pygame.draw.circle(screen, (255, 225, 200), (320, face_y), 15)
    pygame.draw.circle(screen, (0, 0, 0), (318, face_y - 3), 2)
    pygame.draw.circle(screen, (0, 0, 0), (328, face_y - 3), 2)
    pygame.draw.ellipse(screen, (0, 0, 0), (307, face_y - 18, 27, 10))
    pygame.draw.ellipse(screen, (0, 0, 0), (302, face_y - 15, 10, 27))

    # The driver's face 
    pygame.draw.circle(screen, (255, 225, 200), (385, 315), 15)
    pygame.draw.circle(screen, (0, 0, 0), (383, 313), 2)
    pygame.draw.circle(screen, (0, 0, 0), (393, 313), 2)
    pygame.draw.ellipse(screen, (0, 0, 0), (372, 295, 27, 10))
    pygame.draw.ellipse(screen, (0, 0, 0), (367, 298, 10, 27))
    pygame.draw.rect(screen, (255, 225, 200), (378, 320, 14, 20))
    pygame.draw.rect(screen, (255, 0, 0), (270, 330, 160, 40))
    pygame.draw.line(screen, (0, 0, 0), (383, 321), (393, 321), 2)

    # The bird 
    if current_time - flap > 400: 
        # The wings flap down 
        pygame.draw.circle(screen, (0, 0, 0), (bird_x, bird_y - 1), 10)
        pygame.draw.polygon(screen, (0, 0, 0), ((bird_x + 7, bird_y - 5), (bird_x + 28, bird_y + 13), (bird_x + 7, bird_y + 5)))
        pygame.draw.polygon(screen, (0, 0, 0), ((bird_x - 7, bird_y - 5), (bird_x - 28, bird_y + 13), (bird_x - 7, bird_y + 5)))
        pygame.draw.polygon(screen, (255, 69, 0), ((bird_x - 3, bird_y - 1), (bird_x + 3, bird_y - 1), (bird_x, bird_y + 5)))
        pygame.draw.circle(screen, (255, 255, 0), (bird_x - 3, bird_y - 5), 1)
        pygame.draw.circle(screen, (255, 255, 0), (bird_x + 3, bird_y - 5), 1)
    else:
        # The wings flap up 
        pygame.draw.circle(screen, (0, 0, 0), (bird_x, bird_y + 1), 10)
        pygame.draw.polygon(screen, (0, 0, 0), ((bird_x + 7, bird_y - 5), (bird_x + 25, bird_y - 20), (bird_x + 7, bird_y + 5)))
        pygame.draw.polygon(screen, (0, 0, 0), ((bird_x - 7, bird_y - 5), (bird_x - 25, bird_y - 20), (bird_x - 7, bird_y + 5)))
        pygame.draw.polygon(screen, (255, 69, 0), ((bird_x - 3, bird_y + 1), (bird_x + 3, bird_y + 1), (bird_x, bird_y + 7)))
        pygame.draw.circle(screen, (255, 255, 0), (bird_x - 3, bird_y - 3), 1)
        pygame.draw.circle(screen, (255, 255, 0), (bird_x + 3, bird_y - 3), 1)

    # The rain 
    for item in rain_list: 
        pygame.draw.ellipse(screen, (50, 50, 255), (item[0], item[1], 2, 4))

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

pygame.quit()