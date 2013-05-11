__author__ = 'paoolo'

import math
import func


def competitive(learning_rate):
    """
    Kohonen competitive learning mode.

    Keyword arguments:
    learning_rate -- function to determine learning rate in next iteration
    """

    def inner_func(winner, traits, iteration):
        winner.weights = map(lambda obj: obj[1] + learning_rate(iteration) * (obj[0] - obj[1]),
                             zip(traits, winner.weights))

    return func.FunctionWrapper(inner_func, 'learning.competitive', 'Competitive learning mode for Kohonen networks')


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

    return func.FunctionWrapper(inner_func, 'learning.neighborhood', 'Neighborhood learning mode for Kohonen network')