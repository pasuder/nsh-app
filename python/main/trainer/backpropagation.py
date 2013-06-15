from main.tools.function import normalize

__author__ = 'paoolo'

from main.function.trainer import backward


def train_backward(network, signal, target, iterations, learning_rate):
    trainer = backward(learning_rate)
    signal = normalize(signal)

    for iteration in xrange(iterations):
        trainer(network, target, iteration, signal)