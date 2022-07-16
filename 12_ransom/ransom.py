#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 16/07/2022
Purpose: Randomly capitalazing letters
"""

import argparse
import random
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransome note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Randome seed',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    if os.path.isfile(args.text):
      with open(args.text, encoding='utf-8') as file:
        text = file.read().rstrip()
    else:
      text = args.text

    print(''.join(map(chose, text)))  
      
# --------------------------------------------------      
def chose(c):
    """Capitalize randomly a letter"""

    return c.upper() if random.choice([True, False]) else c.lower()

  
# --------------------------------------------------
if __name__ == '__main__':
    main()