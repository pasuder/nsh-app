__author__ = 'paoolo'

import math

from main.tools import function


def hebb(learning_rate):
    """
    Hebb learning mode.

    w_{ki}^(j+1) = w_{ki}^(j) + \learning_rate(j) * y_{k}^(j) * x_{i}^(j)

    Keyword arguments:
    learning_rate       -- function to determine learning rate in next iteration
    """

    def inner_func(neuron, signals, iteration):
        result = neuron.compute(signals)
        neuron.weights = map(lambda obj: obj[0] + learning_rate(iteration) * result * obj[1],
                             zip(neuron.weights, signals))

    return function.Function(inner_func,
                             'learning.hebb',
                             'Hebb learning mode')


def instar(learning_rate):
    """
    Instar learning mode.

    w_{ki}^(j+1) = w_{ki}^(j) + \learning_rate(j) * (x_{i}^(j) - w_{ki}^(j))

    Keyword arguments:
    learning_rate       -- function to determine learning rate in next iteration
    """

    def inner_func(neuron, signals, iteration):
        neuron.weights = map(lambda obj: obj[0] + learning_rate(iteration) * (obj[1] - obj[0]),
                             zip(neuron.weights, signals))

    return function.Function(inner_func,
                             'learning.instar',
                             'Instar learning mode')


def outstar(learning_rate):
    """
    Outstar learning mode.

    w_{ki}^(j+1) = w_{ki}^(j) + \learning_rate(j) * (y_{k}^(j) - w_{ki}^(j))

    Keyword arguments:
    learning_rate       -- function to determine learning rate in next iteration
    """

    def modify_weight(neuron, index, signals, iteration):
        neuron[index] += learning_rate(iteration) * (neuron.compute(signals) - neuron[index])

    def inner_func(neurons, index, signals, iteration):
        map(lambda neuron: modify_weight(neuron, index, signals, iteration), neurons)

    return function.Function(inner_func,
                             'learning.outstar',
                             'Outstar learning mode')


def neighborhood(learning_rate, measurement, neighborhood_radius):
    """
    Kohonen competitive learning mode with neighborhood.

    w_{ki}^(j+1) = w_{ki}^(j) + \learning_rate(j) * distance(i, i*) * (y_{k}^(j) - w_{ki}^(j))

    Keyword arguments:
    learning_rate       -- function to determine learning rate in next iteration
    measurement         -- function used to compute distance neurons location
    neighborhood_radius -- neighborhood radius function
    """

    def distance(neuron, winner, iteration):
        measure = measurement(neuron.location, winner.location)
        return math.exp(-(math.pow(measure, 2)) / (2 * math.pow(neighborhood_radius(iteration), 2)))

    def inner_func(neuron, winner, signals, iteration):
        neuron.weights = map(
            lambda obj: obj[0] + learning_rate(iteration) * distance(neuron, winner, iteration) * (obj[1] - obj[0]),
            zip(neuron.weights, signals))

    return function.Function(inner_func,
                             'learning.neighborhood',
                             'Neighborhood learning mode for Kohonen network')