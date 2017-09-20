# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:22:34 2016

@author: muss
"""

import os


def prpy(basedir):
    for root, dirs, files in os.walk(basedir):
        for fname in files:
            if fname.endswith('.py'):
                print(os.path.join(root, fname))
                if fname == 'testwalk.py':
                    with open(fname) as tw:
                        for line in tw:
                            print('--> {}'.format(line))


def main():
    prpy('c:/devl/projects/python')
    

if __name__ == '__main__':
    main()
