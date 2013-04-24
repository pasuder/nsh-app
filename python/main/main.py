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

COMPUTE = r'compute'
LIST = r'list'
SHOW = r'show'
INIT = r'init'
ZERO = r'zero'
LOAD = r'load'
LOCATE = r'locate'


def normalize(line):
    return re.split(r'\s', re.sub(r'\s+', ' ', re.sub(r'^\s+', '', re.sub(r'\s+$', '', line))))


def first_index(what, sequence):
    return reduce(lambda t, w: (t[0], True) if not t[1] and w == what else (
        t[0] + 1 if not t[1] else t[0], t[1]), sequence, (0, False))[0]


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
    LOCATION
        : 1.0 1.0 ...

    Command:
    * new
        neuron
            NAME FUNC WEIGHTS BIAS [location LOCATION]
        layer
            NAME neurons...
        network
            NAME layers...
    * list
    * show NAME
    * compute NAME INPUTS
    * init NAME
    * zero NAME
    * locate NAME

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
                    print 'Usage: new neuron NAME FUNC WEIGHTS BIAS [location LOCATION]\n\t' \
                          'FUNC\t: [linear|' \
                          'linear_cut|' \
                          'threshold_unipolar|' \
                          'threshold_bipolar|' \
                          'sigmoid_unipolar|' \
                          'sigmoid_bipolar|' \
                          'gauss]\n\t' \
                          'WEIGHTS\t: 1.0 1.2 ...\n\t' \
                          'BIAS\t: 1.0\n\y' \
                          'LOCATION\t: 1.0 1.0 1.0...'

                else:
                    name = line[2]
                    func = active_func[line[3]]()
                    location = first_index('location', line)
                    weights = map(lambda w: float(w), line[4:location - 1])
                    bias = float(line[location - 1])
                    location = map(lambda x: float(x), line[location + 1:])

                    neuron = net.Neuron(func, weights, bias, location)
                    env[name] = neuron

            elif re.match(LAYER, line[1]):
                if len(line) < 4:
                    print 'Usage: new layer NAME NEURONS\n\tNEURONS\t: NAME NAME ...'

                else:
                    name = line[2]
                    try:
                        neurons = map(lambda n: env[n], line[3:])

                        layer = net.Layer(neurons)
                        env[name] = layer
                    except KeyError as e:
                        print 'Neuron not found: ' + e.message

            elif re.match(NETWORK, line[1]):
                if len(line) < 4:
                    print 'Usage: new network NAME LAYERS\n\tLAYERS\t: NAME NAME ...'

                else:
                    name = line[2]
                    try:
                        layers = map(lambda l: env[l], line[3:])

                        network = net.Network(layers)
                        env[name] = network
                    except KeyError as e:
                        print 'Layer not found: ' + e.message

    elif re.match(LIST, line[0]):
        for k in env:
            print '\t' + k

    elif re.match(SHOW, line[0]):
        if len(line) < 2:
            print 'Usage: show NAME'

        else:
            try:
                print env[line[1]]
            except KeyError:
                print 'Name ' + line[1] + ' not found'

    elif re.match(COMPUTE, line[0]):
        if len(line) < 3:
            print 'Usage: compute NAME INPUTS\n\tINPUTS\t: 1.0 1.0 ...'

        else:
            try:
                print env[line[1]].compute(map(lambda i: float(i), line[2:]))
            except KeyError:
                print 'Name ' + line[1] + 'not found'

    elif re.match(INIT, line[0]):
        if len(line) < 2:
            print 'Usage: init NAME'

        else:
            try:
                env[line[1]].init()
            except KeyError:
                print 'Name ' + line[1] + ' not found'

    elif re.match(ZERO, line[0]):
        if len(line) < 2:
            print 'Usage: zero NAME'

        else:
            try:
                env[line[1]].zero()
            except KeyError:
                print 'Name ' + line[1] + ' not found'

    elif re.match(LOAD, line[0]):
        if len(line) < 2:
            print 'Usage: load NAME'

        else:
            env = batch(open(line[1]), env)
            print 'Loaded.'

    elif re.match(LOCATE, line[0]):
        if len(line) < 2:
            print 'Usage: locate NAME LOCATION'

        else:
            try:
                env[line[1]].locate(map(lambda x: float(x), line[2:]))
            except KeyError:
                print 'Name ' + line[1] + 'not found'
            except BaseException as e:
                print 'Cannot set location on ' + line[1] + ': ' + e.message

    else:
        print 'Usage: new|show|compute|init|zero|load|list|locate'

    return env


def shell():
    """
    Enable CLI for application.
    """
    print 'Neuronal shell'
    env = {}
    try:
        sys.stdout.write('nsh> ')
        line = sys.stdin.readline()
        while line is not None:
            env = parse_shell_line(line, env)
            sys.stdout.write('nsh> ')
            line = sys.stdin.readline()
    except KeyboardInterrupt:
        print ' Ouch...'
    print 'Bye!'


def batch(source, env=None):
    """
    Parse file and compute.

    Keyword arguments:
    source -- opened file with data
    """
    if not env:
        env = {}
    i = 0
    for line in source:
        line = normalize(line)
        try:
            if re.match(NEURON, line[0]):
                name = line[1]
                func = active_func[line[2]]()
                location = first_index('location', line)
                weights = map(lambda w: float(w), line[3:location - 1])
                bias = float(line[location - 1])
                location = map(lambda x: float(x), line[location + 1:])
                env[name] = net.Neuron(func, weights, bias, location)

            elif re.match(LAYER, line[0]):
                name = line[1]
                try:
                    neurons = map(lambda n: env[n], line[2:])
                    env[name] = net.Layer(neurons)
                except KeyError as e:
                    print 'Neuron not found: ' + e.message

            elif re.match(NETWORK, line[0]):
                name = line[1]
                try:
                    layers = map(lambda l: env[l], line[2:])
                    env[name] = net.Network(layers)
                except KeyError as e:
                    print 'Layer not found: ' + e.message

            elif re.match(COMPUTE, line[0]):
                name = line[1]
                inputs = map(lambda i: float(i), line[2:])
                try:
                    print env[name].compute(inputs)
                except KeyError as e:
                    print 'Name ' + name + ' not found: ' + e.message

            i += 1
        except IndexError as e:
            print 'Line ' + str(i) + ' is not well formatted. Parsed line "' + ' '.join(line) + '". ' + e.message

    return env


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