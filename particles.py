from utils import Utils
from parameters import Parameters
from pygame.math import Vector2 as vec


class Particle(object):
    def __init__(self, x, y, color):
        """
        Cosmetic parameters
        """
        self.color = color
        """
        Physics initial parameters
        """
        self.pos = vec(x, y)
        self.acc = vec(0, 0)
        self.velocity = vec(Utils.random_ascend_velocity())
        """
        Time-domain parameters
        """
        self.expiration = Parameters.EXPIRATION_TIME
        self.previous_positions = []

    def apply_force(self, force):
        self.acc.y += force

    def update(self):
        """
        Previous Positions
        """
        self.previous_positions.append(self.pos.copy())
        if len(self.previous_positions) >= Parameters.MAX_TRAIL_SUB_PARTICLES:
            self.previous_positions.pop(0)
        """
        Calculate Physics
        """
        self.apply_force(Parameters.GRAVITY)
        self.velocity += self.acc
        self.pos += self.velocity
        """
        Time-domain evaluation
        """
        self.expiration -= Parameters.EXPIRATION_TIMEDELTA


class FlyingParticle(Particle):
    """
    A flying particle object
    """

    def update_particle(self):
        self.update()

    def explode(self):
        """
        Particle Explosion Statement
        """
        return True if self.velocity.y >= 0 else False


class ExplodingParticle(Particle):
    """
    An exploding particle object
    """

    def __init__(self, x, y, color):
        Particle.__init__(self, x, y, color)
        self.initial = vec(x, y)
        self.velocity = vec(Utils.random_explode_velocity())
        self.velocity.normalize()
        self.velocity.scale_to_length(Utils.integer_range(Parameters.EXPLODE_RADIUS))

    def update_particle(self):
        self.update()
        self.color = Utils.color_fade_to_black_positional(self.color, self.initial, self.pos)

    def alive(self):
        """
        Particle Destruction Statement
        """
        return True if self.expiration > 0 else False
