#!/usr/bin/python
import neuronal_network

__author__ = 'paoolo'


def quick_test():
    neurons = [neuronal_network.neuron_and(), neuronal_network.neuron_or()]
    for neuron in neurons:
        for val in [(0., 0.), (1., 0.), (0., 1.), (1., 1.)]:
            print neuron.compute(val)
    neuron = neuronal_network.neuron_not()
    for val in [0, 1]:
        print neuron.compute([val])

    print neuron

    layer = neuronal_network.Layer([neuron])
    print layer

    network = neuronal_network.Network([layer])
    print network


def parse_line(line, context):
    """
    Parse prompt line.

    Keyword arguments:
    line -- line read from keyboard
    context -- shell context, env variables
    """
    print line


def shell():
    print 'Neuronal shell'
    context = {}
    try:
        sys.stdout.write('nsh> ')
        line = sys.stdin.readline()
        while line is not None:
            parse_line(line, context)
            sys.stdout.write('nsh> ')
            line = sys.stdin.readline()
    except KeyboardInterrupt:
        print ' Ouch...'
    print 'Bye!'


if __name__ == '__main__':
    quick_test()