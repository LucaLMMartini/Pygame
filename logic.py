import os
import pygame


#screen settings
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Shooters")

#spaceship parameters
SPACESHIP_WIDTH = 100
SPACESHIP_HEIGHT = 100

SPACESHIP_X = WIDTH/2 - SPACESHIP_WIDTH/2
SPACESHIP_Y = HEIGHT - SPACESHIP_HEIGHT

SPEED = 4

LASER_WIDTH = 20
LASER_HEIGHT = 30


#load and scale images
SPACESHIP = pygame.image.load(os.path.join('Assets', 'spaceship.png'))
SPACESHIP = pygame.transform.scale(SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

BACKROUND = pygame.image.load(os.path.join('Assets', 'backround.jpg'))
BACKROUND = pygame.transform.scale(BACKROUND, (WIDTH, HEIGHT))

LASER = pygame.image.load(os.path.join('Assets', 'laser.png'))
LASER = pygame.transform.scale(LASER, (LASER_WIDTH, LASER_HEIGHT))

def moving_spaceship(s, l):
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_a]: #left
        s.x -= SPEED
        l.x -= SPEED

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_d]: #right
        s.x += SPEED
        l.x += SPEED

def shooting(l):
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_SPACE]:
        while l.y != 0:
            l.y -= 1



def draw_window(s, l):
    WIN.blit(BACKROUND, (0, 0))
    WIN.blit(SPACESHIP, (s.x, s.y))
    WIN.blit(LASER, (l.x, l.y))
    pygame.display.update()


def main():
    s = pygame.Rect(SPACESHIP_X, SPACESHIP_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    l = pygame.Rect(SPACESHIP_X + SPACESHIP_WIDTH/2 - LASER_WIDTH/2,
                    SPACESHIP_Y - LASER_HEIGHT + 10, LASER_WIDTH, LASER_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    FPS = 60


    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        moving_spaceship(s, l)
        shooting(l)
        draw_window(s, l)

    pygame.quit()

if __name__ == "__main__":
    main()
