#!/usr/bin/env python3
from ..game_engine import game_engine
from ..games.brain_gcd import brain_gcd


def main():
    rule = 'Find the greatest common divisor of given numbers.'
    game_engine(rule, brain_gcd)


if __name__ == '__main__':
    main()
