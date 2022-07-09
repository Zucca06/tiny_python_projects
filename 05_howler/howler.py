#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 09/07/2022
Purpose: File Handling
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='sys.stdout')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    out_file_name = args.outfile

    if out_file_name == 'sys.stdout':
        ofile_ptr = sys.stdout
    else:
        ofile_ptr = open(out_file_name, 'wt', encoding='utf-8')

    if os.path.isfile(text):
        ofile_ptr.write(open(text, encoding='utf-8').read().upper() + '\n')
    else:
        ofile_ptr.write(text.upper() + '\n')

    ofile_ptr.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
