__author__ = 'paoolo'

from kohonen import Kohonen
from network import Layer, Neuron

from main.trainer import counterpropagation


class CounterPropagation(Kohonen):
    def __init__(self, input_func, kohonen_func, grossberg_func, inputs, outputs, width, height=1):
        # create Grossberg output layer
        grossberg_layer = [Neuron(activation_func=grossberg_func, weights=[1.0] * width * height)
                           for _ in range(1, outputs)]

        # initialize Kohonen network
        super(CounterPropagation, self).__init__(input_func, kohonen_func, inputs, width, height,
                                                 [Layer(grossberg_layer)])

    def train_competitive(self, traits, config, iterations):
        counterpropagation.train_competitive(self, traits, config, iterations)

    def train_neighborhood(self, traits, config, iterations):
        counterpropagation.train_neighborhood(self, traits, config, iterations)