import traceback

__author__ = 'paoolo'


class Function(object):
    def __init__(self, func, name, desc=None):
        self.func = func
        self.name = name
        self.desc = desc

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __str__(self):
        return self.name if self.desc is None else self.desc