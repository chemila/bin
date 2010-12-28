#!/usr/bin/env python
import tarfile
import sys
import os
import fnmatch
import optparse
import shutil

def tar(name, path=os.path.curdir, savedto=False, pat=False, force='n'):
    t = tarfile.open(name, 'w|bz2')
    print "tar directory %s" % path

    for root, dirnames, fnames in os.walk(path):
        for fname in fnames:
            if fname == name or exclude(fname, pat): continue
            realpath = os.path.join(root, fname)
            print "add file: %s" % realpath
            t.add(realpath)

    print 'tar file saved to %s' % name
    t.close()

    if(savedto):
        target = os.path.abspath(os.path.join(savedto, name))

        if(os.path.exists(target)):
            resposne = 'y' if 'y' == force else raw_input('target file exist, are u sure to override it? (y or n)')

            if('y' == resposne):
                os.remove(target)

        print 'move %s to %s' % (name, target)
        shutil.move(name, savedto)         
       
def exclude(fname, pat):
    return fnmatch.fnmatch(fname, pat)

if __name__ == '__main__':
    parser = optparse.OptionParser()

    parser.add_option('-p', '--path', dest='path', help='file path to be added', metavar='FILE', default=os.path.curdir)
    parser.add_option('-e', '--ext', dest='ext', help='like .gz, .gz, .bz2 etc', type='choice', choices=['.bz', '.bz2'], default='.bz2')
    parser.add_option('-o', '--exclude', dest='exclude', help='file name to be excluded', default='*.pyc')
    parser.add_option('-f', '--force', dest='force', help='file name to be excluded', action='store_true', default=False)

    (options, args) = parser.parse_args()

    assert len(args) > 0, 'tar file name is required(with out extension)'
    savedto = args[1] if len(args) > 1 else False
    tar(args[0] + '.tar' + options.ext, options.path, savedto, options.exclude, options.force)
