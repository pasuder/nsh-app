__author__ = 'paoolo'

from main.tools.function import normalize
from main.function.learning import competitive, neighborhood


def train_competitive(network, traits, iterations, learning_rate):
    trainer = competitive(learning_rate)
    traits = normalize(traits)

    for iteration in range(1, iterations):
        for winner in network[1].get_winners(traits):
            trainer(winner, traits, iteration)


def train_neighborhood(network, traits, iterations, learning_rate, measurement, neighborhood_radius):
    trainer = neighborhood(learning_rate, measurement, neighborhood_radius)
    traits = normalize(traits)

    for iteration in range(1, iterations):
        for winner in network[1].get_winners(traits):
            for neuron in network[1]:
                trainer(neuron, winner, traits, iteration)