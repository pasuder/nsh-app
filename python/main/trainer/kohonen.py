__author__ = 'paoolo'

from main.function.learning import competitive, neighborhood
from main.const import LEARNING_RATE, MEASUREMENT, NEIGHBORHOOD_RADIUS


def train_competitive(network, traits, config, iterations):
    trainer = competitive(config[LEARNING_RATE])

    for iteration in range(0, iterations):
        for winner in network[1].get_winners(traits):
            trainer(winner, traits, iteration)


def train_neighborhood(network, traits, config, iterations):
    trainer = neighborhood(config[LEARNING_RATE], config[MEASUREMENT], config[NEIGHBORHOOD_RADIUS])

    for iteration in range(0, iterations):
        for winner in network[1].get_winners(traits):
            for neuron in network[1]:
                trainer(neuron, winner, traits, iteration)