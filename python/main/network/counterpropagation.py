__author__ = 'paoolo'

from kohonen import Kohonen
from network import Layer, Neuron

from main.trainer import counterpropagation


class CounterPropagation(Kohonen):
    def __init__(self, input_func=None, kohonen_func=None, grossberg_func=None, inputs=1, outputs=1, width=1, height=1):
        # create Grossberg output layer
        grossberg_layer = [Neuron(activation_func=grossberg_func, weights=[1.0] * width * height)
                           for _ in range(1, outputs)]

        # initialize Kohonen network
        super(CounterPropagation, self).__init__(input_func, kohonen_func, inputs, width, height,
                                                 [Layer(grossberg_layer)])

    def train_competitive(self, **kwargs):
        counterpropagation.train_competitive(self, **kwargs)

    def train_competitive_multi(self, traits, configs):
        for kwargs in configs:
            counterpropagation.train_competitive(self, traits, **kwargs)

    def train_neighborhood(self, **kwargs):
        counterpropagation.train_neighborhood(self, **kwargs)

    def train_neighborhood_multi(self, traits, configs):
        for kwargs in configs:
            counterpropagation.train_neighborhood(self, traits, **kwargs)