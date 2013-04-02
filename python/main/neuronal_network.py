__author__ = 'paoolo'

import activation_function

class Neuron(object):
    def __init__(self, activation_function=activation_function.linear(1.0), weights_sequence=None):
        """
        Create simple neuron.

        Keyword arguments:
        activation_function -- one argument function used to compute activation value (default: activation_function.linear(1.0))
        weights_sequence -- one dimensional sequence of weight values (default: [1.0])
        """
        if not weights_sequence: weights_sequence = [1.0]
        self.activation_function = activation_function
        self.weight_sequence = weights_sequence

    def compute(self, values_sequence=None):
        """
        Compute value by neuron.

        Keyword arguments:
        input_sequence -- one dimensional sequence of values (default: [1.0])
        """
        if values_sequence is None: values_sequence = [1] * len(self.weight_sequence)
        summed = sum(map(lambda entry: entry[0] * entry[1], zip(values_sequence, self.weight_sequence)))
        return self.activation_function(summed)


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