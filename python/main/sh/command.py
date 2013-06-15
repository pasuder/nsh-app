__author__ = 'paoolo'

import re

from interpreter import ENVIRONMENT, interpret

from main.network.network import Neuron, Layer, Network
from main.network.kohonen import Kohonen
from main.network.counterpropagation import CounterPropagation
from main.network.backpropagation import compute_error_on_network
from main.trainer import backpropagation


def show_all():
    out = 'List of all elements'
    for key in ENVIRONMENT:
        out += '\n\t' + key
    print out


def show(name):
    print ENVIRONMENT[name]


def load(source):
    try:
        source = open(source)
        for line in source:
            if not re.match(r'^(#.*)?$', line):
                interpret(line)
        source.close()
        print 'Loaded.'
    except IOError as e:
        print 'Error during loading file: %s' % e


def command_set_func(inner_func):
    def func(**kwargs):
        try:
            name = kwargs['name']
            del kwargs['name']
            ENVIRONMENT[name] = inner_func(kwargs)
        except AttributeError as e:
            print 'Cannot execute command: %s' % e

    return func


def command_get_func(inner_func):
    def func(**kwargs):
        try:
            name = kwargs['name']
            del kwargs['name']
            inner_func(ENVIRONMENT[name], kwargs)
        except AttributeError as e:
            print 'Cannot execute command: %s' % e

    return func


new_neuron = command_set_func(lambda kwargs: Neuron(**kwargs))
new_layer = command_set_func(lambda kwargs: Layer(**kwargs))
new_network = command_set_func(lambda kwargs: Network(**kwargs))

new_kohonen = command_set_func(lambda kwargs: Kohonen(**kwargs))
new_cp = command_set_func(lambda kwargs: CounterPropagation(**kwargs))

init = command_get_func(lambda obj, kwargs: obj.init(**kwargs))
init_bias = command_get_func(lambda obj, kwargs: obj.init_bias(**kwargs))

zero = command_get_func(lambda obj, kwargs: obj.zero())
zero_bias = command_get_func(lambda obj, kwargs: obj.zero_bias(**kwargs))

locate = command_get_func(lambda obj, kwargs: obj.locate(**kwargs))


def compute(**kwargs):
    name = kwargs['name']
    del kwargs['name']
    print 'Computation of ' + name \
          + '\n\tfor values ' + str(kwargs['values']) \
          + '\n\tis ' + str(ENVIRONMENT[name].compute(**kwargs))


from main.tools.function import normalize


def compute_error(**kwargs):
    name = kwargs['name']
    del kwargs['name']
    network = ENVIRONMENT[name]
    if isinstance(network, Network):
        kwargs['network'] = network
        error = compute_error_on_network(**kwargs)
        print 'Error of computation on network ' + name \
              + '\n\tfor values ' + str(kwargs['values']) \
              + '\n\tis ' + str(error)
    else:
        print '"' + name + '" is not a network'


def compute_normalize(**kwargs):
    name = kwargs['name']
    del kwargs['name']
    kwargs['values'] = normalize(kwargs['values'])
    print 'Computation of ' + name + '\n\tfor normalized values ' + str(kwargs['values']) + '\n\tis ' + str(
        ENVIRONMENT[name].compute(**kwargs))


train_c = command_get_func(lambda obj, kwargs: obj.train_competitive(**kwargs))
train_n = command_get_func(lambda obj, kwargs: obj.train_neighborhood(**kwargs))
train_bp = command_get_func(lambda obj, kwargs: backpropagation.train_backward(obj, **kwargs))


def multi_train(inner_func, params):
    @command_get_func
    def func(obj, kwargs):
        try:
            for config in kwargs['configs']:
                inner_kwargs = {key: value for (key, value) in zip(params, config[0:-1])}
                inner_kwargs['iterations'] = config[-1]
                inner_kwargs['signals'] = kwargs['signals']
                inner_func(obj, inner_kwargs)
        except AttributeError:
            print 'Cannot train network'

    return func


LEARNING_RATE = 'learning_rate'
MEASUREMENT = 'measurement'
NEIGHBORHOOD_RADIUS = 'neighborhood_radius'
GROSSBERG_PARAMETER = 'grossberg_parameter'

multi_train_c = multi_train(
    inner_func=lambda obj, kwargs: obj.train_competitive(**kwargs),
    params=[LEARNING_RATE])

multi_train_n = multi_train(
    inner_func=lambda obj, kwargs: obj.train_neighborhood(**kwargs),
    params=[LEARNING_RATE, MEASUREMENT, NEIGHBORHOOD_RADIUS]
)

multi_train_c_cp = multi_train(
    inner_func=lambda obj, kwargs: obj.train_competitive(**kwargs),
    params=[LEARNING_RATE, GROSSBERG_PARAMETER]
)

multi_train_n_cp = multi_train(
    inner_func=lambda obj, kwargs: obj.train_neighborhood(**kwargs),
    params=[LEARNING_RATE, MEASUREMENT, NEIGHBORHOOD_RADIUS, GROSSBERG_PARAMETER]
)
