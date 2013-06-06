__author__ = 'paoolo'

import re


def pretty_print(inner_func):
    def func(*args, **kwargs):
        content = re.split(r'\n', inner_func(*args, **kwargs))
        return reduce(lambda acc, line: acc + '\n\t' + line, content[1:], '\t' + content[0])

    return func
