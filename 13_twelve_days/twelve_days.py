#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 23/07/2022
Purpose: Twelve days of christmas
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default='12')

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wr'),
                        default=sys.stdout)

    args = parser.parse_args()

    if args.num < 0 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print('\n\n'.join(map(verse, range(1, args.num + 1))), file=args.outfile)


# --------------------------------------------------
def verse(day):
    """Ceate a single verse"""
    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]

    gifts = [
        'And a partridge in a pear tree', 'Two turtle doves',
        'Three French hens', 'Four calling birds', 'Five gold rings',
        'Six geese a laying', 'Seven swans a swimming',
        'Eight maids a milking', 'Nine ladies dancing', 'Ten lords a leaping',
        'Eleven pipers piping', 'Twelve drummers drumming'
    ]

    single_verse = f'On the {ordinal[day - 1]} day of Christmas,\nMy true love gave to me,\n'
    for num in range(day - 1, 0, -1):
        single_verse = single_verse + gifts[num] + ',\n'

    if day - 1 == 0:
        single_verse = single_verse + 'A partridge in a pear tree.'
    else:
        single_verse = single_verse + gifts[0] + '.'

    return verse


# --------------------------------------------------
if __name__ == '__main__':
    main()
