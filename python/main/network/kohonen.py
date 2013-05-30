__author__ = 'paoolo'

from network import Network, Layer, Neuron

from main.trainer import kohonen, trainer


class Kohonen(Network):
    def __init__(self, input_func, kohonen_func, inputs, width, height=1, output_layers=None):
        # create input layer with `inputs` neurons which have only one input
        input_layer = [Neuron(activation_func=input_func) for _ in range(0, inputs)]

        if height is 1:
            # create 1-dimensional Kohonen output layer
            kohonen_layer = [Neuron(activation_func=kohonen_func, weights=[1.0] * inputs, location=[x])
                             for x in range(0, width)]
        else:
            # create 2-dimensional Kohonen output layer
            kohonen_layer = []
            for y in range(0, height):
                kohonen_layer = kohonen_layer + [
                    Neuron(activation_func=kohonen_func, weights=[1.0] * inputs, location=[x, y])
                    for x in range(0, width)]

        # initialize network with Kohonen layers
        super(Kohonen, self).__init__(
            [Layer(input_layer), Layer(kohonen_layer)] + [] if output_layers is None else output_layers)

    def train_competitive(self, traits, config, iterations):
        kohonen.train_competitive(self, traits, config, iterations)

    def train_competitive_multi(self, traits, configs):
        trainer.train_multi(self, traits, kohonen.train_competitive, configs)

    def train_neighborhood(self, traits, config, iterations):
        kohonen.train_neighborhood(self, traits, config, iterations)

    def train_neighborhood_multi(self, traits, configs):
        trainer.train_multi(self, traits, kohonen.train_neighborhood, configs)