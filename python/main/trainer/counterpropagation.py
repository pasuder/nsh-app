__author__ = 'paoolo'

from main.tools.function import normalize
from main.function.trainer import neighborhood, outstar, instar


def train_competitive(network, signals, iterations, kohonen_learning_rate, grossberg_learning_rate):
    trainer_kohonen = instar(kohonen_learning_rate)
    trainer_grossberg = outstar(grossberg_learning_rate)
    signals = normalize(signals)

    for iteration in range(1, iterations):
        winners_indexes = network[1].get_winners_indexes(signals)
        for val in zip(network[1].get_winners(signals, winners_indexes), winners_indexes):
            trainer_kohonen(val[0], signals, iteration)
            trainer_grossberg(network[2], val[1], signals, iteration)


def train_neighborhood(network, signals, iterations, kohonen_learning_rate, grossberg_learning_rate, measurement,
                       neighborhood_radius):
    trainer_kohonen = neighborhood(kohonen_learning_rate, measurement, neighborhood_radius)
    trainer_grossberg = outstar(grossberg_learning_rate)
    signals = normalize(signals)

    for iteration in range(1, iterations):
        winners_indexes = network[1].get_winners_indexes(signals)
        for val in zip(network[1].get_winners(signals, winners_indexes), winners_indexes):
            for neuron_kohonen in network[1]:
                trainer_kohonen(neuron_kohonen, val[0], signals, iteration)
                trainer_grossberg(network[2], val[1], signals, iteration)