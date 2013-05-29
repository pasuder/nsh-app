__author__ = 'paoolo'

import re


def pretty_print(inner_func):
    def func(*args, **kwargs):
        content = re.split(r'\n', inner_func(*args, **kwargs))
        return reduce(lambda acc, line: acc + '\n\t' + line, content[1:], '\t' + content[0])

    return func


def normalize(inner_func):
    def func(values):
        minimum, maximum = min(values), max(values)
        diff = maximum - minimum
        results = inner_func(map(lambda val: (val - minimum) / diff, values))
        return map(lambda val: (val * diff) + minimum, results)

    return func
