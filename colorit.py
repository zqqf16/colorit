#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import print_function

import sys

colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

__all__ = ['paint', 'colors', 'attributes']+colors
__version__ = '1.0'

_FORMAT = '\033[{}m\033[{};{}m{}\033[0m'

attributes = ['blod', 'underscore', 'blink', 'reverse', 'concealed']

_FOREGROUND = dict(zip(colors, list(range(30, 38))))
_BACKGROUND = dict(zip(colors, list(range(40, 48))))
_attributes = dict(zip(attributes, [1, 4, 5, 7, 8]))

def paint(foreground, background=None, attribute=None):
    fg = _FOREGROUND.get(foreground, 39)
    bg = _BACKGROUND.get(background, 49)
    att = _attributes.get(attribute, 0)

    return lambda s: _FORMAT.format(att, bg, fg, s)

_self = sys.modules[__name__]
for c in colors:
    setattr(_self, c, paint(c))

if __name__ == '__main__':
    def print_row(b):
        for f in colors:
            p = paint(f, b)
            print(p('{:^8}'.format(f)), end=' ')
        print('')

    print_row(None)
    for b in colors:
        print_row(b)

