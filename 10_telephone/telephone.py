#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 14/07/2022
Purpose: Telephone game
"""

import argparse
import random as rnd
import os
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    rnd.seed(args.seed)

    if os.path.isfile(args.text):
        text = open(args.text, encoding='utf-8').read().rstrip()
    else:
        text = args.text

    print(f'You said: "{text}"')

    num_mutations = round(args.mutations * len(text))

    character = ''.join(sorted(string.ascii_letters + string.punctuation))

    char_to_mutate = rnd.sample(range(len(text)), num_mutations)

    for index in char_to_mutate:
        text = text[:index] + rnd.choice(character.replace(
            text[index], '')) + text[index + 1:]

    print(f'I heard : "{text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
