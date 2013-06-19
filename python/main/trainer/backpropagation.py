import random
from main.tools.function import normalize

__author__ = 'paoolo'

from main.function.trainer import backward, backward_momentum


def train_backward(network, signals, targets, iterations, learning_rate):
    trainer = backward(learning_rate)
    signals = map(lambda signal: normalize(signal), signals)
    signals_and_targets = zip(signals, targets)

    for iteration in xrange(iterations):
        random.shuffle(signals_and_targets)
        for signal, target in signals_and_targets:
            trainer(network, target, iteration, signal)


def train_backward_momentum(network, signals, targets, iterations, learning_rate, momentum_rate):
    trainer = backward_momentum(learning_rate, momentum_rate)
    signals = map(lambda signal: normalize(signal), signals)
    signals_and_targets = zip(signals, targets)

    for iteration in xrange(iterations):
        random.shuffle(signals_and_targets)
        for signal, target in signals_and_targets:
            trainer(network, target, iteration, signal)