# -*- coding: utf-8 -*-
"""
swiftbooks.py

Read swift books with concentration on the ones that contain the fields, 
i.e., those that match r'.*[0-9]{3}\.htm'.  Look for qualifier tables where
the m/o column contains a mixture of m's and o's.

This is a temporary script file.
"""
import os
from argparse import ArgumentParser
import glob
from bs4 import BeautifulSoup
import re
import pandas as pd
from collections import defaultdict
import pickle
import json


def get_vols(booksdir):
    vname = booksdir + os.sep + 'us[c0-9]m*'
    voldirs = glob.glob(vname)
    return voldirs
    
    
def get_htmfiles(vol):
    htmname = vol + os.sep + '*.htm'
    fpaths = glob.glob(htmname)
    return fpaths


def get_files_matching(booksdir, ffname_pat):
    """
    Return all file paths matching the pattern ffname_pat from the directory tree
    rooted at booksdir.
    """
    p = re.compile(ffname_pat)
    voldirs = get_vols(booksdir)
    voldirs.sort()
    print('{} volumes found.'.format(len(voldirs)))
    for vol in voldirs: 
        print('Processing {}'.format(vol))
        fpaths = get_htmfiles(vol)
        fpaths.sort()
        for fpath in fpaths:
            fname = os.path.basename(fpath)
            if p.match(fname):
                yield fpath


def get_soup_from_file(fpath):
    with open(fpath, mode='r') as htmf:
        soup = BeautifulSoup(htmf, "html5lib")
    return soup

    
def get_ctx(soup):
    book_context_tag = soup.find('meta', attrs={'name' : 'Book.Context'})
    if book_context_tag is not None:
        bkctx = book_context_tag['content']
    else:
        bkctx = '?'
    return bkctx


def get_subject(soup):
    subject_tag = soup.find('meta', attrs={'name' : 'Subject'})
    if subject_tag is not None:
        subject = subject_tag['content']
    else:
        subject = '?'
    return subject
    

def get_table_for_h4(soup, h4hdr, scls=None):
    """
    Return table element for h4hdr, if any, None otherwise.
    """
    if scls is None:
        h4 = soup.find('h4', string=h4hdr)
    else:
        h4 = soup.find('h4', attrs = {'class' : scls}, string=h4hdr)
    if h4 is not None:
        p = h4.next_sibling
        while p is not None:
            if p.name == 'table':
                return p
            elif p.name == 'h4':
                return None
            else: 
                p = p.next_sibling
    return None


def process_59(fpath, mtdict):
    fname = os.path.basename(fpath)
    vname = os.path.dirname(fpath).split(os.sep)[-1]
    soup = get_soup_from_file(fpath)
    bkctx = get_ctx(soup)
    if bkctx.startswith('MT'):
        subject = get_subject(soup)
        if not subject.startswith('?'):
            mtdict[bkctx] = [vname, fname]
            ix59 = subject.find('59a')
            if ix59 == -1:
                return
            fix = subject.find('MT')
            field = '??'
            if fix >= 0:
                field = subject[fix+9:]
            print('\t{}/{} -- {} -- {}'.format(vname, fname, bkctx, field))
            fmthtmtab = get_table_for_h4(soup, 'FORMAT', 'fldfmt')
            if fmthtmtab is None: 
                print('\t\t NO table found.')
                return
            tbl = pd.read_html(str(fmthtmtab))


  
def process_field(fpath, mtdict, hitdict, missdict):
    fname = os.path.basename(fpath)
    vname = os.path.dirname(fpath).split(os.sep)[-1]
    no_lives = 0
    soup = get_soup_from_file(fpath)
    bkctx = get_ctx(soup)
    if bkctx.startswith('MT'):
        subject = get_subject(soup)
        if not subject.startswith('?'):
            mtdict[bkctx] = [vname, fname]
            fix = subject.find('MT')
            field = '??'
            if fix >= 0:
                field = subject[fix+9:]
            print('\t{}/{} -- {} -- {}'.format(vname, fname, bkctx, field))
            cnt, mo = check_qualifier(soup)
            if cnt >=1:
                no_lives += cnt
                hitdict[bkctx].append([field, mo])
            else:
                if not mo.startswith('No'):
                    missdict[bkctx].append([field, mo])
    return no_lives

            
            
def check_qualifier(soup):
    """
    Find all instances where there is a combination of mandatory and optional qualifiers.
    Exclude cases where:
       there is only one qualifier
       all qualifiers are mandatory
       all qualifiers are optional
    """
    qual = soup.find('h4', attrs = {'class' : 'fldqlfr'}, string='QUALIFIER')
    if qual is not None:
        print('\t\t---> has Qualifier')
        p = qual.next_sibling
        while p is not None:
            if p.name == 'table':
                tlst = pd.read_html(str(p))
                t1 = tlst[0]
                is_mandatory = t1['M/O'] == 'M'
                is_optional = t1['M/O'] == 'O'
                t1m = t1[is_mandatory]
                t1o = t1[is_optional]
                print('\t\t---> and a table: m/o = {}, 1st Qualifier = {}'.format(t1['M/O'].values, t1.iloc[0].Qualifier))
                if len(t1m) >= 1 and len(t1o) >= 1:
                    print('\t\t---> !!!!!!!!!!!LIVE ONE!!!!!!!!!!!')
                    return (1, ', '.join(t1['M/O'].values))
                else:
                    return (0, ', '.join(t1['M/O'].values))
            elif p.name == 'h4':
                return (0, 'No table')
            else: 
                p = p.next_sibling
    return (0, 'No Qualifier?')

    
def process_mt(fpath):
    pass


def format_dict(ddict, mtdict):
    """
    print the info in a dict. applies to the hit and miss dictionaries only.
    For both dicts, the key is the MT and the value is a list containing
    the field and the m/o column from the html qualifier table.
    """
    no_fields = 0
    for mt in sorted(ddict.keys()):
        vname, fname = mtdict[mt]
        print()
        for fmo in ddict[mt]:
            field, mo = fmo
            no_fields += 1
            print('{} ({}/{}): {} ---> {}'.format(mt, vname, fname, field, mo))
    print('Number of items: {} in {} messages'.format(no_fields, len(ddict)))


def get_args():
    """
    Read the command line arguments:
        booksdir is the directory containing the swift books in html format
    """
    parser = ArgumentParser(description = 'Parse Swift books directory')
    parser.add_argument('booksdir', help = 'Swift books directory')
    args = parser.parse_args()
    return args.booksdir
        
    
def get_qinfo(booksdir):
    mtdict = {}
    hitdict = defaultdict(list)
    missdict = defaultdict(list)
    no_lives = 0
    ffname_pat = r'.*[0-9]{3}\.htm'
    for fpath in get_files_matching(booksdir, ffname_pat):
        no_lives += process_field(fpath, mtdict, hitdict, missdict)
        
    print('Number of live ones: {}'.format(no_lives))
    print('\n\nNearMisses:')
    format_dict(missdict, mtdict)
    print('\n\nHits:')
    format_dict(hitdict, mtdict)
    with open('qdata.pickle', 'wb') as fout:
        pickle.dump((hitdict, missdict, mtdict), fout, pickle.HIGHEST_PROTOCOL)
		
    with open('qdata.json', 'w') as jout:
        json.dump((hitdict, missdict, mtdict), jout)
    

def get_59_info(booksdir):    
    mtdict = {}
    ffname_pat = r'.*[0-9]{3}\.htm'
    for fpath in get_files_matching(booksdir, ffname_pat):
        process_59(fpath, mtdict)

    
def main():
    vstr = '0.1'
    print('swiftbooks.py version {} starting.'.format(vstr))
    booksdir = get_args()
    print('booksdir = {}'.format(booksdir))
    get_qinfo(booksdir)
    print('swiftbooks.py version {} done.'.format(vstr))


if __name__ == '__main__':
    main()