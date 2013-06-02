import sys
import traceback

__author__ = 'paoolo'

import re

from network.network import Neuron, Layer, Network
from network.kohonen import Kohonen
from network.counterpropagation import CounterPropagation

from main.const import LEARNING_RATE, MEASUREMENT, NEIGHBORHOOD_RADIUS, ACTIVATION_FUNC, LEARNING_RATE_FUNC, \
    NEIGHBORHOOD_FUNC, MEASUREMENT_FUNC, ERROR_TEXT, GROSSBERG_PARAMETER


ENVIRONMENT = {}


def new_neuron(name, func, weights, bias, location):
    if func is not None:
        neuron = Neuron(func, weights, bias, location)
        ENVIRONMENT[name] = neuron


def new_layer(name, neurons):
    layer = Layer(neurons)
    ENVIRONMENT[name] = layer


def new_network(name, layers):
    network = Network(layers)
    ENVIRONMENT[name] = network


def new_kohonen(name, input_func, kohonen_func, inputs, width, height):
    if input_func is not None and kohonen_func is not None:
        ENVIRONMENT[name] = Kohonen(input_func=input_func, kohonen_func=kohonen_func,
                                    inputs=inputs, width=width, height=height)


def new_cp(name, input_func, kohonen_func, grossberg_func, inputs, outputs, width, height):
    if input_func is not None and kohonen_func is not None and grossberg_func is not None:
        ENVIRONMENT[name] = CounterPropagation(input_func=input_func,
                                               kohonen_func=kohonen_func,
                                               grossberg_func=grossberg_func,
                                               inputs=inputs, outputs=outputs,
                                               width=width, height=height)


def init_weights(obj, min_value, max_value):
    if obj is not None:
        obj.init(min_value=min_value, max_value=max_value)


def zero_weights(obj):
    if obj is not None:
        obj.zero()


def set_location(obj, location):
    if obj is not None:
        try:
            obj.locate(location)
        except AttributeError:
            print 'Cannot set location'


def show_all():
    out = 'List of all elements'
    for key in ENVIRONMENT:
        out += '\n\t' + key
    print out


def show(obj):
    if obj is not None:
        print obj


def compute(obj, values):
    if obj is not None:
        print obj.compute(values)


def load(source):
    try:
        for line in source:
            if not re.match(r'^(#.*)?$', line):
                parse(line)
        print 'Loaded.'
    except IOError as e:
        print 'Error during loading file: %s' % e


def train_c(obj, learning_rate_func, iteration, traits):
    if obj is not None and learning_rate_func is not None and iteration is not None:
        try:
            config = {LEARNING_RATE: learning_rate_func}
            obj.train_competitive(traits=traits, config=config, iterations=iteration)
        except AttributeError:
            print 'Cannot train Kohonen network using competitive mode'


def train_n(obj, learning_rate_func, measurement_func, neighborhood_radius_func, iterations, traits):
    if obj is not None and learning_rate_func is not None and \
                    measurement_func is not None and neighborhood_radius_func is not None:
        try:
            config = {LEARNING_RATE: learning_rate_func,
                      MEASUREMENT: measurement_func,
                      NEIGHBORHOOD_RADIUS: neighborhood_radius_func}
            obj.train_neighborhood(traits=traits, config=config, iterations=iterations)
        except AttributeError:
            print 'Cannot train Kohonen network using neighborhood mode'


def train_c_cp(obj, learning_rate_func, grossberg_parameter, iteration, traits):
    if obj is not None and learning_rate_func is not None and grossberg_parameter is not None and iteration is not None:
        try:
            config = {LEARNING_RATE: learning_rate_func,
                      GROSSBERG_PARAMETER: grossberg_parameter}
            obj.train_competitive(traits=traits, config=config, iterations=iteration)
        except AttributeError:
            print 'Cannot train CP network using competitive mode'


def train_n_cp(obj, learning_rate_func, measurement_func, neighborhood_radius_func, grossberg_parameter, iterations,
               traits):
    if obj is not None and learning_rate_func is not None and grossberg_parameter is not None and \
                    measurement_func is not None and neighborhood_radius_func is not None:
        try:
            config = {LEARNING_RATE: learning_rate_func,
                      GROSSBERG_PARAMETER: grossberg_parameter,
                      MEASUREMENT: measurement_func,
                      NEIGHBORHOOD_RADIUS: neighborhood_radius_func}
            obj.train_neighborhood(traits=traits, config=config, iterations=iterations)
        except AttributeError:
            print 'Cannot train CP network using neighborhood mode'


def multi_train(inner_func, params):
    def func(obj, traits, configs):
        if obj is not None and traits is not None and configs is not None:
            try:
                for config in configs:
                    iterations = config[-1]
                    config = {key: value for (key, value) in zip(params, config[0:-1])}
                    inner_func(obj, traits, config, iterations)
            except AttributeError:
                print 'Cannot train network'

    return func


multi_train_c = multi_train(
    inner_func=lambda obj, traits, config, iterations: obj.train_competitive(traits, config, iterations),
    params=[LEARNING_RATE])

multi_train_n = multi_train(
    inner_func=lambda obj, traits, config, iterations: obj.train_neighborhood(traits, config, iterations),
    params=[LEARNING_RATE, MEASUREMENT, NEIGHBORHOOD_RADIUS]
)

multi_train_c_cp = multi_train(
    inner_func=lambda obj, traits, config, iterations: obj.train_competitive(traits, config, iterations),
    params=[LEARNING_RATE, GROSSBERG_PARAMETER]
)

multi_train_n_cp = multi_train(
    inner_func=lambda obj, traits, config, iterations: obj.train_neighborhood(traits, config, iterations),
    params=[LEARNING_RATE, MEASUREMENT, NEIGHBORHOOD_RADIUS, GROSSBERG_PARAMETER]
)


def error_handler(inner_func, error_text, error_type=BaseException):
    def func(*args, **kwargs):
        try:
            return inner_func(*args, **kwargs)
        except error_type as e:
            print '%s: %s' % (error_text, e)
            return None

    return func


def value_error_handler(inner_func, error_text):
    return error_handler(inner_func, error_text, ValueError)


def key_error_handler(inner_func, error_text):
    return error_handler(inner_func, error_text, KeyError)


def io_error_handler(inner_func, error_text):
    return error_handler(inner_func, error_text, IOError)


def get_func(func_dict):
    def inner_func(val):
        val = val.split(',')
        if val > 0:
            args = map(lambda arg: float(arg), val[1:])
            return func_dict[val[0]](*args)

    return inner_func


GET_ACTIVATION_FUNC = key_error_handler(get_func(ACTIVATION_FUNC), ERROR_TEXT['activation_function_not_found'])
GET_LEARNING_RATE_FUNC = key_error_handler(get_func(LEARNING_RATE_FUNC), ERROR_TEXT['learning_rate_function_not_found'])
GET_NEIGHBORHOOD_FUNC = key_error_handler(get_func(NEIGHBORHOOD_FUNC), ERROR_TEXT['neighborhood_function_not_found'])
GET_MEASUREMENT_FUNC = key_error_handler(lambda val: MEASUREMENT_FUNC[val], ERROR_TEXT['measures_function_not_found'])

GET_OBJECT = key_error_handler(lambda val: ENVIRONMENT[val], ERROR_TEXT['object_not_found'])
GET_OBJECTS = lambda val: map(GET_OBJECT, val.split(','))

TO_STR = lambda val: val
TO_INT = value_error_handler(lambda val: int(val), 'Cannot convert value to integer')
TO_FLOAT = value_error_handler(lambda val: float(val), 'Cannot convert value to float')
TO_FILE = io_error_handler(lambda val: open(val), 'Cannot open file')

TO_INTS = lambda val: map(TO_INT, val.split(','))
TO_FLOATS = lambda val: map(TO_FLOAT, val.split(','))


def GET_CONFIG_C(line):
    return map(lambda val: val[0](val[1]), zip([GET_ACTIVATION_FUNC, TO_INT], line.split(';')))


def GET_CONFIG_N(line):
    return map(lambda val: val[0](val[1]),
               zip([GET_ACTIVATION_FUNC, GET_MEASUREMENT_FUNC, GET_NEIGHBORHOOD_FUNC, TO_INT], line.split(';')))


GET_CONFIGS_C = lambda val: map(GET_CONFIG_C, val.split('|'))
GET_CONFIGS_N = lambda val: map(GET_CONFIG_N, val.split('|'))

commands = {
    'new_neuron': {
        'function': new_neuron,
        'params': [
            ('name', TO_STR),
            ('func', GET_ACTIVATION_FUNC),
            ('weights', TO_FLOATS),
            ('bias', TO_FLOAT),
            ('location', TO_INTS)
        ],
    },
    'new_layer': {
        'function': new_layer,
        'params': [
            ('name', TO_STR),
            ('neurons', GET_OBJECTS)
        ]
    },
    'new_network': {
        'function': new_network,
        'params': [
            ('name', TO_STR),
            ('layers', GET_OBJECTS)
        ]
    },
    'new_kohonen': {
        'function': new_kohonen,
        'params': [
            ('name', TO_STR),
            ('input_func', GET_ACTIVATION_FUNC),
            ('kohonen_func', GET_ACTIVATION_FUNC),
            ('inputs', TO_INT),
            ('width', TO_INT),
            ('height', TO_INT)
        ]
    },
    'new_cp': {
        'function': new_cp,
        'params': [
            ('name', TO_STR),
            ('input_func', GET_ACTIVATION_FUNC),
            ('kohonen_func', GET_ACTIVATION_FUNC),
            ('grossberg_func', GET_ACTIVATION_FUNC),
            ('inputs', TO_INT),
            ('outputs', TO_INT),
            ('width', TO_INT),
            ('height', TO_INT)
        ]
    },
    'init_weights': {
        'function': init_weights,
        'params': [
            ('name', GET_OBJECT),
            ('min', TO_FLOAT),
            ('max', TO_FLOAT)
        ]
    },
    'zero_weights': {
        'function': zero_weights,
        'params': [
            ('name', GET_OBJECT)
        ]
    },
    'set_location': {
        'function': set_location,
        'params': [
            ('name', GET_OBJECT),
            ('location', TO_INTS)
        ]
    },
    'show_all': {
        'function': show_all,
        'params': []
    },
    'show': {
        'function': show,
        'params': [
            ('name', GET_OBJECT)
        ]
    },
    'compute': {
        'function': compute,
        'params': [
            ('name', GET_OBJECT),
            ('values', TO_FLOATS)
        ]
    },
    'load': {
        'function': load,
        'params': [
            ('file_name', TO_FILE)
        ]
    },
    'train_c': {
        'function': train_c,
        'params': [
            ('name', GET_OBJECT),
            ('learning_rate_func', GET_LEARNING_RATE_FUNC),
            ('iteration', TO_INT),
            ('traits', TO_FLOATS)
        ]
    },
    'train_n': {
        'function': train_n,
        'params': [
            ('name', GET_OBJECT),
            ('learning_rate_func', GET_LEARNING_RATE_FUNC),
            ('measurement_func', GET_MEASUREMENT_FUNC),
            ('neighborhood_radius_func', GET_NEIGHBORHOOD_FUNC),
            ('iterations', TO_INT),
            ('traits', TO_FLOATS)
        ]
    },
    'train_c_cp': {
        'function': train_c_cp,
        'params': [
            ('name', GET_OBJECT),
            ('learning_rate_func', GET_LEARNING_RATE_FUNC),
            ('grossberg_parameter', TO_FLOAT),
            ('iteration', TO_INT),
            ('traits', TO_FLOATS)
        ]
    },
    'train_n_cp': {
        'function': train_n_cp,
        'params': [
            ('name', GET_OBJECT),
            ('learning_rate_func', GET_LEARNING_RATE_FUNC),
            ('measurement_func', GET_MEASUREMENT_FUNC),
            ('neighborhood_radius_func', GET_NEIGHBORHOOD_FUNC),
            ('grossberg_parameter', TO_FLOAT),
            ('iterations', TO_INT),
            ('traits', TO_FLOATS)
        ]
    },
    'multi_train_c': {
        'function': multi_train_c,
        'params': [
            ('name', GET_OBJECT),
            ('traits', TO_FLOATS),
            ('configs', GET_CONFIGS_C)
        ]
    },
    'multi_train_n': {
        'function': multi_train_n,
        'params': [
            ('name', GET_OBJECT),
            ('traits', TO_FLOATS),
            ('configs', GET_CONFIGS_N)
        ]
    }
}


def print_error(line):
    sys.stderr.write(line + '\n')


def parse(line):
    line = line.split()
    if len(line) > 0:
        try:
            command = commands[line[0]]
            try:
                function, params = command['function'], command['params']
                try:
                    args = map(lambda (param, arg): param[1](arg), zip(params, line[1:]))
                    try:
                        function(*args)
                    except TypeError as e:
                        traceback.print_exc()
                        print_error('Internal error: %s' % e)
                        print 'Usage: %s' % reduce(lambda acc, val: acc + ' ' + val[0], params, line[0])
                    except BaseException as e:
                        traceback.print_exc()
                        print_error('Internal error: %s' % e)
                except TypeError as e:
                    traceback.print_exc()
                    print_error('Internal error: %s' % e)
            except KeyError as e:
                traceback.print_exc()
                print_error('Internal error: %s' % e)
        except KeyError:
            print 'Available commands: %s' % reduce(lambda acc, val: acc + ' ' + val, commands)