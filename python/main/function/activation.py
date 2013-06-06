__author__ = 'paoolo'

import math

from main.tools import function


def linear(a=1.0, b=0.0):
    """
    Return linear activation function.

    Keyword arguments:
    a -- linear factor
    b -- linear shift (default 0.0)
    """
    return function.Function(lambda x: a * x + b,
                             'activation.linear',
                             'Linear activation function')


def linear_cut():
    """
    Return partially linear activation function.
    """
    return function.Function(lambda x: -1.0 if x < -1.0 else (1.0 if x > 1.0 else x),
                             'activation.linear_cut',
                             'Partially linear activation function')


def threshold_unipolar(a=0.0):
    """
    Return threshold unipolar activation function.

    Keyword arguments:
    a -- threshold value (default 0.0)
    """
    return function.Function(lambda x: 0.0 if x < a else 1.0,
                             'activation.threshold_unipolar',
                             'Threshold unipolar activation function')


def threshold_bipolar(a=0.0):
    """
    Return threshold bipolar activation function.

    Keyword arguments:
    a -- threshold value (default 0.0)
    """
    return function.Function(lambda x: -1.0 if x < a else 1.0,
                             'activation.threshold_bipolar',
                             'Threshold bipolar activation function')


def sigmoid_unipolar(beta=0.0):
    """
    Return sigmoid unipolar activation function.

    Keyword arguments:
    beta -- epsilon factor value, mostly in range (0, 1] (default 0.0)
    """
    return function.Function(lambda x: 1.0 / (1.0 + math.exp(-beta * x)),
                             'activation.sigmoid_unipolar',
                             'Sigmoid unipolar activation function')


def sigmoid_bipolar(beta=1.0):
    """
    Return sigmoid bipolar activation function.

    Keyword arguments:
    beta -- epsilon factor value, mostly in range (0, 1] (default 0.0)
    """

    def f(x):
        val = math.exp(-beta * x)
        return (1.0 - val) / (1.0 + val)

    return function.Function(f,
                             'activation.sigmoid_bipolar',
                             'Sigmoid bipolar activation function')


def gauss(a=1.0, b=1.0, c=1.0):
    """
    Return Gauss activation function. Arguments must be greater than zero.

    Keyword arguments:
    a -- Euler linear factor
    b -- linear shift
    c -- divided part
    """
    div = 2.0 * math.pow(c, 2)
    return function.Function(lambda x: a * math.e - (math.pow(x - b, 2) / div),
                             'activation.gauss',
                             'Gauss activation function')
