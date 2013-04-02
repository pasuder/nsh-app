__author__ = 'paoolo'

import math

def print_values_activation_function(inner_func):
    """
    Print values from activation function.
    """

    def func(*args, **kwargs):
        y = inner_func(args[0])
        print "%f = func(%f)" % (y, args[0])
        return y

    return func


def linear_act_func(a, b=0.0):
    """
    Return linear activation function.

    Keyword arguments:
    a -- linear factor
    b -- linear shift (default 0.0)
    """

    def func(x):
        return a * x + b

    return func


def linear_cut_act_func():
    """
    Return partially linear activation function.
    """

    def func(x):
        if x < -1.0:
            return -1.0
        elif x > 1.0:
            return 1.0
        else:
            return x

    return func


def threshold_unipolar_act_func(a=0.0):
    """
    Return threshold unipolar activation function.

    Keyword arguments:
    a -- threshold value (default 0.0)
    """

    def func(x):
        if x < a:
            return 0.0
        else:
            return 1.0

    return func


def threshold_bipolar_act_func(a):
    """
    Return threshold bipolar activation function.

    Keyword arguments:
    a -- threshold value (default 0.0)
    """

    def func(x):
        if x < a:
            return -1.0
        else:
            return 1.0

    return func


def sigmoid_unipolar_act_func(beta=0.0):
    """
    Return sigmoid unipolar activation function.

    Keyword arguments:
    beta -- epsilon factor value, mostly in range (0, 1] (default 0.0)
    """

    def func(x):
        return 1.0 / (1.0 + math.pow(math.e, -beta * x))

    return func


def sigmoid_bipolar_act_func(beta=0.0):
    """
    Return sigmoid bipolar activation function.

    Keyword arguments:
    beta -- epsilon factor value, mostly in range (0, 1] (default 0.0)
    """

    def func(x):
        val = math.pow(math.e, -beta * x)
        return (1.0 - val) / (1.0 + val)

    return func


def gauss_act_func(a, b, c):
    """
    Return Gauss activation function. Arguments must be greater than zero.

    Keyword arguments:
    a -- Euler linear factor
    b -- linear shift
    c -- divided part
    """
    div = 2.0 * math.pow(c, 2)

    def func(x):
        return a * math.e - (math.pow(x - b, 2) / div)

    return func
