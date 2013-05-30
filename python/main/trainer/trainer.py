from main.const import ITERATIONS

__author__ = 'paoolo'


def train_multi(network, traits, train, configs):
    for config in configs:
        train(network, traits, config, config[ITERATIONS])