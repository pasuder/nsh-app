#!/usr/bin/python


__author__ = 'paoolo'

import getopt
import sys
import re

from core.function import activation as func
from core import neuralnetwork as net


active_func = {'linear': func.linear,
               'linear_cut': func.linear_cut,
               'threshold_unipolar': func.threshold_unipolar,
               'threshold_bipolar': func.threshold_unipolar,
               'sigmoid_unipolar': func.sigmoid_unipolar,
               'sigmoid_bipolar': func.sigmoid_bipolar,
               'gauss': func.gauss}

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


def normalize(line):
    return re.split(r'\s', re.sub(r'\s+', ' ', re.sub(r'^\s+', '', re.sub(r'\s+$', '', line))))


def parse_shell_line(line, env):
    """
    Parse prompt line.

    Neuron variables:
    FUNC
        : linear
        : linear_cut
        : threshold_unipolar
        : threshold_bipolar
        : sigmoid_unipolar
        : sigmoid_bipolar
        : gauss
    WEIGHTS
        : 1.0 1.0 ...
    BIAS
        : 1.0
    INPUTS
        : 1.0 1.0 ...

    Command:
    * new
        neuron
            NAME FUNC WEIGHTS BIAS
        layer
            NAME neurons...
        network
            NAME layers...
    * show NAME
    * compute NAME INPUTS

    Keyword arguments:
    line -- line read from keyboard
    context -- shell context, env variables
    """
    line = normalize(line)

    if re.match(NEW, line[0]):
        if len(line) < 2:
            print 'Usage: new [neuron|layer|network] ...'

        else:
            if re.match(NEURON, line[1]):
                if len(line) < 6:
                    print 'Usage: new neuron NAME FUNC WEIGHTS BIAS\n\t' \
                          'FUNC\t: [linear|' \
                          'linear_cut|' \
                          'threshold_unipolar|' \
                          'threshold_bipolar|' \
                          'sigmoid_unipolar|' \
                          'sigmoid_bipolar|' \
                          'gauss]\n\t' \
                          'WEIGHTS\t: 1.0 1.2 ...\n\t' \
                          'BIAS\t: 1.0'

                else:
                    name = line[2]
                    func = active_func[line[3]]()
                    weights = map(lambda w: float(w), line[4:-1])
                    bias = float(line[-1])

                    neuron = net.Neuron(func, weights, bias)
                    env[name] = neuron

            elif re.match(LAYER, line[1]):
                if len(line) < 4:
                    print 'Usage: new layer NAME NEURONS\n\tNEURONS\t: NAME NAME ...'

                else:
                    name = line[2]
                    neurons = map(lambda n: env[n], line[3:])

                    layer = net.Layer(neurons)
                    env[name] = layer

            elif re.match(NETWORK, line[1]):
                if len(line) < 4:
                    print 'Usage: new network NAME LAYERS\n\tLAYERS\t: NAME NAME ...'

                else:
                    name = line[2]
                    layers = map(lambda l: env[l], line[3:])

                    network = net.Network(layers)
                    env[name] = network

    elif re.match(SHOW, line[0]):
        if len(line) < 2:
            print 'Usage: show NAME'

        else:
            print env[line[1]]

    elif re.match(COMPUTE, line[0]):
        if len(line) < 3:
            print 'Usage: compute NAME INPUTS\n\tINPUTS\t: 1.0 1.0 ...'

        else:
            print env[line[1]].compute(map(lambda i: float(i), line[2:]))


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
            parse_shell_line(line, env)
            sys.stdout.write('nsh> ')
            line = sys.stdin.readline()
    except KeyboardInterrupt:
        print ' Ouch...'
    print 'Bye!'


def parse_batch_line(line, env):
    """
    Neuron variables:
        Activation function (FUNC):
            : linear
            : linear_cut
            : threshold_unipolar
            : threshold_bipolar
            : sigmoid_unipolar
            : sigmoid_bipolar
            : gauss
        Neuron weights (WEIGHTS):
            : 1.0 1.0 ...
        Bias (BIAS):
            : 1.0 ...
    Computation variables:
        Inputs (INPUTS):
            : 1.0 1.0 ...

    Example:

    $
    neuron NAME FUNC WEIGHTS BIAS
    layer NAME NEURONS
    network NAME LAYERS

    compute NAME INPUTS
    ^@

    """
    pass


def batch(source):
    """
    Parse file and compute.

    Keyword arguments:
    source -- opened file with data
    """
    i = 0
    env = {}
    for line in source:
        line = normalize(line)
        try:
            if re.match(NEURON, line[0]):
                name = line[1]
                func = active_func[line[2]]()
                weights = map(lambda w: float(w), line[3:-1])
                bias = float(line[-1])
                env[name] = net.Neuron(func, weights, bias)

            elif re.match(LAYER, line[0]):
                name = line[1]
                neurons = map(lambda n: env[n], line[2:])
                env[name] = net.Layer(neurons)

            elif re.match(NETWORK, line[0]):
                name = line[1]
                layers = map(lambda l: env[l], line[2:])
                env[name] = net.Network(layers)

            elif re.match(COMPUTE, line[0]):
                name = line[1]
                inputs = map(lambda i: float(i), line[2:])
                print env[name].compute(inputs)

            i += 1
        except IndexError:
            print 'Line ' + str(i) + ' is not well formatted. Parsed line "' + ' '.join(line) + '"'


def usage():
    print "Usage:\n" \
          "-h --help\tprint this help\n" \
          "-f --file\tselect input file"


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])

        source = None
        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o in ("-f", "--file"):
                source = open(a)
            else:
                assert False, "unhandled option"
        if source is None:
            shell()
        else:
            batch(source)
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(1)