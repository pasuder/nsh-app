__author__ = 'paoolo'

from main.function.learning import competitive, neighborhood, widrow_hoff
from main.const import LEARNING_RATE, MEASUREMENT, NEIGHBORHOOD_RADIUS, GROSSBERG_PARAMETER


def train_competitive(network, traits, config, iterations):
    kohonen_trainer = competitive(config['learning_rate'])
    grossberg_trainer = widrow_hoff(config['mi'], config['kj'])

    for iteration in range(0, iterations):
        for winner in network[1].get_winners(traits):
            kohonen_trainer(winner, traits, iteration)
            for neuron_kohonen in network[2].get_winners(traits):
                grossberg_trainer(neuron_kohonen, winner, traits)


def train_neighborhood(network, traits, config, iterations):
    kohonen_trainer = neighborhood(config[LEARNING_RATE], config[MEASUREMENT], config[NEIGHBORHOOD_RADIUS])
    grossberg_trainer = widrow_hoff(config[GROSSBERG_PARAMETER], config['kj'])

    for iteration in range(0, iterations):
        for winner in network[1].get_winners(traits):
            for neuron_kohonen in network[1]:
                kohonen_trainer(neuron_kohonen, winner, traits, iteration)
                for neuron_grossberg in network[2]:
                    grossberg_trainer(neuron_grossberg, winner, traits)