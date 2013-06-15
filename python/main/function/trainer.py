__author__ = 'paoolo'

import math

from main.tools import function
from main.network.backpropagation import compute_error_on_network


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


import mpmath


def backward(learning_rate):
    def train_bp_neuron(neuron, error, iteration, signal):
        # Ugly!
        derivative = mpmath.diff(neuron.activation_func, error)
        print str(derivative) + ', ' + str(error) + ', ' + str(neuron.activation_func(error))
        neuron.weights = map(lambda val: val + learning_rate(iteration) * error * derivative * signal, neuron.weights)

    def train_bp_layer(layer, errors, iteration, signals):
        map(lambda val: train_bp_neuron(val[0], val[1], iteration, val[2]), zip(layer.neurons, errors, signals))

    def train_bp_network(network, target, iteration, signal):
        errors = compute_error_on_network(network, signal, target)
        for layer in network.layers:
            map(lambda val: train_bp_layer(val[0], val[1], iteration, signal), zip(network.layers, errors[1:]))
            signal = layer.compute(signal)

    return function.Function(train_bp_network,
                             'learning.backward',
                             'Backward error computation learning mode for BackPropagation network')