from optparse import OptionParser
import urllib
import sys

types = {
    'newhouse' : range(15),
    'esf' : [i+1 for i in range(15)],
    'newhousedup' : [1],
    'esfdup' : [1]
}

DOMAIN_CONFIG = {
    'local' : 'http://dev.adminleju.com',
    'remote' : 'http://admin.leju.com'
}

def update_and_sync(domain, ftype, fileno, prefix=''):
    if 'xml' != prefix:
        print 'Start to update %s%d.xml...' % (ftype, fileno)
        urllib.urlopen('%s/ge_sina/ge_sina.php?action=update&type=%s&fileno=%d' % (domain, ftype, fileno)).read()
        print 'Updated : %s/ge_sina/xml/%s%d.xml' % (domain, ftype, fileno)

    urllib.urlopen('%s/ge_sina/ge_sina.php?action=sync_one&type=%s&fileno=%d&prefix=%s' % (domain, ftype, fileno, prefix)).read()
    print "Sync one file: http://cache.mars.sina.com.cn/datahouse_d/house_partner/%s%s%d.xml" % (prefix, ftype, fileno)

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('-t', '--type', dest='type', type='choice', choices=['newhouse', 'esf', 'newhousedup', 'esfdup'], help='choose file type')
    parser.add_option('-p', '--prefix', dest='prefix', action='store_true', help='choose file prefix: xml or none')
    parser.add_option('-n', '--fileno', dest='fileno', type=int, help='choose file number')
    parser.add_option('-d', '--debug', dest='debug', action='store_true', help='debug or not')

    (options, args) = parser.parse_args()

    if options.prefix:
        prefix = 'xml'
    else:
        prefix = ''

    if options.fileno is not None:
        update_and_sync(args[0], options.type, options.fileno, prefix)
    else:
        for fileno in types[options.type]:
            update_and_sync(args[0], options.type, fileno, prefix)


    print 'finished'

