#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 11/07/2022
Purpose: Apples and Banans
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apple and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=['a', 'e', 'i', 'o', 'u'])

    parser.add_argument('-a',
                        '--adjacent',
                        help='Consider adjacent vowels as one',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    adj = args.adjacent

    if os.path.isfile(args.text):
        with open(args.text) as file:
            text = file.read()
    else:
        text = args.text

    for letter in 'aeiou':
        text = text.replace(letter, args.vowel)
        text = text.replace(letter.upper(), args.vowel.upper())

    while adj:
        if args.vowel * 2 in text:
            text = text.replace(args.vowel * 2, args.vowel)
        else:
            adj = False

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
