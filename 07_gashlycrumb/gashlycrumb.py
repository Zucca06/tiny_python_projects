#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 11/07/2022
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
  
    args = get_args()

    dic = {}
  
    for letter in args.letter:
      if letter.isalpha() and len(letter) == 1:
        with open(args.file.name) as file:
          for line in file:
            if letter.upper() == line[0].upper():
              dic[letter.upper()] = line
      else:
        error_string = f'I do not know "{letter}".\n'
        dic[letter.upper()] = error_string
      print(dic[letter.upper()], end = '')


# --------------------------------------------------
if __name__ == '__main__':
    main()