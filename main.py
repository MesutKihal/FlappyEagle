
import pygame
import sys
import random
import time

def main():
    pygame.init()
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 100, 0)
    BLACK = (0, 0, 0)
    width = 800
    height = 480
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Flappy Eagle")
    fps = 60
    clock = pygame.time.Clock()
    background = pygame.image.load("000.png")
    # Background settings
    bg_x = 0
    bg_y = 0
    bg_w = 900
    bg_h = 504
    # Score settings
    font = pygame.font.SysFont('impact', 38, False)
    score = 0
    score_x = 700
    score_y = 30
    # Tube Settings
    top_tube = pygame.image.load("top_tube.png")
    bottom_tube = pygame.image.load("bottom_tube.png")
    tube_x = 800
    tube_y = 0
    tube_w = 60
    tube_h = random.randint(50, 320)
    # Bird Settings
    i_frame = 0
    bird_frames = [pygame.image.load("frame0.png"),
                   pygame.image.load("frame1.png"),
                   pygame.image.load("frame2.png"),
                   pygame.image.load("frame3.png"),
                   pygame.image.load("frame4.png"),
                   pygame.image.load("frame5.png"),]
    bird_x = 380
    bird_y = 220
    bird_w = 50
    bird_h = 50
    gravity = 5
    # Velocity
    vel = 5
    # Jump constant
    jump = 12
    # Draw on the screen
    def drawScreen():
        screen.fill(WHITE)
        # Background
        screen.blit(background, (bg_x, bg_y))
        screen.blit(background, (bg_x+bg_w, bg_y))
        # Top tube
        screen.blit(top_tube, (tube_x, tube_y-(height-tube_h)))
        # Bottom tube
        screen.blit(bottom_tube, (tube_x, tube_y+tube_h+110))
        # Bird
        screen.blit(bird_frames[i_frame], (bird_x-(bird_w//2), bird_y-(bird_h//2)))
        # Score
        screen.blit(score_text, (score_x, score_y))
    # Menu Screen
    def menu():
        # Button Settings
        btn_w = 100
        btn_h = 50
        btn_x = (width//2)-(btn_w//2)
        btn_y = (height//2)-(btn_h//2)
        # Title Settings
        title_x = (width//2)-100
        title_y = (height//2)-100
        # Main Loop
        while True:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            title_text = font.render("FLAPPY EAGLE", False, WHITE)
            btn_text = font.render("START", False, WHITE)
            if btn_x <= mouse[0] <= btn_x + btn_w and btn_y <= mouse[1] <= btn_y + btn_h and click[0]:
                break
            screen.fill(WHITE)
            # Draw Background
            screen.blit(background, (bg_x, bg_y))
            screen.blit(title_text, (title_x, title_y))
            # Draw start button
            pygame.draw.rect(screen, ORANGE, (btn_x, btn_y, btn_w, btn_h))
            screen.blit(btn_text, (btn_x+5, btn_y))
            # Refresh
            pygame.display.update()
        return
    menu()
    # Main Loop
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        # Score text render
        score_text = font.render(f"{score}", False, WHITE)
        # If space is pressed decrease y by jump
        if keys[pygame.K_SPACE] and bird_y > 0:
            # Play Jump Sound
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('wing.mp3'))
            bird_y -= jump
        # Borders
        if tube_x <= -50:
            tube_x = width
            tube_h = random.randint(40, 320)
            # Score Count
            score += 1
            # Play Score Sound
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('point.mp3'))
            # Increase velocity
            if score == 10:
                vel += 1
            elif score == 25:
                vel += 1
            elif score == 60:
                vel += 1
            elif score == 130:
                vel += 1
            elif score == 520:
                vel += 1
            elif score == 700:
                vel += 1
            else:
                vel = vel
        else:
            # Tube motion
            tube_x -= vel
        # Background motion
        if bg_x <= -bg_w:
            bg_x = 0
        else:
            bg_x -= 1
        # Collision
        if bird_x + bird_w > tube_x and bird_y < tube_y + tube_h and bird_x < tube_x:
            # Play Hit Sound
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('hit.mp3'))
            # Restore default values
            bg_x = 0
            bg_y = 0
            tube_x = 800
            tube_y = 0
            score = 0
            bird_y = 220
            tube_h = random.randint(50, 320)
            # Return to menu
            time.sleep(0.5)
            menu()
        elif bird_x + bird_w > tube_x and bird_y + bird_h > tube_y + tube_h + 110 and bird_x < tube_x:
            # Play Hit Sound
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('hit.mp3'))
            # Restore default values
            bg_x = 0
            bg_y = 0
            tube_x = 800
            tube_y = 0
            score = 0
            bird_y = 220
            tube_h = random.randint(50, 320)
            # Return to menu
            time.sleep(0.5)
            menu()
        # Gravity effect
        if bird_y + bird_h < height:
            bird_y += gravity
        else:
            # Play Hit Sound
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('hit.mp3'))
            # Restore default values
            bg_x = 0
            bg_y = 0
            tube_x = 800
            tube_y = 0
            score = 0
            bird_y = 220
            tube_h = random.randint(50, 320)
            # Return to menu
            time.sleep(0.5)
            menu()
        # Bird Frames
        if i_frame == len(bird_frames) - 1:
            i_frame = 0
        else:
            i_frame += 1
        # Refresh Screen
        drawScreen()
        pygame.display.update()
    return


if __name__ == '__main__':
    main()
