
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:54:09 2017

@author: muss
"""

import os
import shutil
from argparse import ArgumentParser
from collections import OrderedDict

import pomutils as pu

def vrepl(flines, oldstr, newstr):
    '''
    Replace from_vrsn with to_vrsn in a list of strings.  In place replacement.  Returns an OrderedDict
    (key = lno, value = (original line, replacement line)).
    '''
    replacements = OrderedDict()
    for lno, line in enumerate(flines, start=1):
        if oldstr in line:
            flines[lno-1] = line.replace(oldstr, newstr)
            replacements[lno] = (line.strip(), flines[lno-1].strip())
    return flines, replacements

def find_snapshots(flines):
    '''
    Find occurrences of '-SNAPSHOT' in a list of lines (presumably a pom).  Returns an OrderedDict (key = lno, value = line)
    of all lines that contain the string.
    '''
    snapshots = OrderedDict()
    for lno, line in enumerate(flines, start=1):
        if '-SNAPSHOT' in line:
            snapshots[lno] = line.strip()
    return snapshots

def vrsnrepl(f, from_vrsn, to_vrsn):
    fstr = f.read()
    flines = fstr.splitlines()
    flines = vrepl(flines, from_vrsn, to_vrsn)
    rfstr = '\n'.join(flines)
    f.seek(0)
    f.write(rfstr)
    f.truncate()

def process_poms(basedir, from_vrsn, to_vrsn):
    processed_poms = OrderedDict()
    for pom in pu.get_poms(basedir):
        replacements, snapshots = process_pom(pom, from_vrsn, to_vrsn)
        processed_poms[pom] = (replacements, snapshots)
    return processed_poms

def process_pom(pom, from_vrsn, to_vrsn):
    '''
    Replace from_vrsn with to_vrsn in pom.  Return an OrderedDict of replacements and an OrderedDict of remaining
    -SNAPSHOT strings still in the pom after the replacement.
    '''
    flines = []
    flines, replacements = vrepl(get_lines(pom), from_vrsn, to_vrsn)
    put_lines(pom, flines)
    snapshots = find_snapshots(flines)
    return replacements, snapshots

def get_lines(fname):
    with open(fname) as f:
        flines = f.readlines()
    return flines

def put_lines(fname, flines):
    with open(fname, mode='w') as f:
        f.writelines(flines)

def replace_file(oldfile, newfile):
    '''
    Replace oldfile with newfile (delete oldfile and 'rename' newfile to oldfile)
    '''
    os.remove(oldfile)
    shutil.move(newfile, oldfile)

def print_results(processed_poms):
    dashline = '-'*92
    tot_repls, tot_snaps = 0, 0
    print(dashline)
   for pom in processed_poms:
        print('{}'. format(pom))
        replacements, snapshots = processed_poms[pom]
        tot_repls += len(replacements)
        tot_snaps += len(snapshots)
        print_replacements(replacements)
        print_snapshots(snapshots)
        print()
    print('{} poms processed.'.format(len(processed_poms)))
    print('{} total replacements.'.format(tot_repls))
    print('{} snapshot left.'.format(tot_snaps))
    print(dashline)

def print_replacements(replacements):
    print('  Replacements:')
    for lno in replacements:
        oline, nline = replacements[lno]
        print('    {} {} ---> {}'.format(lno, oline, nline))
    print('  {} replacements done.'.format(len(replacements)))

def print_snapshots(snapshots):
    print('  Remaining snapshots:')
    for lno in snapshots:
        line = snapshots[lno]
        print('    {} {}'.format(lno, line))
    print('  {} snapshots left.'.format(len(snapshots)))
        

def get_args():
    """
    Read the command line arguments:
        basedir is the root directory to search for poms
        from_vrsn is the expected current version in the poms
        to_vrsn is the replacement version.  presumably the release.
    """
    parser = ArgumentParser(description='Project Root directory.')
    parser.add_argument('basedir', help='root directory')
    parser.add_argument('from_vrsn', help='current version')
    parser.add_argument('to_vrsn', help='new version')
    args = parser.parse_args()
    return args.basedir, args.from_vrsn, args.to_vrsn

def main():
    vstr = '0.5'
    fstr = os.path.basename(__file__)
    print('{} version {} starting.'.format(fstr, vstr))

    basedir, from_vrsn, to_vrsn = get_args()
    processed_poms = process_poms(basedir, from_vrsn, to_vrsn)
    print_results(processed_poms) 
    print('{} version {} done.'.format(fstr, vstr))
        
    

if __name__ == '__main__':
    main()

…muss

