__author__ = 'paoolo'


class FunctionWrapper():
    def __init__(self, func, name, desc=None):
        self.func = func
        self.name = name
        self.desc = desc

    def __call__(self, *args, **kwargs):
        if self.func.__code__.co_argcount == 1:
            return self.func(args[0])
        return self.func(args, kwargs)

    def __str__(self):
        return self.name if self.desc is None else self.desc