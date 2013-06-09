__author__ = 'paoolo'

from main.tools.function import normalize
from main.function.trainer import instar, neighborhood


def train_competitive(network, signals, iterations, learning_rate):
    trainer = instar(learning_rate)
    signals = normalize(signals)

    for iteration in range(1, iterations):
        try:
            winner = network[1].get_winners(signals)[0]
            trainer(winner, signals, iteration)
        except IndexError:
            pass


def train_neighborhood(network, signals, iterations, learning_rate, measurement, neighborhood_radius):
    trainer = neighborhood(learning_rate, measurement, neighborhood_radius)
    signals = normalize(signals)

    for iteration in range(1, iterations):
        try:
            winner = network[1].get_winners(signals)[0]
            for neuron in network[1]:
                trainer(neuron, winner, signals, iteration)
        except IndexError:
            pass