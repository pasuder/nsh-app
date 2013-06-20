__author__ = 'paoolo'

import random

from main.tools.function import normalize
from main.function.trainer import instar, neighborhood


def train_competitive(network, signals, iterations, learning_rate):
    trainer = instar(learning_rate)
    signals = map(lambda signal: normalize(signal), signals)

    for iteration in xrange(iterations):
        random.shuffle(signals)
        for signal in signals:
            winner = network[0].get_winners(signal)[0]
            trainer(winner, signal, iteration)


def train_neighborhood(network, signals, iterations, learning_rate, measurement, neighborhood_radius):
    trainer = neighborhood(learning_rate, measurement, neighborhood_radius)
    signals = map(lambda signal: normalize(signal), signals)

    for iteration in xrange(iterations):
        random.shuffle(signals)
        for signal in signals:
            winner = network[0].get_winners(signal)[0]
            for neuron in network[0]:
                trainer(neuron, winner, signal, iteration)