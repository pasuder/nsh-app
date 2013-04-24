__author__ = 'paoolo'

import random
import function.activation as func
import decorators as deco


class Neuron(object):
    def __init__(self, active_func=func.linear(1.0), weights=None, bias=1.0, location=None):
        """
        Create simple neuron.

        Keyword arguments:
        activation_function -- one argument function used to compute activation value
                               (default: activation_function.linear(1.0))
        weights_sequence -- one dimensional sequence of weight values (default: [1.0])
        """
        if not weights:
            weights = [1.0]
        if not location:
            location = [0.0]
        self.active_func = active_func
        self.location = location
        self.weights = weights
        self.bias = bias

    def compute(self, values=None):
        """
        Compute value by neuron.

        Keyword arguments:
        input_sequence -- one dimensional sequence of values (default: [1.0])
        """
        if values is None:
            values = [1] * len(self.weights)
        summed = sum(map(lambda entry: entry[0] * entry[1], zip(values, self.weights))) - self.bias
        return self.active_func(summed)

    def __str__(self):
        return 'Neuron(' + str(self.active_func) + ', weights=' + str(self.weights) + ', bias=' + str(
            self.bias) + ', location=' + str(self.location) + ')'

    def init(self, min_value=0.0, max_value=1.0):
        self.weights = [random.random() * (max_value - min_value) + min_value for _ in xrange(len(self.weights))]

    def zero(self):
        self.weights = [0.0] * len(self.weights)
        self.bias = 0.0

    def locate(self, location):
        self.location = location


class Layer(object):
    def __init__(self, neurons=None):
        """
        Create neuronal layer.

        Keyword arguments:
        neurons_sequence -- one dimensional sequence of neurons
        """
        if not neurons:
            neurons = [Neuron()]
        self.neurons = neurons

    def compute(self, values=None):
        """
        Compute value by neuronal layer.

        Keyword arguments:
        input_sequence -- one dimensional sequence of values (default: [1.0])
        """
        return map(lambda n: n.compute(values), self.neurons)

    @deco.pretty_print
    def __str__(self):
        return 'Layer[' + reduce(lambda acc, n: acc + '\n\t' + str(n), self.neurons, '') + '\n]'

    def init(self, min_value=0.0, max_value=1.0):
        map(lambda neuron: neuron.init(min_value, max_value), self.neurons)

    def zero(self):
        map(lambda neuron: neuron.zero(), self.neurons)


class Network(object):
    def __init__(self, layers=None):
        """
        Create neuronal network.

        Keyword arguments:
        layers_sequence -- one dimensional sequence of neuronal layers
        """
        if not layers:
            layers = [Layer()]
        self.layers = layers

    def compute(self, values=None):
        """
        Compute value by neuronal network.

        Keyword arguments:
        input_sequence -- one dimensional sequence of values (default: [1.0])
        """
        for layer in self.layers:
            values = layer.compute(values)
        return values

    def __str__(self):
        return 'Network{' + reduce(lambda acc, l: acc + '\n' + str(l), self.layers, '') + '\n}'

    def init(self, min_value=0.0, max_value=1.0):
        map(lambda layer: layer.init(min_value, max_value), self.layers)

    def zero(self):
        map(lambda layer: layer.zero(), self.layers)