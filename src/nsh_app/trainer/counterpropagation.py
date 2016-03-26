__author__ = 'paoolo'

import random

from nsh_app.function.trainer import neighborhood, outstar, instar
from nsh_app.tools.function import normalize


def train_competitive(network, signals, targets, iterations, kohonen_learning_rate, grossberg_learning_rate):
    trainer_kohonen = instar(kohonen_learning_rate)
    trainer_grossberg = outstar(grossberg_learning_rate)
    signals = map(lambda signal: normalize(signal), signals)
    signals_excepted_values = zip(signals, targets)

    for iteration in xrange(iterations):
        random.shuffle(signals_excepted_values)
        for signal, excepted in signals_excepted_values:
            winners_indexes = network[0].get_winners_indexes(signal)
            for val in zip(network[0].get_winners(signal, winners_indexes), winners_indexes):
                trainer_kohonen(val[0], signal, iteration)
                winner_signal = val[0].compute(signal)
                signal_from_kohonen = network[0].compute(signal)
                trainer_grossberg(network[1], val[1], winner_signal, excepted, signal_from_kohonen, iteration)


def train_neighborhood(network, signals, targets, iterations, kohonen_learning_rate, grossberg_learning_rate,
                       measurement, neighborhood_radius):
    trainer_kohonen = neighborhood(kohonen_learning_rate, measurement, neighborhood_radius)
    trainer_grossberg = outstar(grossberg_learning_rate)
    signals = map(lambda signal: normalize(signal), signals)
    signals_excepted_values = zip(signals, targets)

    for iteration in xrange(iterations):
        random.shuffle(signals_excepted_values)
        for signal, excepted in signals_excepted_values:
            winners_indexes = network[0].get_winners_indexes(signal)
            for val in zip(network[0].get_winners(signal, winners_indexes), winners_indexes):
                for neuron_kohonen in network[0]:
                    trainer_kohonen(neuron_kohonen, val[0], signal, iteration)
                    winner_signal = val[0].compute(signal)
                    signal_from_kohonen = network[0].compute(signal)
                    trainer_grossberg(network[1], val[1], winner_signal, excepted, signal_from_kohonen, iteration)
