#!/usr/bin/env python3
from ..game_engine import game_engine
from ..games.gcd_game import gcd_game, gcd_rule


def main():
    game_engine(gcd_rule, gcd_game)


if __name__ == '__main__':
    main()
