#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 07/07/2022
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word')
    parser.add_argument('side',
                        metavar='side',
                        help='Side: larboard or starboard')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = args.side

    char = word[0].lower()
    article = ''

    if char in 'aeiou':
        article = 'an'
    else:
        article = 'a'

    print(f'Ahoy, Captain, {article} {word} off the {side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
