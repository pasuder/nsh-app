__author__ = 'paoolo'

import math


def competitive(learning_rate):
    """
    Kohonen competitive learning mode.

    Keyword arguments:
    learning_rate -- function to determine learning rate in next iteration
    """

    def func(neuron, winner, traits, iteration):
        neuron.weights = map(lambda obj: obj[1] + learning_rate(iteration) * (obj[0] - obj[1]),
                             zip(traits, neuron.weights))

    return func


def neighborhood_lambda(measurement, neighborhood_radius):
    """
    Neighborhood function, used in competitive, with neighborhood, learning mode.

    Keyword arguments:
    measurement -- function used to compute distance neurons location
    neighborhood_radius -- neighborhood radius function
    """

    def func(neuron, winner, iteration):
        return math.exp(-(math.pow(measurement(neuron.location, winner.location), 2)) / (
            2 * math.pow(neighborhood_radius(iteration), 2)))

    return func


def neighborhood(learning_rate, lambda_func):
    """
    Kohonen competitive learning mode with neighborhood.
    """

    def func(neuron, winner, traits, iteration):
        neuron.weights = map(
            lambda obj: obj[1] + learning_rate(iteration) * lambda_func(neuron, winner, iteration) * (obj[0] - obj[1]),
            zip(traits, neuron.weights))

    return func