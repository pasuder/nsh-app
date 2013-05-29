from main.tools import function

__author__ = 'paoolo'

import math


def competitive(learning_rate):
    """
    Kohonen competitive learning mode.

    Keyword arguments:
    learning_rate -- function to determine learning rate in next iteration
    """

    def inner_func(winner, traits, iteration):
        winner.weights = map(lambda obj: obj[1] + learning_rate(iteration) * (obj[0] - obj[1]),
                             zip(traits, winner.weights))

    return function.Function(inner_func,
                             'learning.competitive',
                             'Competitive learning mode for Kohonen networks')


def neighborhood(learning_rate, measurement, neighborhood_radius):
    """
    Kohonen competitive learning mode with neighborhood.

    Keyword arguments:
    learning_rate -- function to determine learning rate in next iteration
    measurement -- function used to compute distance neurons location
    neighborhood_radius -- neighborhood radius function
    """

    def distance(neuron, winner, iteration):
        return math.exp(-(math.pow(measurement(neuron.location, winner.location), 2)) / (
            2 * math.pow(neighborhood_radius(iteration), 2)))

    def inner_func(neuron, winner, traits, iteration):
        neuron.weights = map(
            lambda obj: obj[1] + learning_rate(iteration) * distance(neuron, winner, iteration) * (obj[0] - obj[1]),
            zip(traits, neuron.weights))

    return function.Function(inner_func,
                             'learning.neighborhood',
                             'Neighborhood learning mode for Kohonen network')


def widrow_hoff(mi, kj):
    """
    Widrow-Hoff learning mode.

    Keyword arguments:
    mi -- stable parameter
    kj -- sequence of parameters
    """

    def inner_func(neuron, winner, traits):
        val = mi * (neuron.compute(traits) - winner.compute(traits))
        neuron.weights = map(lambda obj: obj[1] + val * obj[0], zip(kj, neuron.weights))

    return function.Function(inner_func,
                             'learning.widrow_hoff',
                             'Widrow-Hoff learning mode for CounterPropagation network')