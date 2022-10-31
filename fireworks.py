import sys

import numpy as np

from utils import Utils
from particles import FlyingParticle, ExplodingParticle
from parameters import Parameters

import pygame as pg
from pygame.locals import *


class State:
    particles = []
    fireworks = []


class PG:
    mainClock = pg.time.Clock()
    screen = pg.display.set_mode((Parameters.WIDTH, Parameters.HEIGHT))
    pg.init()

    @staticmethod
    def draw_circle(color, x: int, y: int):
        pg.draw.circle(PG.screen, color, (x, y), Parameters.CIRCLE_SIZE)

    @staticmethod
    def draw_trail(color, positions: []):
        for j, position in enumerate(positions):
            pg.draw.circle(PG.screen,
                           Utils.color_fade_to_black_linear(color,j,Parameters.MAX_TRAIL_SUB_PARTICLES),
                           (position.x, position.y),
                           Parameters.CIRCLE_SIZE)

    @staticmethod
    def generate_particle_explosion(x, y, color, particle_count=100):
        for j in range(particle_count):
            State.fireworks.append(ExplodingParticle(x, y, color))


if __name__ == '__main__':

    while True:
        """
        New frame display canvas clearance and fps count recalculation
        """
        pg.display.set_caption(f'Fireworks :: fps = {int(PG.mainClock.get_fps())}')
        PG.screen.fill(np.zeros(3))

        """
        Fixed chance to generate a new firework each frame
        """
        if np.random.rand() < Parameters.FIREWORK_GENERATION_CHANCE:
            State.particles.append(FlyingParticle(np.random.randint(0, Parameters.WIDTH),
                                                  np.random.randint(600, Parameters.HEIGHT),
                                                  Utils.random_color()))

        """
        Update each particle
        """
        for particle in State.particles:
            particle.update_particle()
            PG.draw_trail(particle.color, particle.previous_positions)
            PG.draw_circle(particle.color, int(particle.pos.x), int(particle.pos.y))
            if particle.explode() is True:
                PG.generate_particle_explosion(particle.pos.x, particle.pos.y, particle.color)
                State.particles.remove(particle)

        """
        Update each firework, from the latest to the oldest one
        """
        for i, firework in sorted(enumerate(State.fireworks), reverse=True):
            firework.update_particle()
            PG.draw_trail(firework.color, firework.previous_positions)
            PG.draw_circle(firework.color, int(firework.pos.x), int(firework.pos.y))
            if firework.alive() is False:
                State.fireworks.remove(firework)

        """
        PyGame Keyboard Event Handlers
        """
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()

        """
        Update
        """
        pg.display.update()
        PG.mainClock.tick(60)
