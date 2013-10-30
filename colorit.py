#!/usr/bin/env python
#-*- coding: utf-8 -*-

__all__ = ['paint']
__version__ = '1.0'

COLOR_FORMAT = '\033[%dm\033[%d;%dm%s\033[0m'

COLOR_NAME = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
ATTRIBUTE_NAME = ['blod', 'underscore', 'blink', 'reverse', 'concealed']

FOREGROUND = dict(zip(COLOR_NAME, list(range(30, 38))))
BACKGROUND = dict(zip(COLOR_NAME, list(range(40, 48))))
ATTRIBUTE = dict(zip(ATTRIBUTE_NAME, [1, 4, 5, 7, 8]))

def paint(foreground, background=None, attribute=None):
    fg = FOREGROUND.get(foreground, 39)
    bg = BACKGROUND.get(background, 49)
    att = ATTRIBUTE.get(attribute, 0)

    return lambda s: COLOR_FORMAT % (att, bg, fg, s)

if __name__ == '__main__':
    for att in ATTRIBUTE_NAME:
        for key in COLOR_NAME:
            p = paint(key, attribute=att)
            print p(key+' '+att)
