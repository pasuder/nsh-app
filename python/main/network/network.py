__author__ = 'paoolo'

import random
import math

from main.tools import decorators
from main.function.activation import linear


class Neuron(object):
    def __init__(self, activation_func=linear(1.0), weights=None, bias=1.0, location=None):
        """
        Create neuron.

        Keyword arguments:
        active_func -- one argument function used to compute activation value
                       (default: activation_function.linear(1.0))
        weights     -- one dimensional sequence of weight values
                       (default: [1.0])
        bias        -- additional value added to computed value
                       (default: 1.0)
        location    -- used in Kohonen networks
                       (location: None)
        """
        self.activation_func = activation_func
        self.weights = [1.0] if not weights else map(lambda val: float(val), weights)
        self.bias = float(bias)
        self.location = [0] if not location else map(lambda val: int(val), location)

    def compute(self, values=None):
        """
        Compute value by neuron.

        Keyword arguments:
        values      -- sequence of values
                       (default: [1.0])
        """
        values = [1] * len(self.weights) if values is None else values
        summed = math.fsum(map(lambda entry: entry[0] * entry[1], zip(values, self.weights))) - self.bias
        return self.activation_func(summed)

    def init(self, min_value=0.0, max_value=1.0):
        """
        Init neuron weights.

        Keyword arguments:
        min_value   -- minimum value of range
                       (default: 0.0)
        max_value   -- maximum value of range
                       (default: 1.0)
        """
        self.weights = [random.random() * (max_value - min_value) + min_value for _ in xrange(len(self.weights))]
        self.bias = random.random() * (max_value - min_value) + min_value

    def zero(self):
        """
        Make neuron weights zero.
        """
        self.weights = [0.0] * len(self.weights)
        self.bias = 0.0

    def locate(self, location):
        """
        Set location for neuron.

        Keyword arguments:
        location    -- location of neuron
        """
        self.location = location

    def __str__(self):
        return 'Neuron(' + str(self.activation_func) + ', weights=' + str(self.weights) + ', bias=' + str(
            self.bias) + ', location=' + str(self.location) + ')'

    def __getitem__(self, item):
        return self.weights[item]

    def __setitem__(self, item, value):
        self.weights[item] = value

    def __iter__(self):
        return self.weights.__iter__()


class Layer(object):
    def __init__(self, neurons=None):
        """
        Create neuronal layer.

        Keyword arguments:
        neurons     -- sequence of neurons
                       (default: None)
        """
        self.neurons = [Neuron()] if not neurons else neurons

    def compute(self, values=None):
        """
        Compute value by neuronal layer.

        Keyword arguments:
        values      -- one dimensional sequence of values
                       (default: None)
        """
        return map(lambda n: n.compute(values), self.neurons)

    def init(self, min_value=0.0, max_value=1.0):
        """
        Init weights on layer.

        Keyword arguments:
        min_value   -- minimum value of range
                       (default: 0.0)
        max_value   -- maximum value of range
                       (default: 1.0)
        """
        map(lambda neuron: neuron.init(min_value, max_value), self.neurons)

    def zero(self):
        """
        Make weights of layer neurons zero.
        """
        map(lambda neuron: neuron.zero(), self.neurons)

    def get_winners_indexes(self, traits):
        """
        Get indexes of winners for traits vector.

        Keyword arguments:
        traits      -- traits vector
        """
        result = self.compute(traits)
        return [i for i, j in enumerate(result) if j == max(result)]

    def get_winners(self, traits, indexes=None):
        """
        Find winner for traits vector.

        Keyword arguments:
        traits      -- traits vector
        """
        return map(lambda index: self.neurons[index], self.get_winners_indexes(traits) if indexes is None else indexes)

    @decorators.pretty_print
    def __str__(self):
        return 'Layer[' + reduce(lambda acc, n: acc + '\n\t' + str(n), self.neurons, '') + '\n]'

    def __getitem__(self, item):
        return self.neurons[item]

    def __setitem__(self, item, value):
        self.neurons[item] = value

    def __iter__(self):
        return self.neurons.__iter__()


class Network(object):
    def __init__(self, layers=None):
        """
        Create neuronal network.

        Keyword arguments:
        layers      -- one dimensional sequence of neuronal layers
                       (default: None)
        """
        self.layers = [Layer()] if not layers else layers

    def compute(self, values=None):
        """
        Compute value by neuronal network.

        Keyword arguments:
        values      -- one dimensional sequence of values
                       (default: None)
        """
        for layer in self.layers:
            values = layer.compute(values)
        return values

    def init(self, min_value=0.0, max_value=1.0):
        """
        Init weights on network.

        Keyword arguments:
        min_value   -- minimum value of range
                       (default: 0.0)
        max_value   -- maximum value of range
                       (default: 1.0)
        """
        map(lambda layer: layer.init(min_value, max_value), self.layers)

    def zero(self):
        """
        Make all weights zero.
        """
        map(lambda layer: layer.zero(), self.layers)

    def __str__(self):
        return 'Network{' + reduce(lambda acc, layer: acc + '\n' + str(layer), self.layers, '') + '\n}'

    def __getitem__(self, item):
        return self.layers[item]

    def __setitem__(self, item, value):
        self.layers[item] = value

    def __iter__(self):
        return self.layers.__iter__()