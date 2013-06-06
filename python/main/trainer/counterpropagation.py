__author__ = 'paoolo'

from main.tools.function import normalize
from main.function.learning import competitive, neighborhood, widrow_hoff


def train_competitive(network, traits, iterations, learning_rate, grossberg_parameter):
    trainer_kohonen = competitive(learning_rate)
    trainer_grossberg = widrow_hoff(grossberg_parameter)
    traits = normalize(traits)

    for iteration in range(1, iterations):
        winners_indexes = network[1].get_winners_indexes(traits)
        for val in zip(network[1].get_winners(traits, winners_indexes), winners_indexes):
            trainer_kohonen(val[0], traits, iteration)
            for neuron_grossberg in network[2]:
                trainer_grossberg(neuron_grossberg, val[0], val[1], traits)


def train_neighborhood(network, traits, iterations, learning_rate, measurement, neighborhood_radius,
                       grossberg_parameter):
    trainer_kohonen = neighborhood(learning_rate, measurement, neighborhood_radius)
    trainer_grossberg = widrow_hoff(grossberg_parameter)
    traits = normalize(traits)

    for iteration in range(1, iterations):
        winners_indexes = network[1].get_winners_indexes(traits)
        for val in zip(network[1].get_winners(traits, winners_indexes), winners_indexes):
            for neuron_kohonen in network[1]:
                trainer_kohonen(neuron_kohonen, val[0], traits, iteration)
                for neuron_grossberg in network[2]:
                    trainer_grossberg(neuron_grossberg, val[0], val[1], traits)