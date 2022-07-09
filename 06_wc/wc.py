#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 09/07/2022
Purpose: Word Counter
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        default=[sys.stdin],
                        type=argparse.FileType('rt'),
                        nargs='*')

    parser.add_argument('-c',
                        '--characters',
                        help='Show character coloumn',
                        action='store_true')

    parser.add_argument('-l',
                        '--lines',
                        help='Show lines column',
                        action='store_true')

    parser.add_argument('-w',
                        '--words',
                        help='Show words coloum',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    num_line_total = 0
    num_char_total = 0
    num_words_total = 0
    counter = 0

    args = get_args()
    file_list = args.file
    show_c = args.characters
    show_l = args.lines
    show_w = args.words

    for f_ptr in file_list:
        num_line = 0
        num_char = 0
        num_words = 0
        for line in f_ptr:
            num_line += 1
            num_words += len(line.split())
            num_char += len(line)

        if (not show_c and not show_l and not show_w):
            print(
                f'{num_line:8}{num_words:8}{num_char:8} {file_list[counter].name}'
            )
        else:
            if show_l:
                print(f'{num_line:8}', end='')

            if show_w:
                print(f'{num_words:8}', end='')

            if show_c:
                print(f'{num_char:8}', end='')

            print(f' {file_list[counter].name}')

        counter += 1
        num_line_total += num_line
        num_char_total += num_char
        num_words_total += num_words

    if not counter == 1:
        print(f'{num_line_total:8}{num_words_total:8}{num_char_total:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
