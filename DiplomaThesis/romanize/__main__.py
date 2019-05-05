# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
from . import romanize

path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)


def main():
    import sys

    if len(sys.argv) > 1:
        print(romanize(' '.join(sys.argv[1:])))
    else:
        print(sys.stdin.encoding)
        for line in sys.stdin:
            line = line.decode(sys.stdin.encoding)
            # words = sys.stdin.read()
            # encoding=sys.stdin.encoding
            print(repr(line))
            print(romanize(line))


if __name__ == "__main__":
    main()
