__author__ = 'ffacce'
import sys

from settings import MAYA_VERSION_LIST

if __name__ == '__main__':
    global INPUT_JSON

    print '>> install start argc', len(sys.argv)
    if ( len(sys.argv) != 2):
        print "Usage: .\\whPy.py sample.json"
        exit()

    print MAYA_VERSION_LIST[0].VERSION



