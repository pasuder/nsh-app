import mpmath

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

    def modify_weight(neuron, index, signal_from_winner, excepted, signals, iteration):
        neuron[index] += learning_rate(iteration) * (neuron.compute(signals) - excepted) * signal_from_winner

    def inner_func(neurons, index, signal_from_winner, excepted_values, signals, iteration):
        map(lambda val: modify_weight(val[0], index, signal_from_winner, val[1], signals, iteration),
            zip(neurons, excepted_values))

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

    def gauss_distance(neuron, winner, iteration):
        measure = measurement(neuron.location, winner.location)
        return math.exp(-(math.pow(measure, 2)) / (2 * math.pow(neighborhood_radius(iteration), 2)))

    def rectangular_distance(neuron, winner, max_distance):
        measure = measurement(neuron.location, winner.location)
        return 1 if measure <= max_distance else 0

    def inner_func(neuron, winner, signals, iteration):
        neuron.weights = map(
            lambda obj: obj[0] + learning_rate(iteration) * gauss_distance(neuron, winner, iteration) * (
                obj[1] - obj[0]),
            zip(neuron.weights, signals))

    return function.Function(inner_func,
                             'learning.neighborhood',
                             'Neighborhood learning mode for Kohonen network')


def get_train_bp_network(train_bp_neuron):
    def train_bp_layer(layer, errors_per_neuron, iteration, signals):
        map(lambda val: train_bp_neuron(val[0], val[1], iteration, signals), zip(layer.neurons, errors_per_neuron))

    def train_bp_network(network, target, iteration, signals):
        errors_per_layer = compute_error_on_network(network, signals, target)
        for layer in network.layers:
            new_signal = layer.compute(signals)
            map(lambda error: train_bp_layer(layer, error, iteration, signals), errors_per_layer[1:])
            signals = new_signal

    return train_bp_network


def backward(learning_rate):
    def train_bp_neuron(neuron, error, iteration, signals):
        # Ugly!
        summed = math.fsum(map(lambda entry: entry[0] * entry[1], zip(signals, neuron.weights))) - neuron.bias
        derivative = mpmath.diff(neuron.activation_func, summed)
        neuron.weights = map(lambda val: val[0] + learning_rate(iteration) * error * derivative * val[1],
                             zip(neuron.weights, signals))

    return function.Function(get_train_bp_network(train_bp_neuron),
                             'learning.backward',
                             'Backward error computation learning mode for BackPropagation network')


def backward_momentum(learning_rate, momentum_rate):
    def train_bp_neuron(neuron, error, iteration, signals):
        # Ugly!
        summed = math.fsum(map(lambda entry: entry[0] * entry[1], zip(signals, neuron.weights))) - neuron.bias
        derivative = mpmath.diff(neuron.activation_func, summed)
        old_weights = neuron.weights
        if hasattr(neuron, 'old_weights'):
            neuron.weights = map(
                lambda val: val[0] + learning_rate(iteration) * error * derivative * val[1] + momentum_rate(iteration) *
                            (val[0] - val[2]),
                zip(neuron.weights, signals, neuron.old_weights))
        else:
            neuron.weights = map(
                lambda val: val[0] + learning_rate(iteration) * error * derivative * val[1],
                zip(neuron.weights, signals))
        neuron.old_weights = old_weights

    return function.Function(get_train_bp_network(train_bp_neuron),
                             'learning.backward_momentum',
                             'Backward error computation learning mode for BackPropagation network')