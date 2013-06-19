__author__ = 'paoolo'


def get_func(func_dict):
    def inner_func(val):
        val = val.split(',')
        if val > 0:
            args = map(lambda arg: float(arg), val[1:])
            return func_dict[val[0]](*args)

    return inner_func


from const import HELP_TEXT
from func import ACTIVATION_FUNC, LEARNING_RATE_FUNC, NEIGHBORHOOD_FUNC, MEASUREMENT_FUNC
from error_handlers import key_error_handler, value_error_handler, io_error_handler
from interpreter import ENVIRONMENT


parse_activation_func = key_error_handler(get_func(ACTIVATION_FUNC), HELP_TEXT['activation_func'])
parse_learning_rate_func = key_error_handler(get_func(LEARNING_RATE_FUNC), HELP_TEXT['learning_rate_func'])
parse_neighborhood_func = key_error_handler(get_func(NEIGHBORHOOD_FUNC), HELP_TEXT['neighborhood_func'])
parse_measurement_func = key_error_handler(lambda val: MEASUREMENT_FUNC[val], HELP_TEXT['measures_func'])

parse_object = key_error_handler(lambda val: ENVIRONMENT[val], 'Object not found')
parse_objects = lambda val: map(parse_object, val.split(','))

parse_string = lambda val: val

parse_int = value_error_handler(lambda val: int(val), 'Cannot convert value to integer')
parse_ints = lambda val: map(parse_int, val.split(','))

parse_float = value_error_handler(lambda val: float(val), 'Cannot convert value to float')
parse_floats = lambda val: map(parse_float, val.split(','))

parse_file = io_error_handler(lambda val: open(val), 'Cannot open file')


def parse_signals(line):
    return map(lambda val: parse_floats(val), line.split(';'))


def parse_config_c(line):
    return map(lambda val: val[0](val[1]),
               zip([parse_learning_rate_func, parse_int],
                   line.split(';')))


def parse_config_n(line):
    return map(lambda val: val[0](val[1]),
               zip([parse_learning_rate_func, parse_measurement_func, parse_neighborhood_func, parse_int],
                   line.split(';')))


parse_configs_c = lambda val: map(parse_config_c, val.split('|'))
parse_configs_n = lambda val: map(parse_config_n, val.split('|'))


def parse_config_c_cp(line):
    return map(lambda val: val[0](val[1]),
               zip([parse_learning_rate_func, parse_learning_rate_func, parse_int],
                   line.split(';')))


def parse_config_n_cp(line):
    return map(lambda val: val[0](val[1]),
               zip([parse_learning_rate_func, parse_measurement_func, parse_neighborhood_func, parse_learning_rate_func,
                    parse_int],
                   line.split(';')))


parse_configs_c_cp = lambda val: map(parse_config_c, val.split('|'))
parse_configs_n_cp = lambda val: map(parse_config_n, val.split('|'))


def parse_config_bp(line):
    return map(lambda val: val[0](val[1]),
               zip([parse_learning_rate_func, parse_int], line.split(';')))


def parse_config_bp_m(line):
    return map(lambda val: val[0](val[1]),
               zip([parse_learning_rate_func, parse_learning_rate_func, parse_int], line.split(';')))


parse_configs_bp = lambda val: map(parse_config_bp, val.split('|'))
parse_configs_bp_m = lambda val: map(parse_config_bp_m, val.split('|'))