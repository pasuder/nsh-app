__author__ = 'paoolo'

import math


def euclidean(obj1, obj2):
    """
    Euclidean measure, used in competitive learning mode.

    d(x, w_i) = \sqrt(\sum_{j=1}^{N} (x_j - w_{ij})^2) )
    """
    return math.sqrt(math.fsum(map(lambda obj: math.pow(obj[0] - obj[1], 2.0), zip(obj1, obj2))))


def scalar(obj1, obj2):
    """
    Scalar measure, used in competitive learning mode.

    d(x, w_i) = \sum_{j=1}^{N} (x_j * w_{ij})
    """
    return math.fsum(map(lambda obj: obj[0] * obj[1], zip(obj1, obj2)))


def manhattan(obj1, obj2):
    """
    Manhattan measure, under L_1 standard, used in competitive learning mode.

    d(x, w_i) = \sqrt(\sum_{j=1}^{N} abs(x_j - w_{ij}) )
    """
    return math.sqrt(math.fsum(map(lambda obj: math.fabs(obj[0] - obj[1]), zip(obj1, obj2))))


def manhattan_infinity(obj1, obj2):
    """
    Manhattan measure, under L_infinity standard, used in competitive learning mode.

    d(x, w_i) = \max_{j} (x_j - w_{ij})
    """
    return max(map(lambda obj: obj[0] - obj[1], zip(obj1, obj2)))
