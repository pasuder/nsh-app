__author__ = 'paoolo'

import math

from nsh_app.tools import function


def linear(max_period=1.0, initial_radius=1.0):
    """
    Return a linear radius neighborhood function.

    f(iteration) = initial_radius * (1.0 - iteration / max_period) + 1.0

    Keyword arguments:
    max_period -- maximal period time
    initial_radius -- initial radius of neighborhood
    """
    return function.Function(lambda iteration: initial_radius * (1.0 - iteration / max_period) + 1.0,
                             'neighborhood.linear',
                             'Linear radius neighborhood function')


def exponential(max_iteration=1.0, min_transition=1.0, initial_radius=1.0):
    """
    Return an exponential radius neighborhood function.

    f(iteration) = initial_radius * (min_transition / initial_radius)^(iteration / max_iteration)

    Keyword arguments:
    max_iteration -- maximum count of iteration
    min_transition -- minimum value radius neighborhood transition
    initial_radius -- initial radius of neighborhood
    """
    return function.Function(
            lambda iteration: initial_radius * math.pow(min_transition / initial_radius, iteration / max_iteration),
            'neighborhood.exponential',
            'Exponential radius neighborhood function')
