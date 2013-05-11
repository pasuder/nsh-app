__author__ = 'paoolo'

import math


def euclidean(obj1, obj2):
    """
    Euclidean measure, used in competitive learning mode.
    """
    return math.sqrt(sum(map(lambda obj: math.pow(obj[0] - obj[1], 2.0), zip(obj1, obj2))))


def scalar(obj1, obj2):
    """
    Scalar measure, used in competitive learning mode.
    """
    return sum(map(lambda obj: obj[0] * obj[1], zip(obj1, obj2)))


def manhattan(obj1, obj2):
    """
    Manhattan measure, under L_1 standard, used in competitive learning mode.
    """
    return math.sqrt(sum(map(lambda obj: math.fabs(obj[0] - obj[1]), zip(obj1, obj2))))


def manhattan_infinity(obj1, obj2):
    """
    Manhattan measure, under L_infinity standard, used in competitive learning mode.
    """
    return max(map(lambda obj: obj[0] - obj[1], zip(obj1, obj2)))