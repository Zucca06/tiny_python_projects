#!/usr/bin/env python3
"""
Purpose: Say hello using a parameter
Author: Michele Minervini <miki.minervini@gmail.com>
"""
import argparse


def main():
    """ Main function, prints the string """

    args = get_args()

    print("Hello, " + args.name + "!")


def get_args():
    """ get the argument for the main function"""

    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument('-n',
                        '--name',
                        metavar='name',
                        default='World',
                        help='Name to greet')

    return parser.parse_args()


if __name__ == '__main__':
    main()
