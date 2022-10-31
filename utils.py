import numpy as np


class Utils:
    """
    Math utilities for firework generation
    """

    @staticmethod
    def random_color(min_i=0, max_i=256):
        """
        Generate random color using random RGB values
        :param min_i: Min color intensity per channel
        :param max_i: Max color intensity per channel
        :return: [r,g,b] Each parameter r, g, b defines the intensity of the color as an integer between min_i and max_i
        :rtype: list
        """
        return np.random.randint(min_i, max_i, size=3)

    @staticmethod
    def random_ascend_velocity(min_y=-20, max_y=-10):
        """
        Generate random (0,y) velocity vector for an ascending particle
        Domain (y) = (min_y; max_y)
        :param min_y: Min value of Y component of a vector
        :param max_y: Max value of Y component of a vector
        :return: tuple
        """
        return tuple([0, np.interp(np.random.rand(), [0, 1], [min_y, max_y])])

    @staticmethod
    def random_explode_velocity(min_x=1, max_x=10, min_y=1, max_y=10):
        """
        Generate random (x,y) velocity vector
        Domain (x)  = (-max_x; -min_x) union (min_x; max_x)
        Domain (y)  = (-max_y; -min_y) union (min_y; max_y)
        :param min_x: Min value of X component of a vector
        :param max_x: Max value of X component of a vector
        :param min_y: Min value of Y component of a vector
        :param max_y: Max value of Y component of a vector
        :return: tuple
        """
        return tuple(np.random.randint([min_x, min_y], [max_x, max_y]) * np.random.choice([-1, 1], [2]))

    @staticmethod
    def integer_range(max_value):
        """
        Generate range with the given max_value
        :param max_value: value to base upon
        :return: [-max_value; max_value]
        """
        return np.interp(np.random.rand(), [0, 1], [-1 * max_value, max_value])
