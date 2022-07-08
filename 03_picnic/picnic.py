#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')
    parser.add_argument('string',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')
    parser.add_argument('-c',
                        '--comma',
                        action='store_true',
                        help='Insert the Oxford comma')
    parser.add_argument('-sep',
                        '--separator',
                        nargs='?',
                        default=',',
                        type=str,
                        help='Select a different separator rather than: \,') 
    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    string = args.string
    sep = args.separator + ' '

    if args.sorted:
        string.sort()

    lenght = len(string)

    if lenght == 1:
        list = string[0]
    elif lenght == 2:
        list = " and ".join(string)
    elif args.comma:
        last_element = " and " + string[-1]
        list = sep.join(string[:-1]) + last_element
    else :
        string[-1] = "and " + string[-1]
        list = sep.join(string)

    print(f'You are bringing {list}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
