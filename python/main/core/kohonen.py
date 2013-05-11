__author__ = 'paoolo'

from function.learning import competitive, neighborhood
from neuralnetwork import Network, Layer, Neuron


class Kohonen(Network):
    def __init__(self, input_func, output_func, inputs, width, height=1):
        input_layer = [Neuron(active_func=input_func) for x in range(0, inputs)]
        if height == 1:
            output_layer = [Neuron(active_func=output_func, weights=[1.0] * inputs, location=[x])
                            for x in range(0, width)]
        else:
            output_layer = []
            for y in range(0, height):
                output_layer = output_layer + [
                    Neuron(active_func=output_func, weights=[1.0] * inputs, location=[x, y])
                    for x in range(0, width)]
        layers = [Layer(input_layer), Layer(output_layer)]
        super(Kohonen, self).__init__(layers)

    def train_competitive(self, traits, learning_rate, iterations):
        trainer = competitive(learning_rate)

        for iteration in range(0, iterations):
            result = self.compute(traits)
            winners = map(lambda index: self.layers[1].neurons[index],
                          [i for i, j in enumerate(result) if j == max(result)])
            for winner in winners:
                trainer(winner, traits, iteration)

    def train_neighborhood(self, traits, learning_rate, measurement, neighborhood_radius, iterations):
        trainer = neighborhood(learning_rate, measurement, neighborhood_radius)

        for iteration in range(0, iterations):
            result = self.compute(traits)
            winners = map(lambda index: self.layers[1].neurons[index],
                          [i for i, j in enumerate(result) if j == max(result)])
            for winner in winners:
                for neuron in self.layers[1]:
                    trainer(neuron, winner, traits, iteration)