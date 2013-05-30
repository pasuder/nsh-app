__author__ = 'paoolo'

from main.function.learning import competitive, neighborhood, widrow_hoff
from main.const import LEARNING_RATE, MEASUREMENT, NEIGHBORHOOD_RADIUS, GROSSBERG_PARAMETER


def train_competitive(network, traits, config, iterations):
    trainer_kohonen = competitive(config[LEARNING_RATE])
    trainer_grossberg = widrow_hoff(config[GROSSBERG_PARAMETER])

    for iteration in range(0, iterations):
        winners_indexes = network[1].get_winners_indexes(traits)
        for winner, index in (network[1].get_winners(traits, winners_indexes), winners_indexes):
            trainer_kohonen(winner, traits, iteration)
            for neuron_grossberg in network[2]:
                trainer_grossberg(neuron_grossberg, winner, index, traits)


def train_neighborhood(network, traits, config, iterations):
    trainer_kohonen = neighborhood(config[LEARNING_RATE], config[MEASUREMENT], config[NEIGHBORHOOD_RADIUS])
    trainer_grossberg = widrow_hoff(config[GROSSBERG_PARAMETER])

    for iteration in range(0, iterations):
        winners_indexes = network[1].get_winners_indexes(traits)
        for winner, index in (network[1].get_winners(traits, winners_indexes), winners_indexes):
            for neuron_kohonen in network[1]:
                trainer_kohonen(neuron_kohonen, winner, traits, iteration)
                for neuron_grossberg in network[2]:
                    trainer_grossberg(neuron_grossberg, winner, index, traits)