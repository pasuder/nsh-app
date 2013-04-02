__author__ = 'paoolo'

import neuronal_network

if __name__ == '__main__':
    for neuron in [neuronal_network.neuron_and(), neuronal_network.neuron_or()]:
        for val in [(0., 0.), (1., 0.), (0., 1.), (1., 1.)]:
            print neuron.compute(val)
    neuron = neuronal_network.neuron_not()
    for val in [0, 1]:
        print neuron.compute([val])