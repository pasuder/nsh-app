__author__ = 'paoolo'

import re

import activation_function


def pretty_print(inner_func):
    def func(*args, **kwargs):
        content = re.split(r'\n', inner_func(*args, **kwargs))
        return reduce(lambda acc, line: acc + '\n\t' + line, content[1:], '\t' + content[0])

    return func


class Neuron(object):
    def __init__(self, active_func=activation_function.linear(1.0), weights=None, bias=1.0):
        """
        Create simple neuron.

        Keyword arguments:
        activation_function -- one argument function used to compute activation value (default: activation_function.linear(1.0))
        weights_sequence -- one dimensional sequence of weight values (default: [1.0])
        """
        if not weights:
            weights = [1.0]
        self.active_func = active_func
        self.weights = weights
        self.bias = bias

    def compute(self, values_sequence=None):
        """
        Compute value by neuron.

        Keyword arguments:
        input_sequence -- one dimensional sequence of values (default: [1.0])
        """
        if values_sequence is None:
            values_sequence = [1] * len(self.weights)
        summed = sum(map(lambda entry: entry[0] * entry[1], zip(values_sequence, self.weights))) - self.bias
        return self.active_func(summed)

    def __str__(self):
        return 'Neuron(' + str(self.active_func) + ', weights=' + str(self.weights) + ', bias=' + str(self.bias) + ')'


def neuron_and():
    return Neuron(activation_function.threshold_unipolar(), weights=[1.0, 1.0], bias=1.5)


def neuron_or():
    return Neuron(activation_function.threshold_unipolar(), weights=[1.0, 1.0], bias=0.5)


def neuron_not():
    return Neuron(activation_function.threshold_unipolar(), weights=[-1.0], bias=-0.5)


class Layer(object):
    def __init__(self, neurons_sequence=None):
        """
        Create neuronal layer.

        Keyword arguments:
        neurons_sequence -- one dimensional sequence of neurons
        """
        if not neurons_sequence: neurons_sequence = [Neuron()]
        self.neurons_sequence = neurons_sequence

    def compute(self, values_sequence=None):
        """
        Compute value by neuronal layer.

        Keyword arguments:
        input_sequence -- one dimensional sequence of values (default: [1.0])
        """
        return map(lambda n: n.compute(values_sequence), self.neurons_sequence)

    @pretty_print
    def __str__(self):
        return 'Layer[' + reduce(lambda acc, n: acc + '\n\t' + str(n), self.neurons_sequence, '') + '\n]'


class Network(object):
    def __init__(self, layers_sequence=None):
        """
        Create neuronal network.

        Keyword arguments:
        layers_sequence -- one dimensional sequence of neuronal layers
        """
        if not layers_sequence: layers_sequence = [Layer()]
        self.layers_sequence = layers_sequence

    def compute(self, values_sequence=None):
        """
        Compute value by neuronal network.

        Keyword arguments:
        input_sequence -- one dimensional sequence of values (default: [1.0])
        """
        for layer in self.layers_sequence:
            values_sequence = layer.compute(values_sequence)
        return values_sequence

    def __str__(self):
        return 'Network{' + reduce(lambda acc, l: acc + '\n' + str(l), self.layers_sequence, '') + '\n}'