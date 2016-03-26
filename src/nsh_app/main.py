import getopt
import sys

import re

from nsh_app.sh import interpreter

__author__ = 'paoolo'


def shell():
    print 'Neuronal (shell)'
    try:
        sys.stdout.write('nsh> ')
        line = sys.stdin.readline()
        while line is not None:
            if not re.match("^\s*#+", line):
                interpreter.interpret(line)
            sys.stdout.write('nsh> ')
            line = sys.stdin.readline()
    except KeyboardInterrupt:
        print ' Ouch...'
    print 'Bye!'


def batch(source):
    print 'Neuronal (batch)'
    for line in source:
        if not re.match("^\s*#+", line):
            interpreter.interpret(line)


def usage():
    print 'Usage:\n' \
          '-h --help\tprint this help\n' \
          '-f --file\tselect input file'


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hf:', ['help', 'file='])

        source = None
        for o, a in opts:
            if o in ('-h', '--help'):
                usage()
                sys.exit()
            elif o in ('-f', '--file'):
                source = open(a.strip())
            else:
                assert False, 'unhandled option'

        if source is None:
            shell()
        else:
            batch(source)

    except getopt.GetoptError as err:
        print str(err)
        sys.exit(1)
