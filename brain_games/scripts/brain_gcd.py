#!/usr/bin/env python3
from ..game_engine import start_game_engine
from ..games.gcd_game import start_gcd_game, gcd_rule


def main():
    start_game_engine(gcd_rule, start_gcd_game)


if __name__ == '__main__':
    main()
