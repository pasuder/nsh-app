__author__ = 'paoolo'

import re

from network.network import Neuron, Layer, Network
from network.kohonen import Kohonen
from network.counterpropagation import CounterPropagation

from const import activation_func, error_text, info_text, learning_rate_func, measures_func, neighborhood_func, \
    help_text, LEARNING_RATE, MEASUREMENT, NEIGHBORHOOD_RADIUS


def normalize(line):
    return re.split(r'\s', re.sub(r'\s+', ' ', re.sub(r'^\s+', '', re.sub(r'\s+$', '', line))))


def first_index(what, sequence):
    return reduce(lambda t, w: (t[0], True) if not t[1] and w == what else (
        t[0] + 1 if not t[1] else t[0], t[1]), sequence, (0, False))[0]


def new_neuron(chunks, env):
    name = chunks[1]

    try:
        func = activation_func[chunks[2]]
    except KeyError as e:
        print error_text['activation_function_not_found'] % (chunks[2], str(e.message))
        func = None

    location = first_index('location', chunks)
    weights = map(lambda w: float(w), chunks[3:location - 1])
    bias = float(chunks[location - 1])
    location = map(lambda x: float(x), chunks[location + 1:])

    if func is not None:
        neuron = Neuron(func, weights, bias, location)
        env[name] = neuron
        print info_text['neuron_added'] % name
    else:
        print info_text['neuron_not_added'] % name

    return env


def new_layer(chunks, env):
    name = chunks[1]

    try:
        neurons = map(lambda n: env[n], chunks[2:])

        layer = Layer(neurons)
        env[name] = layer
        print info_text['layer_added'] % name
    except KeyError as e:
        print error_text['neuron_not_found'] % ('', str(e.message))
        print info_text['layer_not_added'] % name

    return env


def new_network(chunks, env):
    name = chunks[1]

    try:
        layers = map(lambda l: env[l], chunks[2:])

        network = Network(layers)
        env[name] = network
        print info_text['network_added'] % name
    except KeyError as e:
        print error_text['layer_not_found'] % ('', str(e.message))
        print info_text['network_not_added'] % name

    return env


def get_activation_func(name):
    try:
        return activation_func[name]
    except KeyError as e:
        print error_text['activation_function_not_found'] % (name, str(e.message))
        return None


def new_kohonen(chunks, env):
    name = chunks[1]

    input_func = get_activation_func(chunks[2])
    kohonen_func = get_activation_func(chunks[3])

    inputs = int(chunks[4])
    width = int(chunks[5])

    if len(chunks) < 7:
        height = 1
    else:
        height = int(chunks[6])

    if input_func is not None and kohonen_func is not None:
        env[name] = Kohonen(input_func=input_func,
                            kohonen_func=kohonen_func,
                            inputs=inputs,
                            width=width,
                            height=height)
        print info_text['network_added'] % name
    else:
        print info_text['network_not_added'] % name

    return env


def new_cp(chunks, env):
    name = chunks[1]

    input_func = get_activation_func(chunks[2])
    kohonen_func = get_activation_func(chunks[3])
    grossberg_func = get_activation_func(chunks[4])

    inputs = int(chunks[5])
    outputs = int(chunks[6])
    width = int(chunks[7])

    if len(chunks) < 8:
        height = 1
    else:
        height = int(chunks[6])

    if input_func is not None and kohonen_func is not None and grossberg_func is not None:
        env[name] = CounterPropagation(input_func=input_func,
                                       kohonen_func=kohonen_func,
                                       grossberg_func=grossberg_func,
                                       inputs=inputs,
                                       outputs=outputs,
                                       width=width,
                                       height=height)
        print info_text['network_added'] % name
    else:
        print info_text['network_not_added'] % name


def show_all(chunks, env):
    for k in env:
        print '\t' + k
    return env


def show(chunks, env):
    try:
        print env[chunks[1]]
    except KeyError as e:
        print error_text['name_not_found'] % (chunks[1], e.message)
    return env


def compute(chunks, env):
    try:
        print env[chunks[1]].compute(map(lambda i: float(i), chunks[2:]))
    except KeyError as e:
        print error_text['name_not_found'] % (chunks[1], e.message)
    return env


def init(chunks, env):
    env[chunks[1]].init(min_value=float(chunks[2]), max_value=float(chunks[3]))
    return env


def zero(chunks, env):
    try:
        env[chunks[1]].zero()
    except KeyError as e:
        print error_text['name_not_found'] % (chunks[1], e.message)
    return env


def load(chunks, env):
    try:
        source = open(chunks[1])
        for line in source:
            if not re.match(r'^(#.*)?$', line):
                env = parse(line, env)
        print 'Loaded.'
    except IOError as e:
        print error_text['file_not_found'] % (chunks[1], e.message)
    return env


def locate(chunks, env):
    try:
        env[chunks[1]].locate(map(lambda x: float(x), chunks[2:]))
    except KeyError:
        print 'Name ' + chunks[1] + ' not found'
    except BaseException as e:
        print 'Cannot set location on ' + chunks[1] + ': ' + str(e.message)
    return env


def train_c(chunks, env):
    try:
        config = {LEARNING_RATE: learning_rate_func[chunks[2]]}
        env[chunks[1]].train_competitive(traits=map(lambda x: float(x), chunks[4:]),
                                         config=config,
                                         iterations=int(chunks[3]))
    except KeyError as e:
        print 'Name ' + chunks[1] + ' not found: ' + str(e.message)
    except AttributeError as e:
        print chunks[1] + ' is not a Kohonen network: ' + str(e.message)
    return env


def train_n(chunks, env):
    try:
        config = {LEARNING_RATE: learning_rate_func[chunks[2]], MEASUREMENT: measures_func[chunks[3]],
                  NEIGHBORHOOD_RADIUS: neighborhood_func[chunks[4]]}
        env[chunks[1]].train_neighborhood(traits=map(lambda x: float(x), chunks[6:]),
                                          config=config,
                                          iterations=int(chunks[5]))
    except KeyError as e:
        print 'Name ' + chunks[1] + ' not found: ' + str(e.message)
    except AttributeError as e:
        print chunks[1] + ' is not a Kohonen network: ' + str(e.message)
    return env


function = {'new_neuron': (5, new_neuron),
            'new_layer': (3, new_layer),
            'new_network': (3, new_network),
            'new_kohonen': (6, new_kohonen),
            'new_cp': (7, new_cp),
            'show_all': (1, show_all),
            'show': (2, show),
            'compute': (3, compute),
            'init': (3, init),
            'zero': (2, zero),
            'load': (2, load),
            'locate': (2, locate),
            'train_c': (4, train_c),
            'train_n': (6, train_n)}


def parse(line, env):
    line = normalize(line)
    if len(line) > 0:
        try:
            if len(line) < function[line[0]][0]:
                print help_text[line[0]]
            else:
                env = function[line[0]][1](line, env)
        except KeyError:
            print help_text['']
    else:
        print help_text['']
    return env