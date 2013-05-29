__author__ = 'paoolo'


def train_competitive_multi(network, traits, train, configs):
    for config in configs:
        train(network, traits, config, config['iterations'])


def train_neighborhood_multi(network, traits, train, configs):
    for config in configs:
        train(network, traits, config, config['iterations'])