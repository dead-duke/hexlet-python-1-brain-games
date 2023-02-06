#!/usr/bin/env python3
from ..game_engine import game_engine
from ..games.brain_prime import brain_prime


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_engine(rule, brain_prime)


if __name__ == '__main__':
    main()
