__author__ = 'paoolo'

import math


class ActiveFunc():
    def __init__(self, func, name, desc=None):
        self.func = func
        self.name = name
        self.desc = desc

    def __call__(self, *args, **kwargs):
        return self.func(args[0])

    def __str__(self):
        return self.name if self.desc is None else self.desc


def linear(a=1.0, b=0.0):
    """
    Return linear activation function.

    Keyword arguments:
    a -- linear factor
    b -- linear shift (default 0.0)
    """
    return ActiveFunc(lambda x: a * x + b, 'linear', 'Linear activation function')


def linear_cut():
    """
    Return partially linear activation function.
    """
    return ActiveFunc(lambda x: -1.0 if x < -1.0 else (1.0 if x > 1.0 else x), 'linear_cut',
                      'Partially linear activation function')


def threshold_unipolar(a=0.0):
    """
    Return threshold unipolar activation function.

    Keyword arguments:
    a -- threshold value (default 0.0)
    """
    return ActiveFunc(lambda x: 0.0 if x < a else 1.0, 'threshold_unipolar',
                      'Threshold unipolar activation function')


def threshold_bipolar(a=0.0):
    """
    Return threshold bipolar activation function.

    Keyword arguments:
    a -- threshold value (default 0.0)
    """
    return ActiveFunc(lambda x: -1.0 if x < a else 1.0, 'threshold_bipolar',
                      'Threshold bipolar activation function')


def sigmoid_unipolar(beta=0.0):
    """
    Return sigmoid unipolar activation function.

    Keyword arguments:
    beta -- epsilon factor value, mostly in range (0, 1] (default 0.0)
    """
    return ActiveFunc(lambda x: 1.0 / (1.0 + math.pow(math.e, -beta * x)), 'sigmoid_unipolar',
                      'Sigmoid unipolar activation function')


def sigmoid_bipolar(beta=0.0):
    """
    Return sigmoid bipolar activation function.

    Keyword arguments:
    beta -- epsilon factor value, mostly in range (0, 1] (default 0.0)
    """

    def func(x):
        val = math.pow(math.e, -beta * x)
        return (1.0 - val) / (1.0 + val)

    return ActiveFunc(func, 'sigmoid_bipolar', 'Sigmoid bipolar activation function')


def gauss(a=1.0, b=1.0, c=1.0):
    """
    Return Gauss activation function. Arguments must be greater than zero.

    Keyword arguments:
    a -- Euler linear factor
    b -- linear shift
    c -- divided part
    """
    div = 2.0 * math.pow(c, 2)
    return ActiveFunc(lambda x: a * math.e - (math.pow(x - b, 2) / div), 'gauss',
                      'Gauss activation function')
