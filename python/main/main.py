#!/usr/bin/python

__author__ = 'paoolo'

import sys
import re

import neuronal_network
import activation_function


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


active_func = {'linear': activation_function.linear,
               'linear_cut': activation_function.linear_cut,
               'threshold_unipolar': activation_function.threshold_unipolar,
               'threshold_bipolar': activation_function.threshold_unipolar,
               'sigmoid_unipolar': activation_function.sigmoid_unipolar,
               'sigmoid_bipolar': activation_function.sigmoid_bipolar,
               'gauss': activation_function.gauss}

NEW = r'new'
NEURON = r'neuron'
LAYER = r'layer'
NETWORK = r'network'

SHOW = r'show'
COMPUTE = r'compute'
CHANGE = r'change'

NEURONS = 'neurons'
LAYERS = 'layers'
NETWORKS = 'networks'


def parse_line(line, env):
    """
    Parse prompt line.

    Variable:
    FUNC
        : linear
        : linear_cut
        : threshold_unipolar
        : threshold_bipolar
        : sigmoid_unipolar
        : sigmoid_bipolar
        : gauss
    WEIGHTS
        : 1.0 1.0
    BIAS
        : 1.0

    Command:
    * new
        neuron
            NAME FUNC WEIGHTS BIAS
        layer
            NAME neurons...
        network
            NAME layers...
    * show
        neuron
            NAME
        layer
            NAME
        network
            NAME
    * compute
        neuron
            NAME INPUTS
        layer
            NAME INPUTS
        network
            NAME INPUTS

    Keyword arguments:
    line -- line read from keyboard
    context -- shell context, env variables
    """
    line = re.split(r'\s', re.sub(r'\s+', ' ', re.sub(r'^\s+', '', re.sub(r'\s+$', '', line))))

    if re.match(NEW, line[0]):
        if len(line) < 2:
            print 'Usage: new [neuron|layer|network] ...'

        else:
            if re.match(NEURON, line[1]):
                if len(line) < 6:
                    print 'Usage: new neuron NAME FUNC WEIGHTS BIAS\n\t' \
                          'FUNC\t: [linear|linear_cut|threshold_unipolar|threshold_bipolar|sigmoid_unipolar|sigmoid_bipolar|gauss]\n\t' \
                          'WEIGHTS\t: 1.0 1.2 ...\n\t' \
                          'BIAS\t: 1.0'

                else:
                    name = line[2]
                    func = active_func[line[3]]()
                    weights = map(lambda w: float(w), line[4:-1])
                    bias = float(line[-1])

                    neuron = neuronal_network.Neuron(func, weights, bias)
                    env[NEURONS][name] = neuron

            elif re.match(LAYER, line[1]):
                if len(line) < 4:
                    print 'Usage: new layer NAME NEURONS\n\tNEURONS\t: NAME NAME ...'

                else:
                    name = line[2]
                    neurons = map(lambda n: env[NEURONS][n], line[3:])

                    layer = neuronal_network.Layer(neurons)
                    env[LAYERS][name] = layer

            elif re.match(NETWORK, line[1]):
                if len(line) < 4:
                    print 'Usage: new network NAME LAYERS\n\tLAYERS\t: NAME NAME ...'

                else:
                    name = line[2]
                    layers = map(lambda l: env[LAYERS][l], line[3:])

                    network = neuronal_network.Network(layers)
                    env[NETWORKS][name] = network

    elif re.match(SHOW, line[0]):
        if len(line) < 3:
            print 'Usage: show [neuron|layer|network] NAME'

        else:
            if re.match(NEURON, line[1]):
                print env[NEURONS][line[2]]

            elif re.match(LAYER, line[1]):
                print env[LAYERS][line[2]]

            elif re.match(NETWORK, line[1]):
                print env[NETWORKS][line[2]]

    elif re.match(COMPUTE, line[0]):
        if len(line) < 4:
            print 'Usage: compute [neuron|layer|network] NAME INPUTS\n\tINPUTS\t: 1.0 1.0 ...'

        else:
            compute = lambda x: 'Ups!'
            if re.match(NEURON, line[1]):
                compute = env[NEURONS][line[2]]

            elif re.match(LAYER, line[1]):
                compute = env[LAYERS][line[2]]

            elif re.match(NETWORK, line[1]):
                compute = env[NETWORKS][line[2]]

            values = map(lambda i: float(i), line[3:])
            print compute.compute(values)


def shell():
    """
    Enable CLI for application.
    """
    print 'Neuronal shell'
    env = {NEURONS: {}, LAYERS: {}, NETWORKS: {}}
    try:
        sys.stdout.write('nsh> ')
        line = sys.stdin.readline()
        while line is not None:
            parse_line(line, env)
            sys.stdout.write('nsh> ')
            line = sys.stdin.readline()
    except KeyboardInterrupt:
        print ' Ouch...'
    print 'Bye!'


if __name__ == '__main__':
    quick_test()
    shell()