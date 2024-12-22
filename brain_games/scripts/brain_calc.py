#!/usr/bin/env python3
from ..game_engine import start_game_engine
from ..games.calc_game import calc_rule, start_calc_game


def main():
    start_game_engine(calc_rule, start_calc_game)


if __name__ == '__main__':
    main()
