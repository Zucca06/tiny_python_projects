#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 15/07/2022
Purpose: Bottles of beer song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default='10')

    parser.add_argument('-s',
                        '--step',
                        help='Skip verses of step',
                        metavar='step',
                        type=int,
                        default='1')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    if args.step == 0:
        parser.error(f'--step "{args.step}" must not be 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print('\n\n'.join(map(verse, range(args.num, 0, -abs(args.step)))))


# --------------------------------------------------
def verse(bottle):
    """Sing a verse"""

    s_1 = '' if bottle == 1 else 's'
    num_last_verse = 'No more' if bottle - 1 == 0 else bottle - 1
    s_2 = '' if bottle - 1 == 1 else 's'

    return '\n'.join([
        f'{bottle} bottle{s_1} of beer on the wall,',
        f'{bottle} bottle{s_1} of beer,', 'Take one down, pass it around,',
        f'{num_last_verse} bottle{s_2} of beer on the wall!'
    ])


# --------------------------------------------------
def test_verse():
    """Test verse"""
    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])
    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
