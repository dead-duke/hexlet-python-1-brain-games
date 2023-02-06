#!/usr/bin/env python3
from ..game_engine import game_engine
from ..games.brain_even import brain_even


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_engine(rule, brain_even)


if __name__ == '__main__':
    main()
