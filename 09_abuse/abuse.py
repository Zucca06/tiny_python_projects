#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 13/07/2022
Purpose: Make insults
"""

import argparse
import random as rnd


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        type=int,
                        help='Number of adjectives',
                        metavar='adjectives',
                        default='2')

    parser.add_argument('-n',
                        '--number',
                        type=int,
                        help='Number of insults',
                        metavar='insults',
                        default='3')

    parser.add_argument('-s',
                        '--seed',
                        type=int,
                        help='Random seed',
                        metavar='seed',
                        default=None)

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    rnd.seed(args.seed)

    adjectives = """bankrupt base caterwauling corrupt cullionly 
  detestable dishonest false filthsome filthy foolish foul gross 
  heedless indistinguishable infected insatiate irksome lascivious
  lecherous loathsome lubbery old peevish rascaly rotten ruinous 
  scurilous scurvy slanderous sodden-witted thin-faced toad-spotted 
  unmannered vile wall-eyed""".split()

    nouns = """Judas Satan ape ass barbermonger beggar block
  boy braggart butt carbuncle coward coxcomb cur dandy degenerate
  fiend fishmonger fool gull harpy jack jolthead knave liar
  lunatic maw milksop minion ratcatcher recreant rogue scold
  slave swine traitor varlet villain worm""".split()

    for _ in range(args.number):
        adj_string = ', '.join(rnd.sample(adjectives, args.adjectives))
        print(f'You {adj_string} {rnd.choice(nouns)}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
