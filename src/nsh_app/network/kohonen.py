__author__ = 'paoolo'

from nsh_app.trainer import kohonen
from network import Network, Layer, Neuron


class Kohonen(Network):
    def __init__(self, kohonen_func=None, inputs=1, width=1, height=1, output_layers=None):
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
                [Layer(kohonen_layer)] + ([] if output_layers is None else output_layers))

    def train_competitive(self, **kwargs):
        kohonen.train_competitive(self, **kwargs)

    def train_competitive_multi(self, traits, configs):
        for kwargs in configs:
            kohonen.train_competitive(self, traits, **kwargs)

    def train_neighborhood(self, **kwargs):
        kohonen.train_neighborhood(self, **kwargs)

    def train_neighborhood_multi(self, traits, configs):
        for kwargs in configs:
            kohonen.train_neighborhood(self, traits, **kwargs)
