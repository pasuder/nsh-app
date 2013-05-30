#!/usr/bin/python
__author__ = 'paoolo'

import getopt
import sys
import cmd

from main import interpreter


class Main(cmd.Cmd):
    def do_load(self, path):
        print path

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def postloop(self):
        print


def shell():
    print 'Neuronal (shell)'
    env = {}
    try:
        sys.stdout.write('nsh> ')
        line = sys.stdin.readline()
        while line is not None:
            env = interpreter.parse(line)
            sys.stdout.write('nsh> ')
            line = sys.stdin.readline()
    except KeyboardInterrupt:
        print ' Ouch...'
    print 'Bye!'


def batch(source):
    print 'Neuronal (batch)'
    env = {}
    for line in source:
        env = interpreter.parse(line)
    return env


def usage():
    print "Usage:\n" \
          "-h --help\tprint this help\n" \
          "-f --file\tselect input file"


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])

        source = None
        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o in ("-f", "--file"):
                source = open(a)
            else:
                assert False, "unhandled option"

        if source is None:
            shell()
        else:
            batch(source)

    except getopt.GetoptError as err:
        print str(err)
        sys.exit(1)