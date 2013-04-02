__author__ = 'paoolo'

import math

def linear(a, b=0.0):
    """
    Return linear activation function.

    Keyword arguments:
    a -- linear factor
    b -- linear shift (default 0.0)
    """
    return lambda x: a * x + b


def linear_cut():
    """
    Return partially linear activation function.
    """
    return lambda x: -1.0 if x < -1.0 else (1.0 if x > 1.0 else x)


def threshold_unipolar(a=0.0):
    """
    Return threshold unipolar activation function.

    Keyword arguments:
    a -- threshold value (default 0.0)
    """
    return lambda x: 0.0 if x < a else 1.0


def threshold_bipolar(a=0.0):
    """
    Return threshold bipolar activation function.

    Keyword arguments:
    a -- threshold value (default 0.0)
    """
    return lambda x: -1.0 if x < a else 1.0


def sigmoid_unipolar(beta=0.0):
    """
    Return sigmoid unipolar activation function.

    Keyword arguments:
    beta -- epsilon factor value, mostly in range (0, 1] (default 0.0)
    """
    return lambda x: 1.0 / (1.0 + math.pow(math.e, -beta * x))


def sigmoid_bipolar(beta=0.0):
    """
    Return sigmoid bipolar activation function.

    Keyword arguments:
    beta -- epsilon factor value, mostly in range (0, 1] (default 0.0)
    """

    def func(x):
        val = math.pow(math.e, -beta * x)
        return (1.0 - val) / (1.0 + val)

    return func


def gauss(a, b, c):
    """
    Return Gauss activation function. Arguments must be greater than zero.

    Keyword arguments:
    a -- Euler linear factor
    b -- linear shift
    c -- divided part
    """
    div = 2.0 * math.pow(c, 2)
    return lambda x: a * math.e - (math.pow(x - b, 2) / div)
