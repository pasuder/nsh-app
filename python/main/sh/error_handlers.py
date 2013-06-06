__author__ = 'paoolo'


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