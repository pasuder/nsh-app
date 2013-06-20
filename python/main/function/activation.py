import math

__author__ = 'paoolo'

import mpmath

from main.tools import function


def linear(a=1.0, b=0.0):
    """
    Return linear activation function.

    f(x) = a * x + b

    Keyword arguments:
    a -- linear factor (default 1.0)
    b -- linear shift (default 0.0)
    """
    return function.Function(lambda x: a * x + b,
                             'activation.linear',
                             'Linear activation function')


def linear_cut():
    """
    Return partially linear activation function.

    f(x) = -1.0, x \in (-inf, -1.0)
    f(x) =    x, x \in [-1.0, +1.0)
    f(x) =  1.0, x \in [+1.0, +inf)

    """
    return function.Function(lambda x: -1.0 if x < -1.0 else (1.0 if x > 1.0 else x),
                             'activation.linear_cut',
                             'Partially linear activation function')


def threshold_unipolar(a=0.0):
    """
    Return threshold unipolar activation function.

    f(x) = 0.0, x \in (-inf, a)
    f(x) = 1.0, x \in [a, +inf)

    Keyword arguments:
    a -- threshold value (default 0.0)
    """
    return function.Function(lambda x: 0.0 if x < a else 1.0,
                             'activation.threshold_unipolar',
                             'Threshold unipolar activation function')


def threshold_bipolar(a=0.0):
    """
    Return threshold bipolar activation function.

    f(x) = -1.0, x \in (-inf, a)
    f(x) = +1.0, x \in [a, +inf)

    Keyword arguments:
    a -- threshold value (default 0.0)
    """
    return function.Function(lambda x: -1.0 if x < a else 1.0,
                             'activation.threshold_bipolar',
                             'Threshold bipolar activation function')


def sigmoid_unipolar(beta=1.0):
    """
    Return sigmoid unipolar activation function.

    f(x) = 1.0 / (1.0 + exp(-beta * x) )

    Keyword arguments:
    beta -- epsilon factor value, mostly in range (0, 1] (default 1.0)
    """
    return function.Function(lambda x: 1.0 / (1.0 + mpmath.exp(-beta * x)),
                             'activation.sigmoid_unipolar',
                             'Sigmoid unipolar activation function')


def sigmoid_bipolar(beta=1.0):
    """
    Return sigmoid bipolar activation function.

    f(x) = (1.0 - exp(-beta * x)) / (1.0 + exp(-beta * x))

    Keyword arguments:
    beta -- epsilon factor value, mostly in range (0, 1] (default 1.0)
    """

    def f(x):
        val = mpmath.exp(-beta * x)
        return (1.0 - val) / (1.0 + val)

    return function.Function(f,
                             'activation.sigmoid_bipolar',
                             'Sigmoid bipolar activation function')


def gauss(a=1.0, b=1.0, c=1.0):
    """
    Return Gauss activation function. Arguments must be greater than zero.

    f(x) = a * Epsilon - ((x-b)^2 / (2.0 * c^2))

    Keyword arguments:
    a -- Euler linear factor
    b -- linear shift
    c -- divided part
    """
    div = 2.0 * (c ** 2.0)
    return function.Function(lambda x: a * mpmath.e - (((x - b) ** 2) / div),
                             'activation.gauss',
                             'Gauss activation function')


def tanh():
    """
    Return tanh activation function.

    f(x) = tanh(x)
    """
    return function.Function(lambda x: math.tanh(x),
                             'activation.tanh',
                             'Tanh activation function')