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
        self.expiration = 4

    def apply_force(self, force):
        self.acc.y += force

    def update(self):
        """
        Calculate Physics
        """
        self.apply_force(Parameters.GRAVITY)
        self.velocity += self.acc
        self.pos += self.velocity
        """
        Time-domain evaluation
        """
        self.expiration -= 0.05


class FlyingParticle(Particle):
    """
    A flying particle object
    """

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
        self.velocity = vec(Utils.random_explode_velocity())
        self.velocity.normalize()
        self.velocity.scale_to_length(Utils.integer_range(Parameters.EXPLODE_RADIUS))

    def alive(self):
        """
        Particle Destruction Statement
        """
        return True if self.expiration > 0 else False
