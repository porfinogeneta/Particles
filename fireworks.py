import pygame as pg
import sys, random

mainClock = pg.time.Clock()

WIDTH = 600
HEIGHT = 800

vec = pg.math.Vector2

pg.init()
from pygame.locals import *

screen = pg.display.set_mode((WIDTH, HEIGHT))


def set_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


class Particle:
    def __init__(self, x, y, exploder, color):
        self.color = color
        self.want_rect = False
        self.pos = vec(x, y)
        self.set_random_num_for_vel()
        self.velocity = vec(self.random_num_x, self.random_num_y)
        if exploder:
            self.velocity.normalize()
        # to make circle fireworks
            self.velocity.scale_to_length(random.randrange(-5, 5))
        # to make custom fireworks
            # self.velocity.scale_to_length(random.random())
        # to make rect fireworks
            # self.velocity = (random.randint(-5, 5), random.randint(-5, 5))


        else:
            self.velocity = vec(0, random.randint(-20, -10))
        self.expiration = 4
        self.acc = vec(0, 0)
        self.gravity = 0.01
        self.able_to_explode = True

    # sets direction of firework particle, makes it more random
    def set_random_num_for_vel(self):
        self.random_num_x = random.randint(1, 10)
        if random.random() <= 0.5:
            self.random_num_x *= -1
        self.random_num_y = random.randint(1, 10)
        if random.random() <= 0.5:
            self.random_num_y *= -1


    def draw(self):
        pg.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), 5)

    def apply_force(self, force):
        self.acc.y += force

    def explode(self):
        for i in range(0, 100):
            self.p = Particle(explode_pos.x, explode_pos.y, True, firework_color)
            fireworks.append(self.p)



    def update(self):
        self.draw()
        self.apply_force(self.gravity)
        self.velocity += self.acc

        self.pos += self.velocity
        self.expiration -= 0.05


particles = []
fireworks = []

if __name__ == '__main__':
    # game loop
    while True:

        # activities
        pg.display.set_caption('{:f}'.format(mainClock.get_fps()))
        screen.fill((0, 0, 0))


        # 5% probability to make firework every frame
        if random.random() < 0.05:
            particles.append(Particle(random.randint(0, WIDTH), random.randint(600, HEIGHT), False, set_color()))

        # update particles
        for particle in particles:
            particle.update()

            # give setting for new firework and deleting exploded particle
            if particle.velocity.y >= 0:
                explode_pos = particle.pos
                firework_color = particle.color
                particle.explode()
                particles.remove(particle)


        # update fireworks, deleting fireworks from the oldest to the last
        for i, firework in sorted(enumerate(fireworks), reverse=True):
            # print(i, firework, len(fireworks))
            firework.update()
            if fireworks[i].expiration <= 0:
                fireworks.pop(i)


        # buttons
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()

        # update
        pg.display.update()
        mainClock.tick(60)