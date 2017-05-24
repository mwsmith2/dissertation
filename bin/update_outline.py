#!/bin/python

import sys
from glob import glob

def main():

    outline = open('doc/OUTLINE.md', 'w')

    texfiles = glob('*.tex')

    for texfile in texfiles:
        with open(texfile) as f:
            lines = f.read().split('\n')

        for line in lines:

            if '\Title' in line:
                title = line.split('{')[1].split('}')[0]
                outline.write('# Title: %s\n\n' % title)

            if '\chapter' in line:
                title = line.split('{')[1].split('}')[0]
                outline.write('## %s\n\n' % title)

            if '\section' in line:
                title = line.split('{')[1].split('}')[0]
                outline.write('### %s\n\n' % title)

            if '\subsection' in line:
                title = line.split('{')[1].split('}')[0]
                outline.write('- %s\n' % title)

            if '\subsubsection' in line:
                title = line.split('{')[1].split('}')[0]
                outline.write('  - %s\n' % title)

    outline.close()

    return 0


if __name__ == '__main__':
    sys.exit(main())