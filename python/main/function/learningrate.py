__author__ = 'paoolo'

import math

from main.tools import function


def const(value=1.0):
    """
    Return const learning rate function.

    f(iteration) = 1.0

    Keyword arguments:
    value           -- value to return
    """
    return function.Function(lambda iteration: value,
                             'learningrate.const',
                             'Const learning rate function')


def linear(max_period=1.0, initial_rate=1.0):
    """
    Return a linear learning rate function.

    f(iteration) = initial_rate * (1 - iteration / max_period)

    Keyword arguments:
    max_period      -- maximal period time
    initial_rate    -- initial value for learning rate
    """
    return function.Function(lambda iteration: initial_rate * (1 - iteration / max_period),
                             'learningrate.linear',
                             'Linear learning rate function')


def power(alpha=1.0, initial_rate=1.0):
    """
    Return a power learning rate function.

    f(iteration) = initial_rate * alpha * iteration^{-alpha}

    Keyword arguments:
    alpha           -- unknown parameter
    initial_rate    -- initial value for learning rate
    """
    return function.Function(lambda iteration: initial_rate * alpha * math.pow(iteration, -alpha),
                             'learningrate.power',
                             'Power learning rate function')


def exponential(max_iteration=1.0, min_transition=1.0, initial_rate=1.0):
    """
    Return an exponential learning rate function.

    f(iteration) = initial_rate * (min_transition / initial_rate) ^ (iteration / max_iteration)

    Keyword arguments:
    max_iteration   -- maximum count of iteration
    min_transition  -- minimum value radius neighborhood transition
    initial_rate    -- initial value for learning rate
    """
    return function.Function(
        lambda iteration: initial_rate * math.pow(min_transition / initial_rate, iteration / max_iteration),
        'learningrate.exponential',
        'Exponential learning rate function')


def kohonen(alpha=0.1, beta=0.1):
    """
    Return a learning function used in Kohonen network.

    f(iteration) = alpha - beta * iteration

    Keyword arguments:
    alpha           -- alpha value (default: 0.1)
    beta            -- beta value (default: 0.1)
    """
    return function.Function(lambda iteration: alpha - beta * iteration,
                             'learningrate.kohonen',
                             'Function used in Kohonen network')