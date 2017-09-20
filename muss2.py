# -*- coding: utf-8 -*-
"""
pomutils.py: pom.xml related utilites

TODO: Add a function to get the modules. Could be used to determine
      which subdirectories to look in for poms.

Created on Tue May 10 13:22:34 2016

@author: muss
"""

import os
import xml.etree.ElementTree as et
#import lxml.etree as et
from argparse import ArgumentParser
from pathlib import Path
import types

MAVEN_NAMESPACE = '{http://maven.apache.org/POM/4.0.0}'

class MyTreeBuilder(et.TreeBuilder):

    def comment(self, data):
        self.start(et.Comment, {})
        self.data(data)
        self.end(et.Comment)

def get_poms(basedir):
    '''
    pom generator
    Yields all the pom.xml files in the tree rooted at basedir.
    '''
    for root, dirs, files in os.walk(basedir):
        for fname in files:
            # if fname == 'pom.xml':
            if fname.endswith('pom.xml'):
                yield os.path.join(root, fname)
        if '.svn' in dirs:
            dirs.remove('.svn')
        if 'target' in dirs:
            dirs.remove('target')

def change_versions(pom, tmp_pom, from_vrsn, to_vrsn):
    '''
    Change the artifact version and the artifact's parent version from from_vrsn to to_vrsn

    The artifact version is changed only if the current version of the artifact == from_vrsn.
    Idem for the parent's version.
    '''
    tree = et.parse(pom, parser=et.XMLParser(target=MyTreeBuilder()))
    root = tree.getroot()
    vrsn_path = MAVEN_NAMESPACE + 'version'
    version_el = root.find(vrsn_path)
    version = version_el.text if version_el is not None else 'None'
    if version == from_vrsn:
        version_el.text = to_vrsn
    pvrsn_path = MAVEN_NAMESPACE + 'parent/' + MAVEN_NAMESPACE + 'version'
    parent_version_el = root.find(pvrsn_path)
    parent_version = parent_version_el.text if parent_version_el is not None else 'None'
    if parent_version == from_vrsn:
        parent_version_el.text = to_vrsn
    tree.write(tmp_pom)
    return version, parent_version

def get_artifacts(basedir):
    '''
    Yields all artifacts in all poms in basedir and its descendents.

    The return value is a tuple (artifact, pom)
    The artifact format is 'groupId:artifactId:version:packaging'.
    The pom is the full path to the pom
    '''
    for pom in get_poms(basedir):
        yield get_artifact_and_parent(pom), pom

def get_artifact_and_parent(pom):
    '''
    Return the artifact and its parent from the pom.
    '''
    tree = et.parse(pom, parser=et.XMLParser(target=MyTreeBuilder()))
    root = tree.getroot()
    artifact = get_artifact(root)
    parent = get_parent_artifact(root)
    return artifact, parent

def get_artifact(root):
    '''
    Get the main artifact from the pom as a string.

    Output is in 'groupId:artifactId:version:packaging' format.
    Missing pieces are empty.  If all pieces are missing, the
    output is ':::'
    '''
    artifactId = get_artifactId(root)
    version = get_version(root)
    groupId = get_groupId(root)
    packaging = get_packaging(root)
    return ':'.join([groupId, artifactId, version, packaging])

def get_artifactId(root):
    aid_path = MAVEN_NAMESPACE + 'artifactId'
    artifactId_el = root.find(aid_path)
    artifactId = artifactId_el.text if artifactId_el is not None else ''
    return artifactId

def get_groupId(root):
    '''
    Get the artifact groupId from the pom.
    
    If the groupId is missing, use the parent groupId, if it exists.
    '''
    gid_path = MAVEN_NAMESPACE + 'groupId'
    gid_el = root.find(gid_path)
    if gid_el is None:
        gid = get_parent_groupId(root)
    else:
        gid = gid_el.text

    return gid

def get_version(root):
    '''
    Get the artifact version from the pom in parent.
    
    If the version is missing, use the parent version, if it exists.
    '''
    vrsn_path = MAVEN_NAMESPACE + 'version'
    version_el = root.find(vrsn_path)
    if version_el is None:
        version = get_parent_version(root)
    else:
        version = version_el.text
    return version

def get_packaging(parent):
    pkg_path = MAVEN_NAMESPACE + 'packaging'
    packaging_el = parent.find(pkg_path)
    packaging = packaging_el.text if packaging_el is not None else ''
    return packaging

def get_parent_artifact(root):
    '''
    Get the parent artifact from the <parent> element as a string.

    Output is in 'groupId:artifactId:version' format.
    Missing pieces are empty.  If all pieces are missing, the
    output is '::'
    '''
    artifactId = get_parent_artifactId(root)
    groupId = get_parent_groupId(root)
    version = get_parent_version(root)
    return ':'.join([groupId, artifactId, version])

def get_parent_artifactId(root):
    '''
    Get the parent artifactId from the <parent> element in the pom

    Returns the parent artifactId if found, otherwise the empty string.
    '''
    aid_path = MAVEN_NAMESPACE + 'parent/' + MAVEN_NAMESPACE + 'artifactId'
    aid_el = root.find(aid_path)
    aid = aid_el.text if aid_el is not None else ''
    return aid

def get_parent_groupId(root):
    '''
    Get the parent groupId from the <parent> element in the pom

    Returns the parent groupId if found, otherwise the empty string.
    '''
    gid_path = MAVEN_NAMESPACE + 'parent/' + MAVEN_NAMESPACE + 'groupId'
    gid_el = root.find(gid_path)
    gid = gid_el.text if gid_el is not None else ''
    return gid

def get_parent_version(root):
    '''
    Get the parent version from the <parent> element in the pom

    Returns the parent version if found, otherwise the empty string.
    '''
    vrsn_path = MAVEN_NAMESPACE + 'parent/' + MAVEN_NAMESPACE + 'version'
    version_el = root.find(vrsn_path)
    version = version_el.text if version_el is not None else ''
    return version

def get_type(root):
    atype_path = MAVEN_NAMESPACE + 'type'
    atype_el = root.find(atype_path)
    atype = atype_el.text if atype_el is not None else ''
    return atype

def find_artifact_refs(pom):
    '''
    Find all artifact references in the pom.  Generator.
    '''
    tree = et.parse(pom, parser=et.XMLParser(target=MyTreeBuilder()))
    root = tree.getroot()
    yield from find_x(root)

def find_x(root):
    '''
    Find all artifact references in the tree rooted at "root".  Generator

    It will not return the artifactId of the pom., but it will return the
    parent artifactId.

    Comments show up as function types.  And they are bypassed.

    It is not exactely efficient either, but there seems to be no way to get
    the parent element for a given element in the Element Etree module included
    in the standard library.
    '''
    for rchild in list(root):
        # print('\nLooking at {}'.format(rchild.tag))
        for el in rchild.iter():
            eltag = strip_namespace(el.tag)
            if not isinstance(eltag, types.FunctionType):
                if not eltag.startswith('plugin'):
                    artifact = find_artifact_ref(el)
                    if artifact is not None:
                        yield artifact, strip_namespace(el.tag)

def strip_namespace(tag):
    '''
    Strip the namespace from tha tag name.

    {namespace}tag --> tag
    '''
    if not isinstance(tag, types.FunctionType):
        ix = tag.rfind('}')
        if ix > 0:
            tag = tag[ix+1:]
    return tag

    
def find_artifact_ref(root):
    '''
    Check if root has a child 'artifactId'.  If it does, return:
    groupId:artifactId:version:type
    '''
    artifact = None
    aid_path = MAVEN_NAMESPACE + 'artifactId'
    aid_el = root.find(aid_path)
    if aid_el is not None:
        artifactId = get_artifactId(root)
        version = get_version(root)
        groupId = get_groupId(root)
        atype = get_type(root)
        artifact = ':'.join([groupId, artifactId, version, atype])
    return artifact

def get_args():
    """
    Read the command line arguments:
        basedir is the root directory to search for poms
    """
    parser = ArgumentParser(description='Project Root directory.')
    parser.add_argument('basedir', help='root directory')
    parser.add_argument('from_vrsn', help='current version')
    parser.add_argument('to_vrsn', help='new version')
    args = parser.parse_args()
    return args.basedir, args.from_vrsn, args.to_vrsn

def main():
    vstr = '0.4'
    fstr = os.path.basename(__file__)
    print('{} version {} starting.'.format(fstr, vstr))
    basedir, from_vrsn, to_vrsn  = get_args()
    tmpdir = basedir + '-tmp'
    print('basedir = {}'.format(basedir))
    print('tmpdir = {}'.format(tmpdir))
    print('Change the version from {} to {}'.format(from_vrsn, to_vrsn))
    no_poms = 0

   et.register_namespace('', "http://maven.apache.org/POM/4.0.0")
    for pom in get_poms(basedir):
        curpomdir = os.path.dirname(pom)
        relpomdir = os.path.relpath(curpomdir, basedir)
        tmppomdir = os.path.join(tmpdir, relpomdir)
        makedir = Path(tmppomdir)
        if not makedir.exists():
            makedir.mkdir(parents=True)
        tmp_pom = os.path.join(tmppomdir, os.path.basename(pom))
        version, parent_version = change_versions(pom, tmp_pom, from_vrsn, to_vrsn)
        print('{} -- version = {}, parent version = {}'.format(pom, version, parent_version))
        no_poms += 1

    print('{} poms read.'.format(no_poms))
    print('{} version {} done.'.format(fstr, vstr))

def test():
    vstr = '0.4'
    fstr = os.path.basename(__file__)
    print('{} version {} starting.'.format(fstr, vstr))
    basedir = 'c:/devl/projects/mixed/buildsys5/testdata'
    print('basedir = {}'.format(basedir))
    no_poms = 0

    for pom in get_poms(basedir):
        artifact, artifact_parent = get_artifact_and_parent(pom)
        print('pom {}: artifact={}, parent={}'.format(os.path.basename(pom), artifact, artifact_parent))
        no_poms += 1

    print('{} poms read.'.format(no_poms))
    print('{} version {} done.'.format(fstr, vstr))

if __name__ == '__main__':
    test()



…muss

