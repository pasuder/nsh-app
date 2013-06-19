__author__ = 'paoolo'

import math


class Function(object):
    def __init__(self, func, name, desc=None):
        self.func = func
        self.name = name
        self.desc = desc

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __str__(self):
        return self.name if self.desc is None else self.desc


def normalize(values):
    divisor = math.sqrt(reduce(lambda acc, val: acc + math.pow(val, 2), values))
    return map(lambda value: value / divisor, values)


get_indent = lambda indent: ('\t' * indent) + '[\n'