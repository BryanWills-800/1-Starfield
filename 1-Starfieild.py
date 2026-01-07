import pygame
import sys
import numpy as np
import random as rnd

pygame.init()

black: tuple = (0, 0, 0)
white: tuple = (255, 255, 255)

WIDTH, HEIGHT = 1200, 750
SPEED, MAX_SPEED = 25, 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Starfield Simulator -> Coding Challenges #1")


class Star:
    def __init__(self):
        self.x = rnd.uniform(-WIDTH / 2, WIDTH / 2)
        self.y = rnd.uniform(-HEIGHT / 2, HEIGHT / 2)
        self.z = rnd.uniform(1, WIDTH)
        self.size = (1 - self.z / WIDTH) * 4
        self.pz = self.z

    def draw_star(self, surface: pygame.display):
        sx = (self.x / self.z) * WIDTH + WIDTH // 2
        sy = (self.y / self.z) * HEIGHT + HEIGHT // 2

        px = (self.x / self.pz) * WIDTH + WIDTH // 2
        py = (self.y / self.pz) * HEIGHT + HEIGHT // 2

        if SPEED > 0:
            ratio = min(1.0, SPEED / MAX_SPEED)
            r = int(255 - (255 * ratio))
            g = int(255 - (100 * ratio))
            b = 255
        elif SPEED < 0:
            ratio = min(1.0, abs(SPEED) / MAX_SPEED)
            r = 255
            g = int(255 - (150 * ratio))
            b = int(255 - (255 * ratio))
        else:
            r, g, b = 255, 255, 25

        pygame.draw.line(surface, (r ,g, b), (px, py), (sx, sy))
        # pygame.draw.circle(surface, self.color, (sx, sy), self.size)

    def update(self):
        self.pz = self.z
        self.z -= SPEED

        if self.z < 1:
            self.z = WIDTH
            self.pz = WIDTH
            self.x = rnd.uniform(-WIDTH, WIDTH)
            self.y = rnd.uniform(-HEIGHT, HEIGHT)

        elif self.z > WIDTH:
            self.z = 0.1
            self.pz = 0.1
            self.x = rnd.uniform(-WIDTH, WIDTH)
            self.y = rnd.uniform(-HEIGHT, HEIGHT)


clock = pygame.time.Clock()
stars: list[Star] = [Star() for _ in range(2000)]
session = True

while session:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            session = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            SPEED += 2
        if keys[pygame.K_DOWN]:
            SPEED -= 2

        SPEED = max(-MAX_SPEED, min(SPEED, MAX_SPEED))


    # screen.fill(black)
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(50)
    overlay.fill(black)
    screen.blit(overlay, (0, 0))

    for star in stars:
        star.update()
        star.draw_star(screen)

    pygame.display.flip()
    clock.tick(60)
    print(SPEED)

pygame.quit()
sys.exit()
