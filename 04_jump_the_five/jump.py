#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 08/07/2022
Purpose: A simple message encrypter/decrypter"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    dictionary = {
        '0': '5',
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1'
    }

    args = get_args()
    text = args.text

    for single_c in text:
        print(crypt(single_c, dictionary), end='')


# --------------------------------------------------
def crypt(char, dic):
    """Crypt a single character"""
    return dic.get(char, char)


# --------------------------------------------------
if __name__ == '__main__':
    main()
