__author__ = 'paoolo'

import re

from function import activation, learningrate, neighborhood, measures
from core import neuralnetwork as net, kohonen


activation_func = {'linear': activation.linear(),
                   'linear_cut': activation.linear_cut(),
                   'threshold_unipolar': activation.threshold_unipolar(),
                   'threshold_bipolar': activation.threshold_unipolar(),
                   'sigmoid_unipolar': activation.sigmoid_unipolar(),
                   'sigmoid_bipolar': activation.sigmoid_bipolar(),
                   'gauss': activation.gauss()}

learning_rate_func = {'linear': learningrate.linear(),
                      'power': learningrate.power(),
                      'exponential': learningrate.exponential()}

neighborhood_func = {'linear': neighborhood.linear(),
                     'exponential': neighborhood.exponential()}

measures_func = {'euclidean': measures.euclidean,
                 'scalar': measures.scalar,
                 'manhattan': measures.manhattan,
                 'manhattan_infinity': measures.manhattan_infinity}

info_text = {'neuron_not_added': 'Neuron "%s" not added',
             'neuron_added': 'Neuron "%s" added',
             'layer_not_added': 'Layer "%s" not added',
             'layer_added': 'Layer "%s" added',
             'network_not_added': 'Network "%s" not added',
             'network_added': 'Network "%s" added'}

error_text = {
    'activation_function_not_found': 'Activation function "%s" not found: %s.\n'
                                     'Available activation function:\n'
                                     '\tlinear\n'
                                     '\tlinear_cut\n'
                                     '\tthreshold_unipolar\n'
                                     '\tthreshold_bipolar\n'
                                     '\tsigmoid_unipolar\n'
                                     '\tsigmoid_bipolar\n'
                                     '\tgauss',
    'learning_rate_function_not_found': 'Learning rate function "%s" not found: %s.\n'
                                        'Available learning rate function:\n'
                                        '\tlinear\n'
                                        '\tpower\n'
                                        '\texponential',
    'neighborhood_function_not_found': 'Neighborhood function "%s" not found: %s.\n'
                                       'Available neighborhood function:\n'
                                       '\tlinear\n'
                                       '\texponential',
    'measures_function_not_found': 'Measures function "%s" not found: %s.\n'
                                   'Available measures function:\n'
                                   '\teuclidean\n'
                                   '\tscalar\n'
                                   '\tmanhattan\n'
                                   '\tmanhattan_infinity',
    'neuron_not_found': 'Neuron "%s" not found: %s',
    'layer_not_found': 'Layer "%s" not found: %s',
    'name_not_found': 'Name "%s" not found: %s',
    'file_not_found': 'File "%s" not found: %s'}

help_text = {
    '': 'Usage: new_neuron|new_layer|new_network|new_kohonen|'
        'show_all|show|compute|init|zero|load|locate|train_c|train_n',
    'new_neuron': 'Usage: new_neuron NAME FUNC WEIGHTS BIAS [location LOCATION]',
    'new_layer': 'Usage: new_layer NAME NEURONS',
    'new_network': 'Usage: new_network NAME LAYERS',
    'new_kohonen': 'Usage: new_kohonen NAME INPUT_FUNC OUTPUT_FUNC INPUTS WIDTH [HEIGHTS]',
    'show': 'Usage: show NAME',
    'compute': 'Usage: compute NAME INPUTS',
    'init': 'Usage: init NAME MIN MAX',
    'zero': 'Usage: zero NAME',
    'load': 'Usage: load NAME',
    'locate': 'Usage: locate NAME LOCATION',
    'train_c': 'Usage: train_c NAME LEARNING_RATE ITERATION TRAITS',
    'train_n': 'Usage: train_n NAME LEARNING_RATE MEASUREMENT NEIGHBORHOOD_RADIUS ITERATIONS TRAITS'}


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
        neuron = net.Neuron(func, weights, bias, location)
        env[name] = neuron
        print info_text['neuron_added'] % name
    else:
        print info_text['neuron_not_added'] % name

    return env


def new_layer(chunks, env):
    name = chunks[1]

    try:
        neurons = map(lambda n: env[n], chunks[2:])

        layer = net.Layer(neurons)
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

        network = net.Network(layers)
        env[name] = network
        print info_text['network_added'] % name
    except KeyError as e:
        print error_text['layer_not_found'] % ('', str(e.message))
        print info_text['network_not_added'] % name

    return env


def new_kohonen(chunks, env):
    name = chunks[1]

    try:
        input_func = activation_func[chunks[2]]
    except KeyError as e:
        print error_text['activation_function_not_found'] % (chunks[2], str(e.message))
        input_func = None

    try:
        output_func = activation_func[chunks[3]]
    except KeyError as e:
        print error_text['activation_function_not_found'] % (chunks[2], str(e.message))
        output_func = None

    inputs = int(chunks[4])
    width = int(chunks[5])

    if len(chunks) < 7:
        height = 1
    else:
        height = int(chunks[6])

    if input_func is not None and output_func is not None:
        env[name] = kohonen.Kohonen(input_func=input_func,
                                    output_func=output_func,
                                    inputs=inputs,
                                    width=width,
                                    height=height)
        print info_text['network_added'] % name
    else:
        print info_text['network_not_added'] % name

    return env


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
        env[chunks[1]].train_competitive(traits=map(lambda x: float(x), chunks[4:]),
                                         learning_rate=learning_rate_func[chunks[2]],
                                         iterations=int(chunks[3]))
    except KeyError as e:
        print 'Name ' + chunks[1] + ' not found: ' + str(e.message)
    except AttributeError as e:
        print chunks[1] + ' is not a Kohonen network: ' + str(e.message)
    return env


def train_n(chunks, env):
    try:
        env[chunks[1]].train_neighborhood(traits=map(lambda x: float(x), chunks[6:]),
                                          learning_rate=learning_rate_func[chunks[2]],
                                          measurement=measures_func[chunks[3]],
                                          neighborhood_radius=neighborhood_func[chunks[4]],
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